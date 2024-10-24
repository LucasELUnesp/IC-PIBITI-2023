#include "max6675.h"

// Definição dos pinos para cada MAX6675
const int thermoCLK[] = {30, 36, 42, 48, 53};  // CLK para cada MAX6675
const int thermoCS[] = {28, 34, 40, 46, 52};   // CS para cada MAX6675
const int thermoDO[] = {26, 32, 38, 44, 50};   // DO para cada MAX6675

// Pino do sensor de pressão PS10
const int pressurePin1 = A1; // Conecte o PS500 ao pino A1
const int pressurePin2 = A2; // Conecte o PS500 ao pino A2
// Inicialização dos objetos MAX6675 para cada termopar
MAX6675 thermocouples[] = {
  MAX6675(thermoCLK[0], thermoCS[0], thermoDO[0]),
  MAX6675(thermoCLK[1], thermoCS[1], thermoDO[1]),
  MAX6675(thermoCLK[2], thermoCS[2], thermoDO[2])
};

void setup() {
  Serial.begin(9600);
  Serial.println("MAX6675 e PS10 test");

  // Aguarda estabilização dos chips MAX6675
  delay(500);

  Serial.println("Módulos MAX6675 e sensores de pressão PS500 inicializados com sucesso!");
}

void loop() {
  // Realiza a leitura de cada termopar
  float tempEntradaTurbina = thermocouples[1].readCelsius();
  float tempSaidaTurbina = thermocouples[2].readCelsius();
  float tempSaidaCatalisador = thermocouples[3].readCelsius();
  
  // Leitura do sensor de pressão PS500 -1
  int sensorValue = analogRead(pressurePin1);
  // Conversão do valor analógico para pressão (considerando que o sensor PS500 varia de 0.5 a 4.5V)
 float voltage = sensorValue * (5.0 / 1023.0);
  float pressure1 = (voltage- 0.5 ) * (34.4738 / (4.5 - 0.5)); // Conversão para bar
 
 // Leitura do sensor de pressão PS500 -2
 int sensorValue = analogRead(pressurePin2);
  // Conversão do valor analógico para pressão (considerando que o sensor PS500 varia de 0.5 a 4.5V)
 float voltage = sensorValue * (5.0 / 1023.0);
  float pressure2 = (voltage- 0.5 ) * (34.4738 / (4.5 - 0.5)); // Conversão para bar

  // Envia os valores para o monitor serial
  Serial.print(tempEntradaTurbina);
  Serial.print(";");
  Serial.print(tempSaidaTurbina);
  Serial.print(";");
  Serial.print(tempSaidaCatalisador);
  Serial.print(";");
  Serial.println(pressure1);
   Serial.print(";");
  Serial.println(pressure2);

  // Para que o MAX6675 atualize, é necessário um atraso de pelo menos 250 ms entre as leituras
  delay(1000); // Atraso entre leitura