class DMART:

    discountOnEachProduct = 0.10

    def __init__(self):
        self.gstn = None
        self.location = None

    def calculatePrice(self, prodName, originalPriceOfProduct):
        actualPrice = originalPriceOfProduct - (originalPriceOfProduct * DMART.discountOnEachProduct)
        print("Actual Price of", prodName, "after Discount", actualPrice)

    @classmethod
    def revisedDiscount(cls, newDiscount):
        # print(cls)
        cls.discountOnEachProduct = newDiscount

print("*****PRICE WITH DEFAULT DISCOUNT*****")
d1 = DMART()
d1.gstn = 1234567
d1.location = "BTM"
d1.calculatePrice("Cooker", 5000)


d2 = DMART()
d2.gstn = 3343567
d2.location = "Indore"
d2.calculatePrice("AirFryer",8000)

DMART.revisedDiscount(0.20)

print("*****PRICE WITH REVISED DISCOUNT DUE TO FESTIVAL*****")
d1.calculatePrice("Cooker", 5000)
d2.calculatePrice("AirFryer", 8000)