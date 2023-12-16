try:
    from tkinter import *
except ImportError:
    from Tkinter import *  # For Python 2.x

class WifiConfig:
    def __init__(self, master):
        self.master = master
        self.master.title("Configuration Wi-Fi")

        self.label_wifi = Label(self.master, text="Wi-Fi:")
        self.label_wifi.pack()

        self.entry_wifi = Entry(self.master)
        self.entry_wifi.pack()

        self.label_language = Label(self.master, text="Language:")
        self.label_language.pack()

        self.entry_language = Entry(self.master)
        self.entry_language.pack()

        self.button_rpi = Button(self.master, text="Configure RPi", command=self.configure_rpi)
        self.button_rpi.pack()

        self.button_esp32 = Button(self.master, text="Configure ESP32", command=self.configure_esp32)
        self.button_esp32.pack()

    def configure_rpi(self):
        wifi = self.entry_wifi.get()
        language = self.entry_language.get()
        # Code spécifique à la configuration Raspberry Pi
        print("Configuration Raspberry Pi - Wi-Fi:", wifi, "Language:", language)

    def configure_esp32(self):
        wifi = self.entry_wifi.get()
        language = self.entry_language.get()
        # Code spécifique à la configuration ESP32
        print("Configuration ESP32 - Wi-Fi:", wifi, "Language:", language)

def run_gui():
    root = Tk()
    app = WifiConfig(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
