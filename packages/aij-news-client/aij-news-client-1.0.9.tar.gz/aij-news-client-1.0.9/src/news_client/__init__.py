import os
from news_client.news_consumer import NewsConsumer

def callback(queue, body):
    """
    This method prints the articles.
    """

    _response = body.decode('utf-8')
    print(
        f"=============================\n"
        f"Received a message from the queue: {queue}\n"
        f"Message: {_response}\n"
        f"=============================\n"
    )


def main():
    """
    The main function to run the server and publish the news articles to the RabbitMQ queue
    """
    consumer = NewsConsumer(os.environ['AIJ_NEWS_PUBLISHER_HOST'] or 'localhost', callback)

    try:
        consumer.consume()
    except KeyboardInterrupt:
        consumer.destroy()

