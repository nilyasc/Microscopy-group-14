const int stepX1 = 2; // Step pin for motor 1
const int dirX1  = 5; // Direction pin for motor 1

const int stepX2 = 3; // Step pin for motor 2
const int dirX2  = 6; // Direction pin for motor 2

const int enPin = 8;  // Enable pin for motor drivers

const int steppattern[4] = {HIGH, LOW, HIGH, LOW};

void setup() {
  pinMode(stepX1, OUTPUT);
  pinMode(dirX1, OUTPUT);

  pinMode(stepX2, OUTPUT);
  pinMode(dirX2, OUTPUT);

  pinMode(enPin, OUTPUT);

  digitalWrite(enPin, LOW); // Enable both motor drivers
}

void loop() {
  // Move in X direction (both motors same direction)
  for (int v=0; v < 4; v++){
    for (int u=0; u < 5; u++){
      delay(1000); // Wait 1 second
      digitalWrite(dirX1, steppattern[v]);
      digitalWrite(dirX2, steppattern[v]);
      rotateMotors(); 
    }
    if (v < 3) {
      delay(1000); // Wait 1 second
      digitalWrite(dirX1, LOW);
      digitalWrite(dirX2, HIGH);
      rotateMotors();
    }
  }
  for (int y=0; y < 3; y++) {
    delay(1000); // Wait 1 second
    digitalWrite(dirX1, HIGH);
    digitalWrite(dirX2, LOW);
    rotateMotors();
  }
}

void rotateMotors() {
  for (int i = 0; i < 800; i++) { // Number of steps per move
    // Generate step pulse for motor 1
    digitalWrite(stepX1, HIGH);
    // Generate step pulse for motor 2
    digitalWrite(stepX2, HIGH);

    delayMicroseconds(1000); // Step pulse duration

    digitalWrite(stepX1, LOW);
    digitalWrite(stepX2, LOW);

    delayMicroseconds(1000); // Pause between steps
  }
}
