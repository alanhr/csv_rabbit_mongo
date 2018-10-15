import os
import pika

RABBIT_USER = os.environ.get('RABBIT_USER', 'rabbitmq')
RABBIT_PASSWORD = os.environ.get('RABBIT_PASSWORD', 'rabbitmq')
RABBIT_HOST = os.environ.get('RABBIT_HOST', 'localhost')


class Consume():
    def __init__(self):
        credentials = pika.PlainCredentials(RABBIT_USER, RABBIT_PASSWORD)
        self.__connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=RABBIT_HOST, credentials=credentials))

    def __get_channel(self):
        return self.__connection.channel()

    def close(self):
        self.__get_channel().stop_consuming()
        self.__connection.close()

    def run(self, queue_name, callback):
        channel = self.__get_channel()

        channel.queue_declare(queue_name)

        channel.basic_consume(callback, queue_name)

        channel.start_consuming()
