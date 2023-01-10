```mermaid
classDiagram
   %% -- Arucos
    IAruco <|-- Aruco
    Aruco <|-- Aruco_Drawable
    Runnable <|-- Aruco_Drawable
    Aruco_Drawable *-- IVideoSource 
    Aruco_Drawable *-- CV2ImShow_Drawable 

   
    ICommandManager <|-- CommandManager
    Runnable <|-- CommandManager
 
    ICommandManager *-- ICommand
    
   
    ICommand <|-- Command_Change_Color
    ICommand <|-- ICommand_Go_To_Position
   
    ICommand_Go_To_Position *-- IPosition
    
  
    ICommunication <|-- FakeCommunication
    ICommunication <|-- UDP_Client

   
    %% -- Positions
    IPosition <|-- Position_2D
    
    
    ITropa <|-- Tropa
    ITropa <|-- FakeTropa
    ITropa *-- ICommunication
    ITropa *-- IPosition
    ITropa *-- Color
    
    
    IVideoPlayback <|-- CV2ImShow
    Runnable <|-- CV2ImShow
    CV2ImShow <|-- CV2ImShow_Drawable
    IVideoPlayback  *-- IVideoSource
    
   
    IVideoSource <|-- FakeVideo
    IVideoSource <|-- WebCam
    
  
```