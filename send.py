import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare('hello')

channel.basic_publish(exchange='',
					routing_key='hello',
					body='Hello world!')

connection.close()