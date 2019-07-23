#lightly edited example of MQTT client from http://www.steves-internet-guide.com/into-mqtt-python-client/

import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
	print("message received ", str(message.payload.decode("utf-8")))
	print("message topic: ", message.topic)
	print("message qos: ", message.qos)
	print("message retain flag: ", message.retain)


broker_adr="localhost"

print("Creating a new instance")
client=mqtt.Client("Client1")

client.on_message=on_message #function on_message is attached to callback

print("Connecting to MQTT broker")
client.connect(broker_adr)

client.loop_start()

print("Subscribing to topic", "house/office/light")
client.subscribe("house/office/light")

print("Publishing message to the topic", "house/office/light")
client.publish("house/office/light","OFF")

time.sleep(5)
client.loop_stop()


