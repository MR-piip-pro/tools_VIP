#!/bin/bash

# رسالة ترحيبية
echo "Starting installation process..."

# تحديث الحزم وتثبيت الحزم الأساسية
echo "Updating package list and installing required system packages..."
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip xterm python3-tk python3-venv

# التحقق من نجاح تثبيت الحزم
if [ $? -ne 0 ]; then
    echo "Error installing system packages. Exiting..."
    exit 1
fi

# إنشاء بيئة افتراضية
ENV_DIR="myenv"
echo "Creating virtual environment at: $ENV_DIR ..."
python3 -m venv $ENV_DIR

if [ ! -d "$ENV_DIR" ]; then
    echo "Failed to create virtual environment. Exiting..."
    exit 1
fi

# تفعيل البيئة الافتراضية
echo "Activating virtual environment..."
source "$ENV_DIR/bin/activate"

if [ $? -ne 0 ]; then
    echo "Failed to activate the virtual environment. Exiting..."
    exit 1
fi

# تثبيت المكتبات المطلوبة
echo "Installing required Python libraries..."
pip install --upgrade pip
pip install pyautogui rich pyperclip cryptography

# التحقق من نجاح التثبيت
if [ $? -eq 0 ]; then
    echo "All packages installed successfully!"
else
    echo "Package installation failed. Please check your setup."
fi

echo "Download and installation process completed successfully."


