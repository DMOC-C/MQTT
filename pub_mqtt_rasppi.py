import paho.mqtt.client as mqtt

broker = "192.168.0.117"

client = mqtt.Client()
client.connect(broker)

client.publish("LED", 1)
