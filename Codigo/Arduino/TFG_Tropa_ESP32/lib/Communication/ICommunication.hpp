#ifndef _ICommunication_H
#define _ICommunication_H


class ICommunication
{

public:
    virtual ~ICommunication() = default;
    virtual void Start() = 0;
    virtual void Stop() = 0;

protected:

};

#endif