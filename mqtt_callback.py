#lightly edited example of MQTT client from http://www.steves-internet-guide.com/mqtt-python-callbacks/
#Callback is a function called in response to some event.
#API of MQTT client: https://pypi.org/project/paho-mqtt/#callbacks

import paho.mqtt.client as mqtt
import time

def on_log(client, userdata, level, buf):
	print("log: ", buf)

def on_message(client, userdata, message):
	print("message received ", str(message.payload.decode("utf-8")))
	print("message topic: ", message.topic)
	print("message qos: ", message.qos)
	print("message retain flag: ", message.retain)

def on_connect(client, userdata, flags, rc):	
	global loop_flag
	print("In on_connect callback")
	loop_flag=0


broker_adr="localhost"

print("Creating a new instance")
client=mqtt.Client("Client1")

client.on_log=on_log #function on_log is attached to log callback
#client.on_message=on_message #function on_message is attached to message callback
client.on_connect=on_connect #function is attached to callback

print("Connecting to MQTT broker")
client.connect(broker_adr)

client.loop_start() #loop is started to process callbacks

#Callback is triggered when the client receives a connection acknowledgment message
loop_flag=1
iteration=0
while (loop_flag==1):
	print("Waiting for connect callback ", iteration)
	time.sleep(.01)
	iteration+=1

client.disconnect()
client.loop_stop() #loop is ended


