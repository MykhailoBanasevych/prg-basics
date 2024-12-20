class Phone:
    def __init__(self):
        self.power_state = "off" 
        self.volume_level = "medium"  
        self.battery_state = "uncharged" 
    def turn_on(self):
        self.power_state = "on"
        print("Phone is now ON.")
    
    def turn_off(self):
        self.power_state = "off"
        print("Phone is now OFF.")
    
    def increase_volume(self):
        if self.volume_level == "low":
            self.volume_level = "medium"
        elif self.volume_level == "medium":
            self.volume_level = "high"
        print(f"Volume increased to {self.volume_level}.")
    
    def decrease_volume(self):
        if self.volume_level == "high":
            self.volume_level = "medium"
        elif self.volume_level == "medium":
            self.volume_level = "low"
        print(f"Volume decreased to {self.volume_level}.")
    
    def start_charging(self):
        self.battery_state = "charging"
        print("Phone is now charging.")
    
    def stop_charging(self):
        self.battery_state = "charged"
        print("Phone is fully charged.")
    
    def uncharge(self):
        self.battery_state = "uncharged"
        print("Phone is uncharged.")


    def display_status(self):
        print(f"Phone is {self.power_state}.")
        print(f"Volume is {self.volume_level}.")
        print(f"Battery status: {self.battery_state}.")

my_phone = Phone()

my_phone.turn_on()

my_phone.increase_volume()

my_phone.start_charging()

my_phone.display_status()

my_phone.stop_charging()

my_phone.display_status()

my_phone.turn_off()
