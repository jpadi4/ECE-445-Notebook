
#define LED1 PIN_PB2    // Pin for LED1 output
#define LED2 PIN_PD3    // Pin for LED2 output
#define LED3 PIN_PD7    // Pin for LED3 output

#define vdiff PIN_PC1     // Pin for wheatstone bridge 1 signal input
#define vdiff1 PIN_PC2    // Pin for wheatstone bridge 2 signal input
#define vdiff2 PIN_PC3    // Pin for wheatstone bridge 3 signal input

#define imu PIN_PC5       // Pin for IMU signal input

void setup() {
  // sensor layer subsystem inputs
  pinMode(vdiff, INPUT);
  pinMode(vdiff1, INPUT);
  pinMode(vdiff2, INPUT);
  pinMode(imu, INPUT);

  // communication subsystem LEDs
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);

  Serial.begin(9600);  // Initialize serial communication at 9600 baud
}

void loop() {
  Serial.println("Hello World!");  // MCU sends "Hello World" followed by a newline

  // turn on all LEDs
  digitalWrite(LED1, HIGH);
  digitalWrite(LED2, HIGH);
  digitalWrite(LED3, HIGH);

  // read analog val (0-1023)
  int analog1 = analogRead(vdiff);

  // convert ADC val to voltage; 
  float VCC = 3.7;
  float voltage1 = (analog1 * VCC) / 1023.0;

  // print out analog value
  Serial.print("Voltage: ");
  Serial.print(voltage1, 4);  // 2 decimal places
  Serial.println(" V");
 
  delay(1000);  // Wait 1 second before repeating
}
