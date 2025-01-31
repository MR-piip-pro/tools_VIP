#!/bin/bash

# تثبيت الحزم المطلوبة باستخدام APT
echo "Installing required packages..."
sudo apt update
sudo apt install -y python3-pip xterm python3-tk python3-venv

# إنشاء بيئة افتراضية
echo "Creating virtual environment..."
python3 -m venv myenv

# تفعيل البيئة الافتراضية
echo "Activating virtual environment..."
source myenv/bin/activate

# تثبيت المكتبات المطلوبة في البيئة الافتراضية
echo "Installing required Python libraries..."
pip install pyautogui rich pyperclip

echo "Completion of the download process."

