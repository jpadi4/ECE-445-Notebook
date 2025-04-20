#define LED1 PIN_PB2    // Pin for LED1 output
#define STRAIN_GAUGE_1 PIN_PC1 // Pin for wheatstonebridge config1

void setup() {
  pinMode(LED1, OUTPUT);
}

void loop() {
    // read analog val (0-1023)
    int analog1 = analogRead(STRAIN_GAUGE_1);

    // convert ADC val to voltage; 
    float VCC = 3.3;
    float voltage1 = (analog1 * VCC) / 1023.0;

    // if the voltage from the strain gauge > 1.1V
    if (voltage1 > 1.1) {  
      digitalWrite(LED1, HIGH); // Turn on LED
    } else {
      digitalWrite(LED1, LOW);  // Turn off LED
    }
}