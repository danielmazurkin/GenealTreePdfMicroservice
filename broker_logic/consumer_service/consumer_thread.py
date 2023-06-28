import pika
import threading


class ConsumerThread(threading.Thread):
    """Тред, который запускает Consumer для RabbitMQ"""

    def forming_pdf_report(self, ch, method, properties, body):
        """Этот callback и consumer проверяет наличие такого пользователя в БД."""
        body_data = body.decode('utf-8')
        print(" [x] Received %r" % body_data)

    def run(self):
        # Устанавливаем обработчик сообщений для очереди
        connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        channel = connection.channel()

        channel.queue_declare("pdf_forming")
        channel.basic_consume(queue="pdf_forming", on_message_callback=self.forming_pdf_report,
                              auto_ack=True)
        channel.start_consuming()
