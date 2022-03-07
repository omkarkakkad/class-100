class Car(object):
    def __init__(self, model, color, company, speed_limit):
        self.model = model
        self.color = color
        self.company = company
        self.speed_limit = speed_limit

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelerate(self):
        print("acclerating")  

    def changeGear(self, gear_type):
        print("gear changed")

o1 = Car("B6", "white", "bmw", 220)
o2 = Car("A6", "black", "audi", 300)
print(o1.start())
print(o1.color)
print(o1.speed_limit)

print(o2.color)
# print(o1.stop())
# print(o1.accelerate())
# print(o1.changeGear())