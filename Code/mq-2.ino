#include "WiFi.h"
#include "HTTPClient.h"

const char ssid = "KRATON 1";        
const char password = "Katasandi123"; 
const char serverName = "http://192.168.1.12:5000/data"; //alamat IP server lokal
const int mqPin = 4;

void setup() {
  
  Serial.begin(9600);
  pinMode(mqPin, INPUT);
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  int sensorValue = digitalRead(mqPin);

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    
    http.begin(serverName);
    http.addHeader("Content-Type", "application/json");

    String jsonPayload = "{\"smoke_detected\":" + String(sensorValue) + "}";

    int httpResponseCode = http.POST(jsonPayload);

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println(httpResponseCode);
      Serial.println(response);
    } else {
      Serial.print("Eror Post : ");
      Serial.println(httpResponseCode);
    }
    
    http.end();
  } else {
    Serial.println("Eror wifi konek");
  }
  delay(5000);
}
