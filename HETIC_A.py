import paho.mqtt.client as mqtt
import json, time, random
from datetime import datetime
from time import sleep

# Paramètres de connexion à compléter
# Nom du groupe sans espaces avec la nomenclature WEB2 ou WEB3
# Exemple : WEB2-GROUPE3
GROUPNAME = "WEB2-GROUPE10"
MQTT_BROKER = "hetic.arcplex.fr"

# Login et mot de passe du groupe
MQTT_USERNAME = "GROUPE10"
MQTT_PASSWORD = "14991799"
# un ID différent par Node
NODE_ID = ["48321769", "57316482", "46824375", "19375486", "15473684", "15492534"]
# ID du sensor
SENSOR_ID_1 = 110
SENSOR_ID_2 = 102

client = mqtt.Client("client")


def run(condition):
    while datetime.now().minute not in {0, 3, 8, 15, 23, 30, 35, 40, 45, 50, 55}:
        sleep(1)

    def task():
        for node in NODE_ID:
            client.username_pw_set(username=MQTT_USERNAME, password=MQTT_PASSWORD)
            client.connect(MQTT_BROKER)
            MQTT_TOPIC = GROUPNAME + "/" + node + "/" + str(SENSOR_ID_1)
            MQTT_MSG = json.dumps(
                {
                    "source_address": node,
                    "sensor_id": SENSOR_ID_1,
                    "tx_time_ms_epoch": int(time.time()),
                    "data": {"value": random.randint(0, 1)},
                }
            )
            client.publish(MQTT_TOPIC, MQTT_MSG)
            print("MQTT Mis à jour - Node %s Timestamp : %s" % (node, int(time.time())))
            client.username_pw_set(username=MQTT_USERNAME, password=MQTT_PASSWORD)

            client.connect(MQTT_BROKER)
            MQTT_TOPIC = GROUPNAME + "/" + node + "/" + str(SENSOR_ID_2)
            MQTT_MSG = json.dumps(
                {
                    "source_address": node,
                    "sensor_id": SENSOR_ID_2,
                    "tx_time_ms_epoch": int(time.time()),
                    "data": {"value": random.randint(0, 1)},
                }
            )
            client.publish(MQTT_TOPIC, MQTT_MSG)
            print("MQTT Mis à jour - Node %s Timestamp : %s" % (node, int(time.time())))
        client.disconnect()

    task()
    while condition == True:
        sleep(10)
        task()


run(True)
