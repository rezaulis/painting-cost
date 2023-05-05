def paint():
    gallon = (w//115)+ 1
    return gallon
def hlabor():
    hour = gallon * 8
    return hour
def paintcost():
    paintC = p * gallon
    return paintC
def laborcost():
    lcost = hour * 20
    return lcost
def totalcost():
    tcost = paintC + lcost
    return tcost

w = float(input("Enter wall space in space feet: "))
p = float(input("Enter paint price per gallon: "))

gallon = paint()
hour = hlabor()
paintC = paintcost()
lcost = laborcost()
tcost = totalcost()

print("Gallons of paint: ", gallon)
print("Hours of labor: ", hour)
print("Paint charges: ", paintC)
print("Labor charges: ", lcost)
print("Total cost: ", tcost)

    
