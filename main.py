try:
    from tkinter import *
except ImportError:
    from Tkinter import *  # For Python 2.x

import subprocess

class WifiConfigRPi:
    def __init__(self, master):
        self.master = master
        self.master.title("Configuration Wi-Fi RPi")

        self.label_wifi = Label(self.master, text="Wi-Fi:")
        self.label_wifi.pack()

        self.entry_wifi = Entry(self.master)
        self.entry_wifi.pack()

        self.label_password = Label(self.master, text="Mot de passe:")
        self.label_password.pack()

        self.entry_password = Entry(self.master, show="*")
        self.entry_password.pack()

        self.button_connect = Button(self.master, text="Connecter", command=self.connect_wifi)
        self.button_connect.pack()

    def scan_wifi_networks(self):
        wifi_info = subprocess.run(["sudo", "iwlist", "wlan0", "scan"], capture_output=True, text=True)
        return wifi_info.stdout

    def connect_wifi(self):
        wifi = self.entry_wifi.get()
        password = self.entry_password.get()
        # Code pour se connecter au réseau Wi-Fi spécifié
        print("Connecter à", wifi, "avec le mot de passe", password)
        # À implémenter : utilisation des données pour la connexion Wi-Fi

def run_rpi_gui():
    root = Tk()
    app = WifiConfigRPi(root)
    root.mainloop()

if __name__ == "__main__":
    run_rpi_gui()
