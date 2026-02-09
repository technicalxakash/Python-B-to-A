#oops
class Mobile:
        def __init__(self,brand,price):
                self.brand=brand
                self.price=price
        def working(self):
                print(f"{self.brand}mobile is working of price {self.price}")    

mo=Mobile("sumsung",10000000)         
mo.working()
