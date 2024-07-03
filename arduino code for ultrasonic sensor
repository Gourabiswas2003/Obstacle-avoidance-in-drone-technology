  const int trigPinFront = 9;
  const int echoPinFront = 8;
  const int trigPinLeft = 7;
  const int echoPinLeft = 6;
  const int trigPinRight = 5;
  const int echoPinRight = 4;

  const int motorPin1 = 3;  
  const int motorPin2 = 10; 
  const int motorPin3 = 11; 
  const int motorPin4 = 12; 

  long duration;
  int distanceFront, distanceLeft, distanceRight;

  void setup() {
    Serial.begin(9600);
    pinMode(trigPinFront, OUTPUT);
    pinMode(echoPinFront, INPUT);
    pinMode(trigPinLeft, OUTPUT);
    pinMode(echoPinLeft, INPUT);
    pinMode(trigPinRight, OUTPUT);
    pinMode(echoPinRight, INPUT);
    pinMode(motorPin1, OUTPUT);
    pinMode(motorPin2, OUTPUT);
    pinMode(motorPin3, OUTPUT);
    pinMode(motorPin4, OUTPUT);
  }

  void loop() {
    distanceFront = getDistance(trigPinFront, echoPinFront);
    distanceLeft = getDistance(trigPinLeft, echoPinLeft);
    distanceRight = getDistance(trigPinRight, echoPinRight);

    if (distanceFront < 50) {
      Serial.print("Front: ");
      Serial.print(distanceFront);
      Serial.print(" cm, ");
    } else {
      Serial.print("Front: No obstacle, ");
    }

    if (distanceLeft < 50) {
      Serial.print("Left: ");
      Serial.print(distanceLeft);
      Serial.print(" cm, ");
    } else {
      Serial.print("Left: No obstacle, ");
    }

    if (distanceRight < 50) {
      Serial.print("Right: ");
      Serial.print(distanceRight);
      Serial.print(" cm");
    } else {
      Serial.print("Right: No obstacle");
    }

    Serial.println();

  }

  int getDistance(int trigPin, int echoPin) {
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    duration = pulseIn(echoPin, HIGH);
    int distance = duration * 0.034 / 2;
    return distance;
  }

