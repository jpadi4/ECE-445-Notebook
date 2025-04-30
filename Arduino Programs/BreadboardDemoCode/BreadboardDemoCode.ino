#define LED_PIN PIN_PB1   // Pin for LED output
#define STRAIN_GAUGE_0 A1 // specifies using PB3 as an analog input pin


void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
    // read analog val (0-1023)
    int analogValue = analogRead(STRAIN_GAUGE_0);

    // convert ADC val to voltage; 
    float VCC = 3.3;
    float voltage = (analogValue * VCC) / 1023.0;

    // if the voltage from the strain gauge > 1.1V
    if (voltage > 1.1) {  
      digitalWrite(LED_PIN, HIGH); // Turn on LED
    } else {
      digitalWrite(LED_PIN, LOW);  // Turn off LED
    }
}
