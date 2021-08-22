class Atm(object):
    def __init__(self, atm_number, atm_pin):
        self.atm_number = atm_number
        self.atm_pin = atm_pin

    def CashWithdrawl():
        print("Cash Withdrawl successfully for the atm number")

    def BalanceEnquiry():
        print("Cash Withdrawl successfully")


User = Atm(12345, 1122)
print(User.atm_number)
