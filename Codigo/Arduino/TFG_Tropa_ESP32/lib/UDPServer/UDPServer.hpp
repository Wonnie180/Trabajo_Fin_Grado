#ifndef _UDPServer_H
#define _UDPServer_H

#include "AsyncUDP.h"

class UDPServer
{
private:
    void (*callback)(AsyncUDPPacket);

public:
    ~UDPServer() = default;
    UDPServer(uint16_t port, void (*callback)(AsyncUDPPacket));
    void Start();   


protected:
    uint16_t port;
    AsyncUDP udp;
};

#endif
