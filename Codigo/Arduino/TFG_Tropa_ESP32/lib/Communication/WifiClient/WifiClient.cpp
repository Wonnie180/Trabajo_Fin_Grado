#include "WifiClient.hpp"

WifiClient::WifiClient(const char *ssid, const char *password, const char *hostname)
{
    this->ssid = ssid;
    this->password = password;
    this->hostname = hostname;
}

void WifiClient::Start()
{
    this->Stop();
    WiFi.config(INADDR_NONE, INADDR_NONE, INADDR_NONE, INADDR_NONE);
    WiFi.hostname(this->hostname);
    WiFi.mode(WIFI_STA);
    WiFi.begin(this->ssid, this->password);
    while (WiFi.status() != WL_CONNECTED)
    {
        Serial.print(".");
        delay(500);
    }
    Serial.print("IP: ");
    Serial.print(WiFi.localIP());
    Serial.print(", Hostname: ");
    Serial.println(WiFi.getHostname());
}

void WifiClient::Stop()
{
    WiFi.disconnect(true, true);
}