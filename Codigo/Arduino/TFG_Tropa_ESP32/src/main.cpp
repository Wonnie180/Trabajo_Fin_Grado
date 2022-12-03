#include <UDPServer.hpp>
#include <CommandEnum.hpp>

#include "../lib/Led/Led/Led.hpp"
#include "../lib/Motor/Motor_DC/Motor_DC.hpp"
#include "../lib/Tropa/Tropa/Tropa.hpp"
#include "../lib/Communication/WifiClient/WifiClient.hpp"

// Declarations
void ProcessUDPPacket(AsyncUDPPacket packet); // Callback

// Global Variables
// Primitive Types
const char *ssid = "DD-WRT"; 
const char *pass = "Sup0sitorio";
const int port = 1234;
const uint8_t id = 1;
const char *hostname = "Tropa_1";

// Object Types
Led led = Led(2);
Motor_DC motor_izq = Motor_DC(15,4,5); // D15, D4, RX2 | EnableA, In1, In2
//Motor_DC motor_Der = Motor_DC(22,27,34); // D2, TX2, D5 | EnableB, In3, In4
Tropa tropa = Tropa(id, led, motor_izq, motor_izq);
WifiClient wifi = WifiClient(ssid,pass,hostname);
UDPServer udpServer = UDPServer(port, ProcessUDPPacket);

void setup()
{
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