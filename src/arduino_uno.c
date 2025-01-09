pwm code
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <Keypad.h>

const byte ROWS = 4;
const byte COLS = 4;
char keys[ROWS][COLS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};
byte rowPins[ROWS] = {9, 8, 7, 6}; // Connect to the row pins of the keypad
byte colPins[COLS] = {5, 4, 3, 2}; // Connect to the column pins of the keypad

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

// Initialize the LCD (16x2 display)
LiquidCrystal_I2C lcd(0x27, 16, 2); // Adjust 0x27 to your I2C address

// Motor Driver Pins
#define ENA 10   // PWM pin for motor speed
#define IN1 12   // Motor driver input 1
#define IN2 13   // Motor driver input 2

// Variables
int speedValue = 0; // Store current speed value

void setup() {
  // Initialize the Serial Monitor
  Serial.begin(9600);

  // Set motor driver pins as outputs
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);

  // Initialize the LCD
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Flow Rate Control");

  // Stop motor initially
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);

  // Print instructions on the Serial Monitor
  Serial.println("Enter keys (2-8) for speeds:");
}

void loop() {
   if (Serial.available()) {
    // Read the incoming data from Serial (ESP32)
    String incomingData = Serial.readString();

    // Print the received data to the Arduino Serial Monitor
    Serial.print("Received from ESP32: ");
    Serial.println(incomingData);
  }

  // Check for a key press on the keypad
  char key = keypad.getKey();

  // If a key is pressed, adjust the speed value
  if (key) {
    if (key == '0'){
      speedValue = 0;
      triggerPump(speedValue);
    }
    if (key=='1'){
      speedValue = 25;
      triggerPump(speedValue);
    }
    // Assign speeds for keys 2–8
    if (key == '2') {
      speedValue = 50;   // Low speed
      triggerPump(speedValue);
    }
    else if (key == '3') {
      speedValue = 80;
      triggerPump(speedValue);
    }
    else if (key == '4') {
      speedValue = 110;
      triggerPump(speedValue);
    }
    else if (key == '5') {
      speedValue = 140;
      triggerPump(speedValue);
    }
    else if (key == '6') {
      speedValue = 170;
      triggerPump(speedValue);
    }
    else if (key == '7') {
      speedValue = 200;
      triggerPump(speedValue);
    }
    else if (key == '8') {
      speedValue = 230; // High speed
      triggerPump(speedValue);
    }
    else {
      // Invalid input
      Serial.println("Invalid key! Enter a number between 2 and 8.");
      return;
    }

    // Print the current speed on Serial Monitor
    Serial.print("Speed set to: ");
    Serial.println(speedValue);

    // Update LCD display
    lcd.setCursor(0, 1);
    lcd.print("Speed: ");
    lcd.print(speedValue);
    lcd.print("      "); // Clear extra characters
  }
}

// Function to control pump (motor)
void triggerPump(int speed) {
  // Control motor direction (forward)
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);

  // Set motor speed with PWM
  analogWrite(ENA, speed);
}