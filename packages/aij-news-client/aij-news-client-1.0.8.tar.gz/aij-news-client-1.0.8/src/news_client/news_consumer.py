import pika


class NewsConsumer:
    """
    This class implements a RabbitMQ consumer.
    """
    def __init__(self, host, callback_function):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='news_stream')
        self.callback_function = callback_function

    def consume(self):
        """
        This method starts consuming messages from the RabbitMQ queue.
        """
        self.channel.basic_consume(queue='news_stream', on_message_callback=self.callback, auto_ack=True)
        self.channel.start_consuming()

    def callback(self, ch, method, properties, body):
        self.callback_function(method.routing_key, body) 

    def destroy(self):
        """
        This method closes the connection to the RabbitMQ server.
        """
        if self.connection.is_open:
            self.connection.close()