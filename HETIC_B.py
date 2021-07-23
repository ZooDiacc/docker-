import paho.mqtt.client as mqtt
import json, time, random
from datetime import datetime
from time import sleep

# Paramètres de connexion à compléter
# Nom du groupe sans espaces avec la nomenclature WEB2 ou WEB3
# Exemple : WEB2-GROUPE3

# Login et mot de passe du groupe


GROUPNAME = "GROUPE7"

MQTT_USERNAME = "GROUPE7"
MQTT_PASSWORD = "64459019"
MQTT_BROKER = "hetic.arcplex.fr"
# un ID différent par Node
NODE_ID = [
    "12345678",
    "7654321",
    "1274555678",
    "7654931",
    "845217199",
    "741852963",
    "12342255678",
    "7622554321",
    "127455777",
    "7652254931",
    "999999",
    "4444555",
]

# ID du sensor
SENSOR_ID_1 = 126
SENSOR_ID_2 = 133
SENSOR_ID_3 = 109


# Type de donnée renvoyée : Random 0 ou 1
VALMIN = 28
VALMAX = 29

client = mqtt.Client("client")
client.username_pw_set(username=MQTT_USERNAME, password=MQTT_PASSWORD)
client.connect(MQTT_BROKER)


def run(condition):
    while datetime.now().minute not in {0, 3, 8, 15, 23, 30, 35, 40, 45, 50, 55}:
        sleep(1)

    def task():
        for node in NODE_ID:
            MQTT_TOPIC = GROUPNAME + "/" + node + "/" + str(SENSOR_ID_1)
            MQTT_MSG = json.dumps(
                {
                    "source_address": node,
                    "sensor_id": SENSOR_ID_1,
                    "tx_time_ms_epoch": int(time.time()),
                    "data": {"value": round(random.uniform(0, 100), 2)},
                }
            )

            client.publish(MQTT_TOPIC, MQTT_MSG)
            print("MQTT Mis à jour - Node %s Timestamp : %s" % (node, int(time.time())))
            MQTT_TOPIC = GROUPNAME + "/" + node + "/" + str(SENSOR_ID_2)
            MQTT_MSG = json.dumps(
                {
                    "source_address": node,
                    "sensor_id": SENSOR_ID_2,
                    "tx_time_ms_epoch": int(time.time()),
                    "data": {"value": round(random.uniform(0, 50), 2)},
                }
            )

            client.publish(MQTT_TOPIC, MQTT_MSG)
            print("MQTT Mis à jour - Node %s Timestamp : %s" % (node, int(time.time())))
            MQTT_TOPIC = GROUPNAME + "/" + node + "/" + str(SENSOR_ID_3)
            MQTT_MSG = json.dumps(
                {
                    "source_address": node,
                    "sensor_id": SENSOR_ID_3,
                    "tx_time_ms_epoch": int(time.time()),
                    "data": {"value": round(random.uniform(0, 65535), 2)},
                }
            )

            client.publish(MQTT_TOPIC, MQTT_MSG)
            print("MQTT Mis à jour - Node %s Timestamp : %s" % (node, int(time.time())))

    task()
    while condition == True:
        sleep(60 * 15)
        task()


run(True)
