import paho.mqtt.client as mqtt

broker_url = "test.mosquitto.org"
broker_port = 1883


def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code: {}".format(rc))


def on_disconnect(client, userdata, rc):
    print("Client Got Disconnected")


client = mqtt.Client()
client.on_connect = on_connect
client.connect(broker_url, broker_port)
client.on_disconnect = on_disconnect

client.subscribe("TestingTopic", qos=1)

client.publish(topic="TestingTopic", payload="TestingPayload", qos=1, retain=False)

client.loop_forever()
