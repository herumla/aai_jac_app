class Account:
    def __init__(self, name, accountID, owner, annualRevenue, website, headcount, industry, phone, customerSegment):
        self.name = name
        self.accountID = accountID
        self.owner = owner
        self.annualRevenue = annualRevenue
        self.website = website
        self.headcount = headcount
        self.industry = industry
        self.phone = phone
        self.customerSegment = customerSegment

account = None  # Initialize with None

def set_account(name, accountID, owner, annualRevenue, website, headcount, industry, phone, customerSegment):
    global account
    account = Account(name, accountID, owner, annualRevenue, website, headcount, industry, phone, customerSegment)

def get_account():
    return account


