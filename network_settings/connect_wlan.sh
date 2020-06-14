#/bin/bash

#Script pour connecter la rasbery au reseau fablab. 
#Ajouter un SSID WIFI (avec mot de passe)
#wpa_supplicant  ESSID WIFI_PASSWORD | tee /etc/wpa_supplicant/wpa_supplicant.conf

systemctl stop NetworkManager
systemctl disable NetworkManager NetworkManager-wait-online NetworkManager-dispatcher
wpa_supplicant -B -c /etc/wpa_supplicant/wpa_supplicant.conf -i wlan0
dhclient wlan0
