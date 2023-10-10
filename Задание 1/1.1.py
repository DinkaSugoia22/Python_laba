class Car:
    def __init__(self, color, fuel, probeg, speed):
        self.color = color
        self.fuel = fuel
        self.probeg = probeg
        self.speed = speed

    def go(self):
        print("Автомобиль поехал со скоростью", self.speed, "км/ч")

    def turn(self):
        print("Автомобиль повернул")

    def stop(self):
        self.speed = 0
        print("Автомобиль остановился")
    
    def show(self):
        print("Цвет автомобиля:", self.color)
        print("Количество топлива:", self.fuel)
        print("Пробег:", self.probeg)
        print("Скорость:", self.speed)


myCar = Car("Black", "50%", 130.000, 90)

myCar.show()
myCar.go()
myCar.turn()
myCar.stop()