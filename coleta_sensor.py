import time
import random

def ler_sensor():
    # Simulação de leitura de dados do sensor
    temperatura = random.uniform(20, 50)
    umidade = random.uniform(40, 80)
    return temperatura, umidade

def main():
    while True:
        temperatura, umidade = ler_sensor()
        # Enviar dados para processamento ou armazenamento em nuvem
        print(f"Temperatura: {temperatura}°C, Umidade: {umidade}%")
        time.sleep(1)  # Simula intervalo de leitura dos sensores

if __name__ == "__main__":
    main()
