import serial
import csv
import time
import sys

# Configurações da porta serial
porta_serial = 'COM4'  # Altere para a porta serial correta do seu sistema
baud_rate = 9600

# Abre a porta serial
try:
    ser = serial.Serial(porta_serial, baud_rate, timeout=1)
except serial.SerialException as e:
    print(f"Erro ao abrir a porta serial: {e}")
    sys.exit(1)

# Nome do arquivo CSV para salvar os dados
nome_arquivo_csv = 'Clibracao_TEMP_0108_90C.csv'

# Abre o arquivo CSV em modo de escrita
with open(nome_arquivo_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
   
    # Escreve o cabeçalho no arquivo CSV
    writer.writerow(['Temperatura Entrada Turbina', 'Temperatura Saida Turbina', 'Temperatura Saida Catalisador', 'Pressao coletor de escape', 'Pressao Saida Turbina'])

    try:
        while True:
            # Lê uma linha da porta serial
            line = ser.readline().decode().strip()
           
            # Divide a linha em valores individuais
            values = line.split(';')
           
            if len(values) == 5:  # Verifica se há 5 valores na linha
                try:
                    # Converte os valores para float
                    tempEntradaTurbina = float(values[0])
                    tempSaidaTurbina = float(values[1])
                    tempSaidaCatalisador = float(values[2])
                    pressaoColetor = float(values[3])
                    pressaoSaidaTurbina = float(values[4])
                   
                    # Escreve os valores no arquivo CSV
                    writer.writerow([tempEntradaTurbina, tempSaidaTurbina, tempSaidaCatalisador, pressaoColetor, pressaoSaidaTurbina])
                   
                    # Exibe os valores lidos no console (opcional)
                    print(f'TempEntradaTurbina: {tempEntradaTurbina} °C, TempSaidaTurbina: {tempSaidaTurbina} °C, TempSaidaCatalisador: {tempSaidaCatalisador} °C, Pressao Coletor: {pressaoColetor} PSI, Pressao Saida Turbina: {pressaoSaidaTurbina} PSI')
               
                except ValueError as e:
                    print(f"Erro ao converter valores para float: {e}")
           
            # Aguarda um intervalo entre leituras
            time.sleep(1)  # Intervalo de 1 segundo

    except KeyboardInterrupt:
        print("\nCaptura de dados encerrada pelo usuário.")

# Fecha a porta serial
ser.close()
