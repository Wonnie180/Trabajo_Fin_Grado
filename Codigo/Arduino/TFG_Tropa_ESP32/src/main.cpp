#include <UDPServer.hpp>
#include <CommandEnum.hpp>

#include "../lib/Led/Led/Led.hpp"
#include "../lib/Motor/Motor_DC/Motor_DC.hpp"
#include "../lib/Motor/Motor_Servo/Motor_Servo.hpp"
#include "../lib/Tropa/Tropa/Tropa.hpp"
#include "../lib/Communication/WifiClient/WifiClient.hpp"

// Declarations
void ProcessUDPPacket(AsyncUDPPacket packet); // Callback
void SerialCommand();                         // Callback

// Global Variables
// Primitive Types
String inString;
int command = -1;
int value = 0;

const char *ssid = "Bot-MindHive";
const char *pass = "LuisTFG2022";
const int port = 1234;
const uint8_t id = 1;
const char *hostname = "Tropa_1";

// Object Types
Led led = Led(2);

Motor_DC motorIzq = Motor_DC(15,4,18); // D15, D4, D18 | EnableA, In1, In2
Motor_DC motorDer = Motor_DC(32,12,33); // D35, D32, D12 | EnableB, In3, In4
// Motor_Servo motorIzq = Motor_Servo(12);
// Motor_Servo motorDer = Motor_Servo(4, true);
Tropa tropa = Tropa(id, led, motorIzq, motorDer);
WifiClient wifi = WifiClient(ssid, pass, hostname);
UDPServer udpServer = UDPServer(port, ProcessUDPPacket);

void setup()
{
  tropa.Set_MaxMiddleMinSpeeds(192, 32, 0);
  // tropa.Set_MaxMiddleMinSpeeds(15, 0, 0);

  // motorIzq.setMaxSpeed(89);
  // motorIzq.setMinSpeed(1);
  // motorDer.setMaxSpeed(89);
  // motorDer.setMinSpeed(1);
  // motorIzq.setOffset(-10);
  // motorDer.setOffset(-9);
  
  Serial.begin(115200);
  wifi.Start();
  udpServer.Start();
}

void loop()
{
  SerialCommand();
}

// Callback
void ProcessUDPPacket(AsyncUDPPacket packet)
{
  Serial.print("Command: ");
  CommandEnum command = static_cast<CommandEnum>(packet.data()[0]);
  switch (command)
  {
  case Forward:
    Serial.println("Move_Forward");
    tropa.Move_Forward();
    break;
  case Backwards:
    Serial.println("Move_Backward");
    tropa.Move_Backwards();
    break;
  case Turn_Left:
    Serial.println("Turn_Left");
    tropa.Turn_Left();
    break;
  case Turn_Right:
    Serial.println("Turn_Right");
    tropa.Turn_Right();
    break;
  case Change_Color:
    Serial.println("Change_Color");
    if (packet.length() < 4)
    {
      return;
    }
    tropa.Change_Color(packet.data()[1], packet.data()[2], packet.data()[3]);
    break;
  default:
    Serial.println("Not_Valid_Command");
  }
}

void ExecuteCommand()
{
  Serial.print("Command: ");
  Serial.print(command);
  Serial.print(" | Value: ");
  Serial.println(value);
  switch (command)
  {
  case Forward:
    Serial.println("Move_Forward");
    tropa.Move_Forward();
    break;
  case Backwards:
    Serial.println("Move_Backward");
    tropa.Move_Backwards();
    break;
  case Turn_Left:
    Serial.println("Turn_Left");
    tropa.Turn_Left();
    break;
  case Turn_Right:
    Serial.println("Turn_Right");
    tropa.Turn_Right();
    break;
  case 4:
    motorIzq.setOffset(value);
    break;
  case 5:
    motorDer.setOffset(value);
    break;
  case 6:
    motorIzq.ChangeSpeed(value);
    break;
  case 7:
    motorDer.ChangeSpeed(value);
    break;
  case 8:
    if (value > 0)
    {
      motorIzq.RotateLeft();
    }
    else
    {
      motorIzq.RotateRight();
    }
    break;
  case 9:
    if (value > 0)
    {
      motorDer.RotateLeft();
    }
    else
    {
      motorDer.RotateRight();
    }
    break;
  case 10:
    motorIzq.Stop();
    motorDer.Stop();
  case 11:
    motorIzq.setMaxSpeed(value);
    break;
  case 12:
    motorDer.setMaxSpeed(value);
    break;
  case 13:
    led.TurnOn();
    break;
  case 14:
    led.TurnOff();
    break;
  default:
    Serial.println("Not_Valid_Command");
  }

  command = -1;
  value = 0;
}

void SerialCommand()
{
  while (Serial.available())
  {
    char inChar = Serial.read();
    if (inChar == '\n')
    {
      value = inString.toInt();
      inString = "";
      ExecuteCommand();
    }
    else if (inChar >= '0' and inChar <= '9')
    {
      inString += inChar;
    }
    else if (inChar == ' ')
    {
      command = inString.toInt();
      inString = "";
    }
  }
}