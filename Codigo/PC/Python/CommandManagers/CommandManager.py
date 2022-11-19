import os
import sys
from typing import List

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(os.path.join(os.path.dirname(__file__), ".." + os.path.sep))

from ICommandManager import ICommandManager
from Commands.ICommand import ICommand
from AbleInterfaces.Runnable import Runnable
from time import sleep 

class CommandManager(ICommandManager, Runnable):
    def __init__(self):
        super().__init__()

    def Run(self):
        while not self.has_to_stop:
            self.Execute_Commands()            
            sleep(0.0008)

    def Stop(self):
        self.has_to_stop = True

    def Add_Command(self, command: ICommand):
        self.commands.append(command)

    def Execute_Commands(self):
        if len(self.commands) < 1:            
            return
        commands_to_remove : List[ICommand] = []
        for command in self.commands:
            command.Execute_Command()
            if command.Have_Finished_Command():
                commands_to_remove.append(command)

        self.Remove_Finished_Commands(commands_to_remove)
                
    def Remove_Finished_Commands(self, commands_to_remove: List[ICommand]):
        for command in commands_to_remove:
            if command in self.commands:
                self.commands.remove(command)
        commands_to_remove = []


if __name__ == "__main__":
    from Commands.Command_Change_Color.Command_Change_Color import Command_Change_Color
    from Tropas.FakeTropa import FakeTropa
    from Comunicaciones.FakeCommunication import FakeCommunication
    from Utils.Frame import Frame
    from Utils.Resolution import Resolution
    from Color.Color import Color
    from threading import Thread
    from time import sleep

    prueba = CommandManager()
    frame = Frame(Resolution(600,600))
    tropa = FakeTropa(0,FakeCommunication(),Color((255,0,0)),frame.frame,frame.frame,None)
    thread_main = Thread(target=prueba.Run, args=()).start()

    for i in range(20):
        prueba.Add_Command(Command_Change_Color(tropa,Color((1,0,0))))
    sleep(3)
    prueba.Stop()