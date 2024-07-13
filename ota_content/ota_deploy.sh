#!/bin/bash

echo -ne "Installing... \n"

sudo apt update
sudo apt install python3-pip
sudo pip3 install -U jetson-stats


sudo cp startup_display_kanga.py /usr/local/bin/
sudo chmod +x /usr/local/bin/startup_display_kanga.py
# Make sure that this directory exists
sudo mkdir -p /usr/local/share/startup_script/images
sudo cp ./JHKanga.jpg /usr/local/share/startup_script/images/JHKanga.jpg

sudo mkdir /etc/systemd/user
sudo cp JHKanga.service /etc/systemd/user/
sudo systemctl daemon-reload
sudo systemctl enable --global JHKanga.service

