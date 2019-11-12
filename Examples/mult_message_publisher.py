import paho.mqtt.client as mqtt

broker_url = "test.mosquitto.org"
broker_port = 1883

client = mqtt.Client()
client.connect(broker_url, broker_port)

client.publish(topic="TestingTopic", payload="TestingPayload", qos=1, retain=False)
client.publish("KitchenTopic", "KitchenPayload", 1)
client.publish("BedroomTopic", "BedroomPayload", 1)
