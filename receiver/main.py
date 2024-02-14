# Receiver

import network
import time
import json
from machine import Pin
from umqtt.simple import MQTTClient

# You need to create a secrets.py file with the following variables
from my_secrets import ssid, wifi_password, mqtt_user, mqtt_password, mqtt_client_id, mqtt_host

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, wifi_password)
while wlan.isconnected() == False:
    print('Waiting for connection...')
    time.sleep(1)
print("Connected to WiFi")

# Initialize our MQTTClient and connect to the MQTT server
mqtt_client = MQTTClient(
        client_id=mqtt_client_id,
        server=mqtt_host,
        ssl=True,
        port=0,
        ssl_params={'server_hostname': mqtt_host},
        user=mqtt_user,
        password=mqtt_password)


def message_received(topic, response):
    print("Message received!")
    print(f"message: {response}")
    print(f"topic: {topic}")


mqtt_subscribe_topic = "my_own_topic/message"
    
mqtt_client.connect()
mqtt_client.set_callback(message_received)
mqtt_client.subscribe(mqtt_subscribe_topic)

while True:
    mqtt_client.check_msg()
    
