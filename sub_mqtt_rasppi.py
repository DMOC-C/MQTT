from gpiozero import LED
import paho.mqtt.client as mqtt

led = LED(17)
broker = "192.168.0.117"
messages = []


def on_connect(client, userdata, flags, rc):
    print(f"Connected With Result Code: {rc}")


def on_disconnect(client, userdata, rc):
    print("Client Got Disconnected")


def on_message(client, userdata, message):
    msg = message.payload.decode()
    topic = message.topic
    messages.append(topic, msg)


client = mqtt.Client()

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.connect(broker)

client.subscribe("LED")
client.publish("LED", 1)

if len(messages) > 0:
    mess = messages.pop(0)
    print(f"Received {mess}")
    if mess[1]:
        led.on()
    elif not mess[1]:
        led.off()

client.loop_forever()
