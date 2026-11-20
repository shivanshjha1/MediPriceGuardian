
# models.py
# MediPrice Guardian
# Object-Oriented Data Models


class Consumable:
    def __init__(self, name, market_price):
        self.name = name
        self.market_price = market_price

    def display_details(self):
        print("Consumable Name:", self.name)
        print("Market Price:", self.market_price)


class Procedure:
    def __init__(self, code, name, surgeon_fee, consumables):
        self.code = code
        self.name = name
        self.surgeon_fee = surgeon_fee
        self.consumables = consumables

    def display_details(self):
        print("Procedure Code:", self.code)
        print("Procedure Name:", self.name)
        print("Surgeon Fee:", self.surgeon_fee)
        print("Required Consumables:", self.consumables)


class Hospital:
    def __init__(self, name, pricing, accepted_schemes):
        self.name = name
        self.pricing = pricing
        self.accepted_schemes = accepted_schemes

    def display_details(self):
        print("Hospital Name:", self.name)
        print("Hospital Pricing:", self.pricing)
        print("Accepted Schemes:", self.accepted_schemes)




class GovernmentScheme:
    def __init__(
        self,
        code,
        name,
        description,
        benefits,
        eligibility,
        coverage_amount=None,
        category="Healthcare Programme",
        official_url=""
    ):
        self.code = code
        self.name = name
        self.description = description
        self.benefits = benefits
        self.eligibility = eligibility
        self.coverage_amount = coverage_amount
        self.category = category
        self.official_url = official_url

    def display_details(self):
        print("Scheme Code:", self.code)
        print("Scheme Name:", self.name)
        print("Category:", self.category)
        print("Description:", self.description)
        print("Benefits:", self.benefits)
        print("Eligibility:", self.eligibility)
        print("Coverage Amount:", self.coverage_amount)
        print("Official Website:", self.official_url)