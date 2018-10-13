import os
import pika
import json

RABBIT_USER = os.environ.get('RABBIT_USER', 'rabbitmq')
RABBIT_PASSWORD = os.environ.get('RABBIT_PASSWORD', 'rabbitmq')
RABBIT_HOST = os.environ.get('RABBIT_HOST', 'localhost')

class Queue():
    def __init__(self):
        credentials = pika.PlainCredentials(RABBIT_USER, RABBIT_PASSWORD)
        self.__connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=RABBIT_HOST, credentials=credentials))
    
    def __get_channel(self):
        return self.__connection.channel()
    
    def send_batch(self,index,items):
        channel = self.__get_channel()

        channel.queue_declare(queue=index)

        for item in items:
              channel.basic_publish(exchange='',
                                    routing_key=index,
                                    body=json.dumps(item))
    
    def close(self):
        self.__connection.close()


        
        
