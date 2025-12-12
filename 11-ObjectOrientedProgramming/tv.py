class TV:
    def __init__(self):
        self.is_on = False
        self.channel = 1
    def turn_off(self):
        self.is_on = False
    def turn_on(self):
        self.is_on = True
    def set_channel(self, new_channel_no):
        self.channel = new_channel_no
    def show_status(self):
        return (f"TV is on, channel {self.channel}") if self.is_on == True else ("TV is off")