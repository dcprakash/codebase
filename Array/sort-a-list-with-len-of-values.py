

def sfunc(e):
    return len(e)


cars = ['Ford', 'BMWBMW', 'Volvo']
# cars.sort(key=sfunc)


cars.sort(key=lambda x: len(x))
print(cars)



