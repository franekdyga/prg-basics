class Phone():
    def __init__(self, charged, powered, muted, beh1, beh2, beh3):
        self.charged = charged
        self.powered = powered
        self.muted = muted
                    

def main():
    # object creation based on the Book class
    phone1 = Phone(True, True, False, 'ringing', 'blinking', 'beeping')
    
if __name__ =="__main__":
    main()
