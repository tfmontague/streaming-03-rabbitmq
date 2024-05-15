# See Hello World! Example at
# https://www.rabbitmq.com/tutorials/tutorial-one-python.html
# Name: Topaz Montague
# Date: 5/15/2024

import pika

# Define the message
message = "Hello, People!"

# Establish a connection with RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue="hello")

# Publish the message
channel.basic_publish(exchange="", routing_key="hello", body=message)
print(f" [x] Sent '{message}'")

# Close the connection
connection.close()
