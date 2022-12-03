#include "UDPServer.hpp"

UDPServer::UDPServer(uint16_t port, void (*callback)(AsyncUDPPacket)){
    this->port = port;
    this->callback = callback;
}

void UDPServer::Start(){
    this->udp.listen(this->port);
    
    void (*callback)(AsyncUDPPacket) = this->callback;

    this->udp.onPacket([callback](AsyncUDPPacket packet){ 
        callback(packet); 
    });
}
