import json
import os
import time
from threading import Timer

import pandas as pd
import numpy as np
import sqlalchemy
import pika

from sqlalchemy import create_engine


class NewsPublisher:
    """
    A class to publish news articles to a RabbitMQ queue using the NewsAPI
    @param api_key: the api key to access the NewsAPI
    @param host: the host name of the RabbitMQ server
    @param queue_name: the name of the queue to publish the news articles
    """
    def __init__(self, host='localhost', queue_name='news_stream'):
        self.queue_name = queue_name
        # set up a connection to RabbitMQ
        self.host = host
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()
        self.sources = 'bbc-news, cnn, fox-news, google-news, time, wired, the-new-york-times, the-wall-street-journal, the-washington-post, usa-today, abc-news, associated-press, bloomberg, business-insider, cbs-news, cnbc, entertainment-weekly, espn, fortune, fox-sports, mtv-news, national-geographic, nbc-news, new-scientist, newsweek, politico, reddit-r-all, reuters, the-hill, the-huffington-post, the-verge, the-washington-times, vice-news'

        # if the database does not exist, create it
        if not os.path.exists('data/articles.db'):
            self.articles = create_engine('sqlite:///data/articles.db')
        else:
            self.articles = pd.read_sql_table('articles', 'sqlite:///data/articles.db')

        if not os.path.exists('data/headlines.db'):
            self.headlines = create_engine('sqlite:///data/headlines.db')
        else:
            self.headlines = pd.read_sql_table('headlines', 'sqlite:///data/headlines.db')

    def publish(self):
        """
        Publish the news articles to the RabbitMQ queue one by one...
        """
        for _article in self.articles['articles']:
            _body = json.dumps(_article).encode('utf-8')
            self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=_body)
            print(f"Published a news article to the queue: {_article['title']}")
            # wait for 1 second before publishing the next article
            time.sleep(1)

        for _headline in self.headlines['articles']:
            _body = json.dumps(_headline).encode('utf-8')
            self.channel.basic_publish(exchange='', routing_key=f"{self.queue_name}_headlines", body=_body)
            print(f"Published a news headline to the queue: {_headline['title']}")
            # wait for 1 second before publishing the next article
            time.sleep(1)
            
        # do not close the connection until the message is delivered
        if self.connection.is_open:
            self.connection.close()

        # call the function again after 60 seconds
        Timer(60, self.publish).start()



