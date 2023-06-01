import pika
import threading


class ConsumerThread(threading.Thread):
    """Тред, который запускает Consumer для RabbitMQ"""

    def callback_check_user(self, ch, method, properties, body):
        """Этот callback и consumer проверяет наличие такого пользователя в БД."""
        print(" [x] Received %r" % body)

    def run(self):
        # Устанавливаем обработчик сообщений для очереди
        connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        channel = connection.channel()

        channel.queue_declare("auth_queue")
        channel.basic_consume(queue="auth_queue", on_message_callback=self.callback_check_user, auto_ack=True)
        channel.start_consuming()
