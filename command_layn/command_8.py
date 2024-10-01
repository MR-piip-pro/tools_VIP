import tkinter as Tk
import subprocess
import pyperclip 
from tkinter import *
from tkinter import font
################################################
def command_list_8():
    na = Tk()
    na.title("upgrd os")
    na.geometry('800x400+400+250')
    na.wm_resizable(False, False)
    ################################################
    takid_fat7_anfida1  = False
    takid_fat7_anfida2  = False
    takid_fat7_anfida3  = False
    takid_fat7_anfida4  = False
    takid_fat7_anfida5  = False
    takid_fat7_anfida6  = False
    takid_fat7_anfida7  = False
    takid_fat7_anfida8  = False
    #############################################
    color1 = "#005f87"
    color2 = "#00afaf"
    #############################################
    ispas10 = "          "
    ispas20 = "                    "
    ispas30 = "                              "
    ispas40 = "                                        "
    ###############  variyabl  #################
    sayz1 = font.Font(family="system", size=10)
    ###############
    sayz2 = font.Font(family="system", size=25)
    #############################################
    na.config(bg=color1)
    ############################################################################################################   (1)
    def update_and_upgrade():
        global takid_fat7_anfida1
        if not takid_fat7_anfida1:
            takid_fat7_anfida1 = True
            #############################################
            new_window = Toplevel(na)
            new_window.title("UPDATE AND UPGRADE")
            new_window.geometry('370x400+30+200')
            new_window.wm_resizable(False, False)
            #############################################
            new_window.protocol("WM_DELETE_WINDOW", lambda: on_close_update(new_window))
            #############################################
            def comands1():
                lamr = "sudo apt update && sudo apt upgrade -y"
                subprocess.Popen(["xterm", "-e", f"bash -c '{lamr} && sleep 6 && exit'"])
                #########################################
            new_window.config(bg=color1)
            #############################################
            L = Label(new_window, text="""
            The command 
            `sudo apt update && sudo apt upgrade -y` 
            in Kali Linux updates \nthe package list and then upgrades all  
            installed packages to the latest versions,
            with the `-y` flag automatically 
            confirming the upgrades. 
            This keeps your system up-to-date and secure.""", bg=color2, relief="raised", bd=1)
            L.pack(pady=5)
            #############################################
            button = Button(new_window, text=f"{ispas10} Go ahead {ispas10}", command=comands1, bg=color2, font=sayz1, relief="raised", bd=3)
            button.place(x=95, y=320)
            #############################################
    def on_close_update(window):
        global takid_fat7_anfida1
        takid_fat7_anfida1 = False
        window.destroy()
    ############################################################################################################   (2)
    def install_tor():
        global takid_fat7_anfida2
        if not takid_fat7_anfida2:
            takid_fat7_anfida2 = True
            #############################################
            tor = Toplevel(na)
            tor.title("install tor")
            tor.geometry('370x400+30+230')   
            tor.wm_resizable(False, False)
            #############################################
            tor.protocol("WM_DELETE_WINDOW", lambda: on_close_install_tor(tor))
            #############################################
            def comand2():
                lamr = "sudo apt install tor -y"
                subprocess.Popen(["xterm", "-e", f"bash -c '{lamr} && sleep 6 && exit'"])
            #############################################
            tor.config(bg=color1)
            #############################################
            L = Label(tor, text="""The command 
            'sudo apt install tor -y' 
            in Kali Linux installs  
            the Tor server which allows anonymous 
            and secure web browsing. 
            The '-y' flag automatically 
            confirms the installation.""", bg=color2, relief="raised", bd=1)
            L.pack(pady=5)
            #############################################
            button = Button(tor, text=f"{ispas10} GO AHEAD {ispas10}", command=comand2, bg=color2, font=sayz1, relief="raised", bd=3)
            button.place(x=95, y=320)
            #############################################
    def on_close_install_tor(window):
        global takid_fat7_anfida2
        takid_fat7_anfida2 = False
        window.destroy()
    ############################################################################################################   (3)
    def install_proxychains():
        global takid_fat7_anfida3
        if not takid_fat7_anfida3:
            takid_fat7_anfida3 = True
            #############################################
            proxychains = Toplevel(na)
            proxychains.title("install proxychains")
            proxychains.geometry('370x400+30+260')   
            proxychains.wm_resizable(False, False)
            #############################################
            proxychains.protocol("WM_DELETE_WINDOW", lambda: on_close_install_proxychains(proxychains))
            #############################################
            def comand3():
                lamr = "sudo apt install proxychains -y"
                subprocess.Popen(["xterm", "-e", f"bash -c '{lamr} && sleep 6 && exit'"])
            #############################################
            proxychains.config(bg=color1)
            #############################################
            L = Label(proxychains, text="""The command 
            `sudo apt install proxychains -y` 
            in Kali Linux installs ProxyChains, 
            a tool that forces network connections 
            through a series of proxies. 
            The `-y` flag automatically 
            confirms the installation.""", bg=color2, relief="raised", bd=1)
            L.pack(pady=5)
            #############################################
            button = Button(proxychains, text=f"{ispas10} GO AHEAD {ispas10}", command=comand3, bg=color2, font=sayz1, relief="raised", bd=3)
            button.place(x=95, y=320)
            #############################################
    def on_close_install_proxychains(window):
        global takid_fat7_anfida3
        takid_fat7_anfida3 = False
        window.destroy()
    ############################################################################################################   (4)
    def install_code_oss():
        global takid_fat7_anfida4
        if not takid_fat7_anfida4:
            takid_fat7_anfida4 = True
            #############################################
            code_oss = Toplevel(na)
            code_oss.title("install code_oss")
            code_oss.geometry('370x400+30+290')   
            code_oss.wm_resizable(False, False)
            #############################################
            code_oss.protocol("WM_DELETE_WINDOW", lambda: on_close_install_code_oss(code_oss))
            #############################################
            def comand4():
                lamr = "sudo apt install code-oss -y"
                subprocess.Popen(["xterm", "-e", f"bash -c '{lamr} && sleep 6 && exit'"])
            #############################################
            code_oss.config(bg=color1)
            #############################################
            L = Label(code_oss, text="""The command 
            `sudo apt install code-oss` 
            installs "Code - OSS," 
            the open-source version of Visual Studio Code, 
            on Linux distributions that use 
            the `apt` package manager. 
            The `sudo` part grants the necessary 
            permissions to install software on 
            the system.""", bg=color2, relief="raised", bd=1)
            L.pack(pady=5)
            #############################################
            button = Button(code_oss, text=f"{ispas10} GO AHEAD {ispas10}", command=comand4, bg=color2, font=sayz1, relief="raised", bd=3)
            button.place(x=95, y=320)
            #############################################
    def on_close_install_code_oss(window):
        global takid_fat7_anfida4
        takid_fat7_anfida4 = False
        window.destroy()
    ############################################################################################################   (5)
    def install_airgeddon():
        global takid_fat7_anfida5
        if not takid_fat7_anfida5:
            takid_fat7_anfida5 = True
            #############################################
            airgeddon = Toplevel(na)
            airgeddon.title("install airgeddon")
            airgeddon.geometry('370x400+30+320')   
            airgeddon.wm_resizable(False, False)
            #############################################
            airgeddon.protocol("WM_DELETE_WINDOW", lambda: on_close_install_airgeddon(airgeddon))
            #############################################
            def comand5():
                command = [ 
                "sudo apt install git",
                "cd /home/kali/Downloads",
                "git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git"
                ]
                lamr = " && ".join(command)
                subprocess.Popen(["xterm", "-e", f"bash -c '{lamr} && sleep 6 && exit'"])
                    #############################################
            airgeddon.config(bg=color1)
            #############################################
            L = Label(airgeddon, text="""1. **`sudo apt install git`** 
            This command installs Git, \n
            2. **`cd /home/kali/Downloads`** 
            This command changes the current directory \n
            3. **`git clone 
            https://github.com/v1s1t0r1sh3r3/airgeddon.git`**   
            This command downloads 
            the Airgeddon repository from GitHub """, bg=color2, relief="raised", bd=1)
            L.pack(pady=5)
            #############################################
            button = Button(airgeddon, text=f"{ispas10} GO AHEAD {ispas10}", command=comand5, bg=color2, font=sayz1, relief="raised", bd=3)
            button.place(x=95, y=320)
            #############################################
    def on_close_install_airgeddon(window):
        global takid_fat7_anfida5
        takid_fat7_anfida5 = False
        window.destroy()
    ############################################################################################################   (6)
    def basics_install_airgeddon():
        global takid_fat7_anfida6
        if not takid_fat7_anfida6:
            takid_fat7_anfida6 = True
            #############################################
            basics = Toplevel(na)
            basics.title("basics install airgreddon")
            basics.geometry('370x400+30+350')   
            basics.wm_resizable(False, False)
            #############################################
            basics.protocol("WM_DELETE_WINDOW", lambda: on_close_basics_install_airgeddon(basics))
            #############################################
            def comand6():
                lamr = "sudo apt install basics airgeddon -y"
                subprocess.Popen(["xterm", "-e", f"bash -c '{lamr} && sleep 6 && exit'"])
            #############################################
            basics.config(bg=color1)
            #############################################
            L = Label(basics, text="""the commands download Collection 
        from libraries\n
        "bettercap" , "hostapd-wpe" 
        "isc-dhcp-server" , "asleap" 
        "mdk4" , "hcxdumptool" 
        "hcxtools" , "beef-xss" 
        "lighttpd" """, bg=color2, relief="raised", bd=1)
            L.pack(pady=5)
            #############################################
            button = Button(basics, text=f"{ispas10} GO AHEAD {ispas10}", command=comand6, bg=color2, font=sayz1, relief="raised", bd=3)
            button.place(x=95, y=320)
            #############################################
    def on_close_basics_install_airgeddon(window):
        global takid_fat7_anfida6
        takid_fat7_anfida6 = False
        window.destroy()
    ############################################################################################################   (7)
    def install_python3():
        global takid_fat7_anfida7
        if not takid_fat7_anfida7:
            takid_fat7_anfida7 = True
            #############################################
            python3 = Toplevel(na)
            python3.title("install python3")
            python3.geometry('370x400+30+380')   
            python3.wm_resizable(False, False)
            #############################################
            python3.protocol("WM_DELETE_WINDOW", lambda: on_close_install_python3(python3))
            #############################################
            def comand7():
                lamr = "sudo apt install python3"
                subprocess.Popen(["xterm", "-e", f"bash -c '{lamr} && sleep 6 && exit'"])
            #############################################
            python3.config(bg=color1)
            #############################################
            L = Label(python3, text="""The command 
            `sudo apt install python3` 
            installs Python 3 on your Linux system using 
            the `apt` package manager. 
            The `sudo` part provides the necessary 
            administrative permissions to install software. 
            This command ensures you have 
            the latest version of Python 3 
            available in your distribution's 
            repositories.""", bg=color2, relief="raised", bd=1)
            L.pack(pady=5)
            #############################################
            button = Button(python3, text=f"{ispas10} GO AHEAD {ispas10}", command=comand7, bg=color2, font=sayz1, relief="raised", bd=3)
            button.place(x=95, y=320)
            #############################################
    def on_close_install_python3(window):
        global takid_fat7_anfida7
        takid_fat7_anfida7 = False
        window.destroy()
    ############################################################################################################   (8)
    def install_list_passwor():
        global takid_fat7_anfida8
        if not takid_fat7_anfida8:
            takid_fat7_anfida8 = True
            #############################################
            list_passwor = Toplevel(na)
            list_passwor.title("install list_passwor")
            list_passwor.geometry('370x400+30+410')   
            list_passwor.wm_resizable(False, False)
            #############################################
            list_passwor.protocol("WM_DELETE_WINDOW", lambda: on_close_install_list_passwor(list_passwor))
            #############################################
            text1 = "git clone https://github.com/MR-piip-pro/list-password.git" 
            #############################################
            def comand8(text):
                pyperclip.copy(text)
            #############################################
            list_passwor.config(bg=color1)
            #############################################
            L = Label(list_passwor, text="""
            
            
            Lists of passwords 
        About 1.000.000.000 passwords
            
            To download the tool
            
        Copy the link to download from github  
    
      git clone https://github.com/MR-piip-pro  
               /list-password.git   
            
    
            """, bg=color2, relief="raised", bd=5)
            L.place(x=30, y=45)
            #############################################
            button = Button(list_passwor, text=f"{ispas10} COPY THE LINK {ispas10}", command=lambda: comand8(text1), bg=color2, font=sayz1, relief="raised", bd=3)
            button.place(x=70, y=320)
            #############################################
    def on_close_install_list_passwor(window):
        global takid_fat7_anfida8
        takid_fat7_anfida8 = False
        window.destroy()
    ############################################################################################################
    
    ###############  variyabl
    sayz1 = font.Font(family="system", size=10)
    sayz2 = font.Font(family="system", size=25)
    ############################################################
    L = Label(na, text="            Welcome to my application             ", bg=color1, font=sayz2, relief="raised", bd=3)
    L.pack(pady=10)
    
    
    ########################################  41    (1)
    L = Label(na, text=f"{ispas10}1)  To update and upgrade the system. ==>{ispas30}{ispas30}", bg=color2, font=sayz1, relief="raised", bd=3) 
    L.place(x=20, y=80)
    #############
    button = Button(na, text=f"{ispas10}Reading{ispas10}", command=update_and_upgrade, bg=color2, font=sayz1, relief="raised", bd=1)
    button.place(x=630, y=80)
    
    
    ########################################   24   (2) 
    L = Label(na, text=f"{ispas10}2)   To install tor. ==>{ispas30}     {ispas30}{ispas30}", bg=color2, font=sayz1, relief="raised", bd=3) 
    L.place(x=20, y=120)
    #############
    button = Button(na, text=f"{ispas10}Reading{ispas10}", command=install_tor,bg=color2, font=sayz1, relief="raised", bd=1)
    button.place(x=630, y=120)
    
    
    ########################################      (3)
    L = Label(na, text=f"{ispas10}3)  To install proxychains. ==>{ispas20} {ispas30}{ispas30}", bg=color2, font=sayz1, relief="raised", bd=3) 
    L.place(x=20, y=160)
    #############
    button = Button(na, text=f"{ispas10}Reading{ispas10}", command=install_proxychains, bg=color2, font=sayz1, relief="raised", bd=1)
    button.place(x=630, y=160)
    
    
    ########################################      (4)
    L = Label(na, text=f"{ispas10}4)  To install vs_code. ==>{ispas20}       {ispas30}{ispas30}", bg=color2, font=sayz1, relief="raised", bd=3) 
    L.place(x=20, y=200)
    #############
    button = Button(na, text=f"{ispas10}Reading{ispas10}", command=install_code_oss,bg=color2, font=sayz1, relief="raised", bd=1)
    button.place(x=630, y=200)
    
    
    ########################################      (5)
    L = Label(na, text=f"{ispas10}5)  To install airgeddon. ==>{ispas20}    {ispas30}{ispas30}", bg=color2, font=sayz1, relief="raised", bd=3) 
    L.place(x=20, y=240)
    #############
    button = Button(na, text=f"{ispas10}Reading{ispas10}", command=install_airgeddon, bg=color2, font=sayz1, relief="raised", bd=1)
    button.place(x=630, y=240)
    
    
    ########################################      (6)
    L = Label(na, text=f"{ispas10}6)  To install basics airgeddon ==>{ispas10}    {ispas30}{ispas30}", bg=color2, font=sayz1, relief="raised", bd=3) 
    L.place(x=20, y=280)
    #############
    button = Button(na, text=f"{ispas10}Reading{ispas10}", command=basics_install_airgeddon,bg=color2, font=sayz1, relief="raised", bd=1)
    button.place(x=630, y=280)
    
    ########################################      (7)
    L = Label(na, text=f"{ispas10}7)  To install python3. ==>{ispas20}       {ispas30}{ispas30}", bg=color2, font=sayz1, relief="raised", bd=3) 
    L.place(x=20, y=320)
    #############
    button = Button(na, text=f"{ispas10}Reading{ispas10}", command=install_python3,bg=color2, font=sayz1, relief="raised", bd=1)
    button.place(x=630, y=320)
    ########################################      (8)
    L = Label(na, text=f"{ispas10}8)  To install list passsword. ==>{ispas10}       {ispas30}{ispas30}", bg=color2, font=sayz1, relief="raised", bd=3) 
    L.place(x=20, y=360)
    #############
    button = Button(na, text=f"{ispas10}Reading{ispas10}", command=install_list_passwor,bg=color2, font=sayz1, relief="raised", bd=1)
    button.place(x=630, y=360)
    ########################################
    na.mainloop()
