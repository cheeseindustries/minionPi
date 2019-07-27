#include <Arduino.h>
#include <Wire.h>
#include <SoftwareSerial.h>
#include <MeOrion.h>


double angle_rad = PI/180.0;
double angle_deg = 180.0/PI;
double iSonicSensor;
MeUltrasonicSensor ultrasonic_3(3);
MeDCMotor motor_9(9);
MeDCMotor motor_10(10);
int speed = 50;

void setup(){
  Serial.begin(9600);
  Serial.write("connected");
}

void loop(){
  String command;
  if (Serial.available()){
    command = Serial.readStringUntil('\n');
  }
  if(command != NULL){
    if(command == "halt"){
      Serial.write(1);
      halt();
    }
    else if(command == "forward"){
      Serial.write(1);
      forward(speed);
    }
    else if(command == "back"){
      Serial.write(1);
      back(speed);
    }
    else if(command == "left"){
      Serial.write(1);
      left(speed);
    }
    else if(command == "right"){
      Serial.write(1);
      right(speed);
    }
    else if(command == "help"){
      Serial.write("Commands: forward, back, left, right, halt, help");
    }
    else{
      Serial.write(0);
    }
  }
}


void halt(){
  motor_9.run(0);
  motor_10.run(0);
}

void forward(int s){
  motor_9.run(-s);
  motor_10.run(s);
}

void left(int s){
  motor_9.run(100);
  motor_10.run(100);
}

void right(int s){
  motor_9.run(-100);
  motor_10.run(-100);
}

void back(int s){
  motor_9.run(s);
  motor_10.run(-s);
}

void readProxSensor(){
  
}
