import pika

class MessageController(object):

    EXCHANGE_NAME = 'records'
    EXCHANGE_TYPE = 'topic'
    ROUTING_KEY = 'records'
    QUEUE_NAME = 'test-queue'

    connection = None
    channel = None
    parameters = pika.URLParameters('amqp://guest:guest@localhost:5672/%2F')

    def open_connection(self):
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()
        self.channel.exchange_declare(
            exchange=self.EXCHANGE_NAME,
            exchange_type=self.EXCHANGE_TYPE)
        print("Opened connection to RabbitMQ")

    def close_connection(self):
        self.connection.close()
        print("Closed connection to RabbitMQ")

class Publisher(MessageController):

    def publish(self, message):
        self.channel.basic_publish(
            exchange=self.EXCHANGE_NAME,
            routing_key=self.ROUTING_KEY,
            body=message,
            properties=pika.BasicProperties(content_type='application/json', delivery_mode=1))

class Receiver(MessageController):

    consume_function = None

    def on_message(self, channel, method_frame, header_frame, body):
        self.consume_function(body)

    def setup_consumer(self, consume_function):
        self.consume_function = consume_function
        self.channel.queue_declare(queue=self.QUEUE_NAME)
        self.channel.queue_bind(
            queue=self.QUEUE_NAME,
            exchange=self.EXCHANGE_NAME,
            routing_key=self.ROUTING_KEY)
        self.channel.basic_consume(
            consumer_callback=self.on_message,
            queue=self.QUEUE_NAME)

    def start_consuming(self):
        self.channel.start_consuming()

    def stop_consuming(self):
        self.channel.stop_consuming()
