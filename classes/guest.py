class Guest:
    
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        
    def check_guest_name(self):
        return self.name

    def check_guest_cash(self):
        return self.cash

    def pay_entry_fee(self, room):
        self.cash -= room.entry_fee