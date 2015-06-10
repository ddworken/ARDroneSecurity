#A folder to hold configuration details for hostapd on the Raspberry Pi. 

Required Software: ```hostapd udhcpd```

##wlan0

wlan0 hosts the unsecured hotspot and all traffic on wlan0 is redirected to localhost where the authentication webpage is hosted. 

##wlan1

wlan1 hosts the secure hotspot. The ar drone connects to wlan1 and the password for wlan1 is given out by the webapge on wlan0. 
