# M2M Communication Using MQTT Example

 - This repository contains 2 folders:
   - ./sender/ contains a main.py intended for a device that will publish to a topic
   - ./receiver/ contains a main.py intended for a device that will subscribe to the same topic

Both devices need libraries installing, [see here!](https://projects.raspberrypi.org/en/projects/thonny-install-package)

Install "umqtt.simple" on the receiver and "umqtt.robust" on the sender

Each device also needs a "my_secrets.py" file in the root (adjacent to main.py), ensure this is not stored in your GitHub repository (add it to .gitignore)

- ssid: the wifi ssid
- wifi_password: self explanatory
- mqtt_host: the URL for your MQTT broker (e.g. HiveMQ)
- mqtt_client_id: a unique identifying string for your device that is unique for the MQTT broker (e.g. your HiveMQ cluster)
- mqtt_user, mqtt_password: these are your mqtt credentials (e.g. on your HiveMQ cluster you can make multiple sets of credentials with different access, it is not your username and password for you HiveMQ account itself)