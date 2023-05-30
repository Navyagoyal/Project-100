class Atm(object):
    def __init__(self,card_no,pin_no):
        self.card_no = card_no
        self.pin_no = pin_no
    
    def cashWithdrawal(self):
        print("Cash Withdrawn")
    
    def balanceEnquiry(self):
        print("Enquired about balance")
    
bank = Atm(12345,21345)
bank.cashWithdrawal()