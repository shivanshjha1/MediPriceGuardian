
# ==========================================
# MediPrice Guardian
# File: models.py
# Purpose: Define the main data models
# ==========================================


# 1. CONSUMABLE CLASS

class Consumable:

    def __init__(self, name, market_price):
        self.name = name
        self.market_price = market_price

    def display_details(self):
        print("Consumable Name:", self.name)
        print("Market Price: Rs.", self.market_price)


# 2. PROCEDURE CLASS

class Procedure:

    def __init__(self, code, name, surgeon_fee, consumables):
        self.code = code
        self.name = name
        self.surgeon_fee = surgeon_fee
        self.consumables = consumables

    def display_details(self):
        print("Procedure Code:", self.code)
        print("Procedure Name:", self.name)
        print("Surgeon Fee: Rs.", self.surgeon_fee)

        print("Associated Consumables:")

        for item in self.consumables:
            item.display_details()


# 3. HOSPITAL CLASS

class Hospital:

    def __init__(self, name, pricing, accepted_schemes):
        self.name = name
        self.pricing = pricing
        self.accepted_schemes = accepted_schemes

    def display_details(self):
        print("Hospital Name:", self.name)
        print("Hospital Pricing:", self.pricing)
        print("Accepted Schemes:", self.accepted_schemes)


# 4. GOVERNMENT SCHEME CLASS

class GovernmentScheme:

    def __init__(self, code, name, coverage_amount,
                 description, eligibility):

        self.code = code
        self.name = name
        self.coverage_amount = coverage_amount
        self.description = description
        self.eligibility = eligibility

    def display_details(self):
        print("Scheme Code:", self.code)
        print("Scheme Name:", self.name)
        print("Coverage Amount: Rs.", self.coverage_amount)
        print("Description:", self.description)
        print("Eligibility:", self.eligibility)


# ==========================================
# END OF MODELS
# ==========================================
