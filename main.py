from car import Car
from electrical_car import ElectricalCar
from battery import Battery
from gasoline_car import GasolineCar
from hybrid import HybridCar
car1 = Car('xe1', 'red', 2017)
battery1 = Battery('ab900', 2019, 10)
electrical_car1 = ElectricalCar ('Tesla', 'green', 2018, 200, battery1)
gasoline_car1 = GasolineCar ('audi', 'blue', 2017, 150, battery1)
hybrid_car1 = HybridCar ('Tesla', 'green', 2018, 'audi', 'blue', 2017, 200, 150, battery1)
print(car1.gioi_thieu_ban_than())
print(electrical_car1.gioi_thieu_ban_than())
print(gasoline_car1.gioi_thieu_ban_than())
print (hybrid_car1.gioi_thieu_ban_than())

class Car:
    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year
        print ('Khoi tao tai Car')
    def gioi_thieu_ban_than (self):
        return ' name = {}, color = {}, year = {}, '.\
        format(self.name, self.color, self.year)
       
from car import Car
from battery import Battery
class ElectricalCar(Car):
    def __init__(self, name, color, year, charging_voltage, battery):
        super().__init__(name, color, year)
        self.charging_voltage = charging_voltage
        self.battery = battery
        print ('Khoi tao tai ElectricalCar')
    def gioi_thieu_ban_than (self):
            return Car.gioi_thieu_ban_than(self)+\
            'charging_voltage = '+str(self.charging_voltage)+','+\
            self.battery.gioi_thieu_ban_than()
            
from car import Car
from battery import Battery
class GasolineCar(Car):
    def __init__(self, name, color, year, volume, battery):
        super().__init__(name, color, year)
        self.volume = volume
        self.battery = battery
        print ('Khoi tao tai GasolineCar')
    def gioi_thieu_ban_than (self): 
        return Car.gioi_thieu_ban_than(self)+\
        'volume = '+str(self.volume)+','+\
        self.battery.gioi_thieu_ban_than()
        
from electrical_car import ElectricalCar
from gasoline_car import GasolineCar
from car import Car
from battery import Battery
class HybridCar(ElectricalCar, GasolineCar):
    def __init__(self, name, color, year, charging_voltage, volume, battery):
        super.__init__(self, name, color, year)
        self.charging_voltage = charging_voltage
        self.volume = volume
        self.battery = battery
        print ('Khoi tao Hybrid')
    def gioi_thieu_ban_than (self):
            return Car.gioi_thieu_ban_than(self)+\
            'volume = '+str(self.volume)+',' +\
             'charging_voltage = '+','+\
            str(self.charging_voltage) +\
            self.battery.gioi_thieu_ban_than() 
