class DonationSystem:
    def __init__(self):
        self.total = 0
        self.error = None

    def donate(self, amount):
        if amount <= 0:
            self.error = "Invalid donation amount"
            return False

        self.total += amount
        self.error = None
        return True

    def get_total(self):
        return self.total

    def get_error(self):
        return self.error
