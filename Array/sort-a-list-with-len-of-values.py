

def sfunc(e):
    return len(e)


cars = ['Ford', 'BMW', 'Volvo']
cars.sort(key=sfunc)
print(cars)