#General Idea
Mount a raspberry pi on the ar drone. The ar drone will connect to the raspberry pi's networkA which will be secured with WPA2. 
The raspberry pi will then broadcast a second network-networkB (with no encryption) that will host a web server. On the web server the 
user will be asked to authenticate. There will be two types of authentication (for v1):

1. Full authentication. 

  a. The user will be given the key to access networkA. Once connected to networkA, the user will have full access to the drone. 

2. Camera/data authentication.
  
  a. Using node-ar-drone, the following information will be made available on the web interface:
    
    1. Images and Videos
    
      a. Users can download videos and images from the ar drone
      
    2. Sensors/Events
    
      a. Users can view: ```landed, hovering, flying, landing, batteryChange, and altitudeChange events```

#Hardware

1. Raspberry Pi with two WiFi cards

2. Ar Drone

#Software

1. On the raspberry pi, the following software will be needed: 

  a. Create WPA2 hotspot
  
  b. Create WiFi hotspot without any authentication
  
  c. Simple python/flask webserver that interfaces with a node.js backend. 
  
    1. [Running node.js from Python](http://sweetme.at/2014/02/17/a-simple-approach-to-execute-a-node.js-script-from-python/)
    
      a. If we simply exposed a node-ar-drone interface to the user they could use it to control the drone when authenticated for only camera/data. 
      
    2. python/flask program will need to be able to authenticate users and return different pages depending on authentication status. 

2. On the AR drone, the following software will be needed:

  a. [Connect AR Drone to a WPA2 network (instead of having the AR drone broadcast it's own network)](https://github.com/daraosn/ardrone-wpa2)

    1. Write your own additional script to assist with the above code to make the AR-Drone automatically connect to a hard coded hotspot at bootup. 
    
#Execution Plan

| Step  |  Difficulty |
|---|---|
| Set up raspberry pi to host two hotspots at once (using hostapd)            | Easy |
| Write a python script to authenticate users and direct to different logic depending on authentication level  | Medium  |
| Allow python script to give authenticated users WPA2 credentials  | Easy  |
| Interface Camera/Data users with node.js backend to supply them with data  | Hard |
| Set up AR drone to connect to hard coded WPA2 network  | Medium  |
| Set up AR drone to automatically do the above  | Easy  |
| Make the above web interface look nice (use bootstrap for responsive design etc) | Medium |

#Possible Improvements

1. IRC channel hosted on the drone

2. Crowd control mode

  a. a la Twitch Plays Pokemon, allow users to vote on who get's control/what is executed.
  
3. Buy drone time
  
  a. Allow people to buy drone time (e.g. 1 dollar a minute) and after their time runs out the drone automatically deletes their
  credentials and lands. 
  
3. Stream video from the drone to the internet (live!)
