from mongoengine import connect
import json

from csv_read.Consume import Consume
from csv_read.UserCreate import create


def on_message(channel, method_frame, header_frame, body):
    body_parse = json.loads(body)

    try:
        create(body_parse)
    except Exception as error:
        print(error)

    channel.basic_ack(delivery_tag=method_frame.delivery_tag)


def main():
    consume = Consume()

    try:
        consume.run('user', on_message)
    except KeyboardInterrupt:
        consume.close()


if __name__ == '__main__':
    connect(db='users')

    main()
