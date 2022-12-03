#ifndef _Wifi_H
#define _Wifi_H

#include <WiFi.h>
#include "../ICommunication.hpp"

class WifiClient : public ICommunication
{
private:

public:
    ~WifiClient() = default;
    WifiClient(const char *ssid, const char* password, const char* hostname);
    void Start();
    void Stop();

protected:
    const char* ssid;
    const char* password;
    const char* hostname;
};

#endif
