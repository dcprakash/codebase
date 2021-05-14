"""
https://leetcode.com/problems/design-parking-system/

ask questions, clarify assumptions
do i design or algorithm?

spots

size:   small, medium, large and xlarge
    small car can be parked on bus spot but, not vice versa
    
price
disability, premium
levels
entry and exit: concurrency


abstract vehicle
    string licensePlate     # to identify vehicle
    enum color
    
bike, car, truck, bus classes inherit from vehicle class above

class parkingLot(zipcode):
    spot: placeVehicle(vehicle v) 
        # will need to find first avilable spot, in type of spots
        # array or list of spots: we would have to run through list in linear fashion
        # Stack: constant time to place a medium vehicle, we first check if medium stack is available, if not then check large and xlarge stacks
        # put in hashmap to accomodate removeVehicle
    
    spot: removeVehicle(vehicle v)
        # hash map helps with fast lookup
        # get licensePlate as lookup key, if exist then remove from hashmap
    
    
class spot(id, size):


how do efficiently park and retieve car?






"""
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking={
            1: big,
            2: medium,
            3: small
        }
        

    def addCar(self, carType: int) -> bool:
        if self.parking[carType]:
            self.parking[carType]-=1
            return True
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)