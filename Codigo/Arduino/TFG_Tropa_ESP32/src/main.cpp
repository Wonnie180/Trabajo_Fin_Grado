#include <UDPServer.hpp>
#include <CommandEnum.hpp>

#include "../lib/Led/Led/Led.hpp"
#include "../lib/Motor/Motor_DC/Motor_DC.hpp"
#include "../lib/Motor/Motor_Servo/Motor_Servo.hpp"
#include "../lib/Tropa/Tropa/Tropa.hpp"
#include "../lib/Communication/WifiClient/WifiClient.hpp"

// Declarations
void ProcessUDPPacket(AsyncUDPPacket packet); // Callback

// Global Variables
// Primitive Types
const char *ssid = "Bot-MindHive";
const char *pass = "LuisTFG2022";
const int port = 1234;
const uint8_t id = 2;
const char *hostname = "Tropa_2";

// Object Types
Led led = Led(2);

// Motor_DC motorIzq = Motor_DC(15,4,18); // D15, D4, D18 | EnableA, In1, In2
// Motor_DC motorDer = Motor_DC(32,12,33); // D35, D32, D12 | EnableB, In3, In4
Motor_Servo motorIzq = Motor_Servo(12);
Motor_Servo motorDer = Motor_Servo(4, true);
Tropa tropa = Tropa(id, led, motorIzq, motorDer);
WifiClient wifi = WifiClient(ssid,pass,hostname);
UDPServer udpServer = UDPServer(port, ProcessUDPPacket);

void setup()
{
  /* If using Servo motors, uncomment the line bellow */
  motorIzq.setOffset(-7);
  Serial.begin(115200);
  wifi.Start();
  udpServer.Start();
}

void loop()
{
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
    if (packet.length() < 4){
      return;
    }
    tropa.Change_Color(packet.data()[1], packet.data()[2], packet.data()[3]);
    break;
  default:
    Serial.println("Not_Valid_Command");
  }
}