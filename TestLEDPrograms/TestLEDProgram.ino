#define LED1 PIN_PB2    // Pin for LED1 output
#define LED2 PIN_PD3    // rename for actual pin names
#define LED3 PIN_PD7    // rename for actual pin names
#define STRAIN_GAUGE_1 PIN_PC1 // specifies using PB3 as an analog input pin
#define STRAIN_GAUGE_2 PIN_PC2 
#define STRAIN_GAUGE_3 PIN_PC3 


// !! CHANGE DEFINITIONS BASED ON SCHEMATIC

void setup() {
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
}

void loop() {
    // read analog val (0-1023)
    int analog1 = analogRead(STRAIN_GAUGE_1);
    int analog2 = analogRead(STRAIN_GAUGE_2);
    int analog3 = analogRead(STRAIN_GAUGE_3);


    // convert ADC val to voltage; 
    float VCC = 3.3;
    float voltage1 = (analog1 * VCC) / 1023.0;
    float voltage2 = (analog2 * VCC) / 1023.0;
    float voltage3 = (analog3 * VCC) / 1023.0;

    // if the voltage from the strain gauge > 1.1V
    if (voltage1 > 1.1) {  
      digitalWrite(LED1, HIGH); // Turn on LED
    } else {
      digitalWrite(LED1, LOW);  // Turn off LED
    }

    if (voltage2 > 1.1) {
        digitalWrite(LED2, HIGH);
    } else {
        digitalWrite(LED2, LOW);
    }

    if(voltage3 > 1.1) {
        digitalWrite(LED3, HIGH);
    } else {
        digitalWrite(LED3, LOW);
    }
}