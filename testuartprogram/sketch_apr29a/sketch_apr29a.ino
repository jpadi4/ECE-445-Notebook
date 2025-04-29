void setup() {
  Serial.begin(9600);  // Initialize serial communication at 9600 baud
}

void loop() {
  Serial.println("Hello World");  // Send "Hello World" followed by a newline
  delay(1000);  // Wait 1 second before repeating
}
