from kafka import KafkaProducer


class KafkaOutput:

    def __init__(self):
        self.counter = 0
        self.topic = None
        self.bootstrap_servers = None
        self.producer = None

    def set_params(self, topic, bootstrap_servers):
        self.topic = topic
        self.bootstrap_servers = bootstrap_servers

    def create_producer(self):
        self.producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers)

    def send_data(self, msg):
        self.producer.send(self.topic, msg.encode("UTF-8")).add_callback(self.on_send_success())

    def on_send_success(self):
        self.counter += 1

    def end(self):
        self.producer.flush()


if __name__ == '__main__':
    connection_str = ["localhost:9092"]
    topic = "my-topic"
    kafka_output = KafkaOutput()
    kafka_output.set_params(topic, connection_str)
    print("Creating Kafka producer")
    kafka_output.create_producer()

    msg_to_send = "Hello my friend: "

    for i in range(20):
        payload = msg_to_send + str(i)
        kafka_output.send_data(payload)

    kafka_output.end()
    # Put counter after flush because send_data async
    print("Number of data sent: ", kafka_output.counter)
