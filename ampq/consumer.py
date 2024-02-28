import pika


def callback(ch, method, properties, body):
    # Função de retorno de chamada (callback) que será chamada quando uma
    # mensagem for recebida
    print(f'Mensagem recebida: {body}')


# Conectar-se ao servidor RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declarar a mesma fila que o produtor
channel.queue_declare(queue='example')

# Configurar a função de retorno de chamada para lidar com as mensagens
# recebidas
channel.basic_consume(queue='example',
                      on_message_callback=callback,
                      auto_ack=True)

print('Waiting for message...')
channel.start_consuming()
