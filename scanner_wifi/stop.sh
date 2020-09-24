#!/bin/bash

airmon-ng stop wlan0mon
systemctl start NetworkManager
