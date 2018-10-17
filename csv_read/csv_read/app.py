import json
import logging
from time import sleep
from mongoengine import connect
import os

from csv_read.Consume import Consume
from csv_read.UserCreate import create


MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def on_message(channel, method_frame, header_frame, body):
    body_parse = json.loads(body)

    try:
        user = create(body_parse)

        logger.info('User create {}'.format(user.email))
    except Exception as error:
        logger.error(error)

    channel.basic_ack(delivery_tag=method_frame.delivery_tag)


def main():

    logger.info('Init APP')
    
    consume = Consume()

    try:
        consume.run('user', on_message)
    except KeyboardInterrupt:
        logger.info('Finishing APP')
        consume.close()


if __name__ == '__main__':
    connect(db='users', host=MONGO_HOST)

    main()
