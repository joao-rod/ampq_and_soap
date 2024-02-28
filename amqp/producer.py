import pika


# Conectar-se ao servidor RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declarar uma fila chamada 'example'
channel.queue_declare(queue='example')

# Enviar uma mensagem para a fila
MESSAGE = input('Digite a mensagem: ')
channel.basic_publish(exchange='',
                      routing_key='example',
                      body=MESSAGE)

print(f'Mensagem enviada: {MESSAGE}')

# Fechar a conexão
connection.close()
