import pika
import os

from producer_interface import mqProducerInterface
class mqProducer(mqProducerInterface):
    def __init__(self, routing_key: str, exchange_name: str) -> None:
        # Save parameters to class variables
        self.routing_key = routing_key
        self.exchange_name = exchange_name
        # Call setupRMQConnection
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        connection = pika.BlockingConnection(parameters=con_params)
        # Establish Channel
        channel = connection.channel()
        # Create the exchange if not already present
        if exchange is None:
            exchange = channel.exchange_declare(exchange=exchange_name)


    def publishOrder(self, message: str) -> None:
        # Basic Publish to Exchange
        channel.basic_publish(
            exchange=exchange_name,
            routing_key=routing_key,
            body=message,
        )
        # Close Channel
        channel.close()

        # Close Connection
        connection.close()


