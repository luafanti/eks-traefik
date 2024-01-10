import pika

# Connection parameters
rabbitmq_host = "rabbitmq.<YOUR_DOMAIN>"
rabbitmq_port = 5672
rabbitmq_username = "admin"
rabbitmq_password = "admin"

# Create a connection to the RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, credentials=pika.PlainCredentials(rabbitmq_username, rabbitmq_password)))

# Create a channel
channel = connection.channel()

# Define the queue to use
queue_name = "your_queue_name"

# Publish a message
message_body = "Hello, RabbitMQ!"
channel.basic_publish(exchange="", routing_key=queue_name, body=message_body)

print(f" [x] Sent '{message_body}'")

# Close the connection
connection.close()
