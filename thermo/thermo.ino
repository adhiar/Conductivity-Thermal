#include <SD.h>
#include <SPI.h>
#include <SD.h>
#include "max6675.h"

int CLK = 19;
const int chipSelect = 10;

int thermoSO1 = 2;
int thermoCS1 = 3;

MAX6675 thermocouple1(CLK, thermoCS1, thermoSO1);

int thermoSO2 = 4;
int thermoCS2 = 5;

MAX6675 thermocouple2(CLK, thermoCS2, thermoSO2);

int thermoSO3 = 6;
int thermoCS3 = 7;

MAX6675 thermocouple3(CLK, thermoCS3, thermoSO3);

int thermoSO4 = 8;
int thermoCS4 = 9;

MAX6675 thermocouple4(CLK, thermoCS4, thermoSO4);


bool headerWritten = false;

void setup() {
  Serial.begin(9600);

  // Initialize SD card
  if (!SD.begin(chipSelect)) {
    while (1);
  }
}

void loggingTemperature() {
  float T1 = thermocouple1.readCelsius();
  float T2 = thermocouple2.readCelsius();
  float T3 = thermocouple3.readCelsius();
  float T4 = thermocouple4.readCelsius();
  float T5 = thermocouple5.readCelsius();

  Serial.print(T1);
  Serial.print(",");
  Serial.print(T2);
  Serial.print(",");
  Serial.print(T3);
  Serial.print(",");
  Serial.print(T4);
  
  File dataFile = SD.open("dat.txt", FILE_WRITE);
  if (dataFile) {
    // Check if header needs to be written
    if (!headerWritten) {
      // Write header
      dataFile.println("T1,T2,T3,T4,T5");
      headerWritten = true;
    }
    
    // Write data
    String data = String(T1) + "," + String(T2) + "," + String(T3) + "," + String(T4);
    dataFile.println(data);
    dataFile.close();
  } else {
    Serial.println("error opening data_thermal.txt");
  }
}

void loop() {
  loggingTemperature();
  delay(1000);
}
