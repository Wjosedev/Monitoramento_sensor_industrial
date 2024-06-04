#Integração com Serviços em Nuvem (Exemplo com AWS IoT Core):
#Baixar a biblioteca AWSIoTPythonSDK

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time
import json

# Configurações do cliente MQTT
host = "XXXXXXXXXXXXXX.iot.us-west-2.amazonaws.com"
rootCAPath = "root-CA.crt"
certificatePath = "certificate.pem.crt"
privateKeyPath = "private.pem.key"
clientId = "basicPubSub"
topic = "sensor/dados"

# Inicializa o cliente MQTT
myMQTTClient = AWSIoTMQTTClient(clientId)
myMQTTClient.configureEndpoint(host, 8883)
myMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# Conecta ao AWS IoT Core
myMQTTClient.connect()

def enviar_dados_aws_iot(temperatura, umidade):
    payload = {
        "temperatura": temperatura,
        "umidade": umidade
    }
    myMQTTClient.publish(topic, json.dumps(payload), 1)
    print("Dados enviados para AWS IoT Core:", payload)

def main():
    while True:
        temperatura, umidade = ler_sensor()
        enviar_dados_aws_iot(temperatura, umidade)
        time.sleep(5)  # Envia dados a cada 5 segundos

if __name__ == "__main__":
    main()
