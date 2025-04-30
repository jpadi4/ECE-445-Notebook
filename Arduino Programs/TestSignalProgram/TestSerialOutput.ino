// example serial output (received by UART/Python program):
// Bridge 1: 1.8500 V | Bridge 2: 2.1000 V | Bridge 3: 0.7500 V | IMU: 1.6500 V

#define LED1 PIN_PB2     // LED1 output
#define LED2 PIN_PD3     // LED2 output
#define LED3 PIN_PD7     // LED3 output

#define vdiff  PIN_PC1   // Wheatstone bridge 1
#define vdiff1 PIN_PC2   // Wheatstone bridge 2
#define vdiff2 PIN_PC3   // Wheatstone bridge 3
#define imu    PIN_PC5   // IMU analog output

float adcToVoltage(int analogVal, float vRef = 3.7) {
    return (analogVal * vRef) / 1023.0;
}

void setup() {
  // Set analog pins as inputs (optional on most Arduino-like boards)
  pinMode(vdiff,  INPUT);
  pinMode(vdiff1, INPUT);
  pinMode(vdiff2, INPUT);
  pinMode(imu,    INPUT);

  // Set LED pins as outputs
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);

  Serial.begin(9600);  // Initialize Serial
}

void loop() {
  // Turn on all LEDs (optional)
  digitalWrite(LED1, HIGH);
  digitalWrite(LED2, HIGH);
  digitalWrite(LED3, HIGH);

  // Read all analog inputs
  int analog0 = analogRead(vdiff);
  int analog1 = analogRead(vdiff1);
  int analog2 = analogRead(vdiff2);
  int analog3 = analogRead(imu);

  // Read and convert all analog inputs
  // float voltage0 = adcToVoltage(analogRead(vdiff));    // Bridge 1
  // float voltage1 = adcToVoltage(analogRead(vdiff1));   // Bridge 2
  // float voltage2 = adcToVoltage(analogRead(vdiff2));   // Bridge 3
  // float voltage3 = adcToVoltage(analogRead(imu));      // IMU

  // Print all values
  Serial.print("Bridge 1: ");
  Serial.print(analog0);
  Serial.print(" | Bridge 2: ");
  Serial.print(analog1);
  Serial.print(" | Bridge 3: ");
  Serial.print(analog2);
  Serial.print(" | IMU: ");
  Serial.print(analog3);
  Serial.println("");

  delay(1000);  // Wait 1 second-- maybe alter this for higher frequency?
}