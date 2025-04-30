// Test program that lights up 3 LEDs on the PCB

#define LED1 PIN_PB2    // Pin for LED1 output
#define LED2 PIN_PD3    // rename for actual pin names
#define LED3 PIN_PD7    // rename for actual pin names

// !! CHANGE DEFINITIONS BASED ON SCHEMATIC

void setup() {
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
}

void loop() {

    // Light up LEDs
    digitalWrite(LED1, HIGH); // Turn on LED
    digitalWrite(LED2, HIGH);
    digitalWrite(LED3, HIGH);
}