#lightly edited example of MQTT client from http://www.steves-internet-guide.com/into-mqtt-python-client/

import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
	print("message received ", str(message.payload.decode("utf-8")))
	print("message topic: ", message.topic)
	print("message qos: ", message.qos)
	print("message retain flag: ", message.retain)

def on_log(client, userdata, level, buf):
	print("log: ", buf)

broker_adr="localhost"

print("Creating a new instance")
client=mqtt.Client("Client1")

client.on_message=on_message #function on_message is attached to callback
client.on_log=on_log #function is attached to log callback

print("Connecting to MQTT broker")
client.connect(broker_adr)

client.loop_start()

print("Subscribing to topic", "house/office/light")
client.subscribe("house/office/light")

iteration=0
msg="OFF"
while (iteration<5):
	if (iteration%2==0):
		msg="ON"
		#print("Publishing message to the topic", "house/office/light")
		client.publish("house/office/light",msg)
		time.sleep(2)
	else:
		msg="OFF"
		#print("Publishing message to the topic", "house/office/light")
		client.publish("house/office/light",msg)
		time.sleep(2)
	iteration+=1

time.sleep(5)
client.disconnect()
client.loop_stop()


