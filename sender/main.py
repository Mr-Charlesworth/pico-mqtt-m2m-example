# Sender

import network
import time
import json
from machine import Pin
from umqtt.robust import MQTTClient

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

# Your topic can be created in your device profile on thingsboardshu.cloud
mqtt_publish_topic = "my_own_topic/message"

# Initialize our MQTTClient and connect to the MQTT server
mqtt_client = MQTTClient(
        client_id=mqtt_client_id,
        server=mqtt_host,
        port=0,
        ssl=True,
        ssl_params={'server_hostname': mqtt_host},
        user=mqtt_user,
        password=mqtt_password)

mqtt_client.connect()

button = Pin(0, Pin.IN, Pin.PULL_UP)
message_sent = False

try:
    while True:
        if(button.value() == 0):
            if (not message_sent):
                data = json.dumps({ 'message': 'nathen' })
                print(data)
                mqtt_client.publish(mqtt_publish_topic, data)
                message_sent = True
        else:
            message_sent = False
except Exception as e:
    print(f'Failed to publish message: {e}')
finally:
    mqtt_client.disconnect()
