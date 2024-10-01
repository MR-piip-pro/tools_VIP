#!/bin/bash

# تثبيت الحزم المطلوبة باستخدام APT
echo "Installing required packages..."
sudo apt update
sudo apt install -y python3-pip xterm python3-tk

echo "Installing required Python libraries..."
pip3 install pyautogui rich pyperclip

echo "Completion of the download process. "
