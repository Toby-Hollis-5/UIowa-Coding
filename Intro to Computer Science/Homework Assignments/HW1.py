import math
import test

def hotel(hoursRequired, daysRequired, hotelCostPerNight):
    if (hoursRequired / 8) == daysRequired:
        hotelNights = daysRequired - 1
        #print("No hotel last night")
    else:
        hotelNights = daysRequired
        #print("Hotel every night")
    hotelCost = hotelNights * hotelCostPerNight
    return hotelCost, hotelNights

def breakfast(hoursRequired, daysRequired, breakfastCostPerDay):
    #If exactly 8 hours in trip, there shouldn't be a breakfast.
    if (hoursRequired / 8) <= 1:
        breakfastDays = 0
        #print("No breakfast")
    else:
        breakfastDays = int(hoursRequired / 8)
        #print(breakfastDays, "breakfast")
    breakfastCostTotal = breakfastDays * breakfastCostPerDay
    return breakfastCostTotal

def lunch(hoursRequired, daysRequired, lunchCostPerDay):
    if (hoursRequired % 8) > 4:
        extraLunch = 1
        #print("extraLunch")
    else:
        extraLunch = 0
        #print("noExtraLunch")
    lunchDays = (daysRequired + extraLunch)
    lunchCostTotal = lunchDays * lunchCostPerDay
    return lunchCostTotal, lunchDays

def dinner(hoursRequired, daysRequired, dinnerCostPerDay):
    #No dinner on last day
    if (hoursRequired / 8) <= 1:
        dinnerDays = 0
    else:
        dinnerDays = daysRequired
    dinnerCostTotal = dinnerDays * dinnerCostPerDay
    return dinnerCostTotal

def tripCostInfo(distanceKM, vehSpeedMPS, vehKPL, gasCostPerLiter,
                 hotelCostPerNight, breakfastCostPerDay, lunchCostPerDay,
                 dinnerCostPerDay):

    vehSpeedKPH = vehSpeedMPS * 3.6
    hoursRequired = distanceKM / vehSpeedKPH
    daysRequired = int(hoursRequired / 8)
    hoursExtra = hoursRequired % 8

    gas = distanceKM / vehKPL
    gasCost = gasCostPerLiter * gas

    hotelCost, hotelNights = hotel(hoursRequired, daysRequired, hotelCostPerNight)
    
    breakfastCostTotal = breakfast(hoursRequired, daysRequired, breakfastCostPerDay)
    lunchCostTotal, lunchDays = lunch(hoursRequired, daysRequired, lunchCostPerDay)
    dinnerCostTotal = dinner(hoursRequired, daysRequired, dinnerCostPerDay)

    foodCostTotal = breakfastCostTotal + lunchCostTotal + dinnerCostTotal
    totalCost = hotelCost + foodCostTotal + gasCost

    #print(gasCost, vehSpeedKPH)
    #print(hoursRequired, daysRequired, hoursExtra)
    #print(breakfastCostTotal, lunchCostTotal, dinnerCostTotal)
    #print(hotelCost)

    #print(totalCost, gasCost, hotelNights, lunchDays, foodCostTotal)

    return totalCost, gasCost, hotelNights, lunchDays, foodCostTotal

def bestVehicleForTrip(distanceM, veh1Name, veh1SpeedMPH, veh1MPG, veh2Name,
                       veh2SpeedMPH, veh2MPG, gasCostPerGallon,
                       hotelCostPerNight, breakfastCostPerDay, lunchCostPerDay,
                       dinnerCostPerDay):
    distanceKM = distanceM * 1.609344
    veh1SpeedMPS = veh1SpeedMPH * 0.44704
    veh2SpeedMPS = veh2SpeedMPH * 0.44704
    veh1KPL = veh1MPG * 0.425144
    veh2KPL = veh2MPG * 0.425144
    gasCostPerLiter = gasCostPerGallon / 3.78541

    veh1totalCost, veh1gasCost, veh1hotelNights, veh1lunchDays, veh1foodCostTotal = tripCostInfo(distanceKM,
                 veh1SpeedMPS, veh1KPL, gasCostPerLiter,
                 hotelCostPerNight, breakfastCostPerDay, lunchCostPerDay,
                 dinnerCostPerDay)
    veh1hotelCost = veh1hotelNights * hotelCostPerNight
    
    print("{:.1f} miles in vehicle '{}' will cost ${:.2f}, including: ${:.2f} for {} hotel nights, ${:.2f} for gas, and ${:.2f} for food (including {} lunches)".format(distanceM, veh1Name, veh1totalCost, veh1hotelCost, veh1hotelNights, veh1gasCost, veh1foodCostTotal, veh1lunchDays))
    
    veh2totalCost, veh2gasCost, veh2hotelNights, veh2lunchDays, veh2foodCostTotal = tripCostInfo(distanceKM,
                 veh2SpeedMPS, veh2KPL, gasCostPerLiter,
                 hotelCostPerNight, breakfastCostPerDay, lunchCostPerDay,
                 dinnerCostPerDay)
    veh2hotelCost = veh2hotelNights * hotelCostPerNight
    print("{:.1f} miles in vehicle '{}' will cost ${:.2f}, including: ${:.2f} for {} hotel nights, ${:.2f} for gas, and ${:.2f} for food (including {} lunches)".format(distanceM, veh2Name, veh2totalCost, veh2hotelCost, veh2hotelNights, veh2gasCost, veh2foodCostTotal, veh2lunchDays))

    if veh1gasCost < veh2gasCost:
        print("To save money, use '{}'".format(veh1Name))
    else:
        print("To save money, use '{}'".format(veh2Name))


def testQ1():
    
    #One hour
    totalCost, gasCost, hotelNights, lunchDays, foodCostTotal = tripCostInfo(36, 10, 5, 1.57, 180, 13, 18, 6)
    print(totalCost, gasCost, hotelNights, lunchDays, foodCostTotal)
    print("One hour test done")
    #Four hours
    totalCost, gasCost, hotelNights, lunchDays, foodCostTotal = tripCostInfo(144, 10, 5, 1.57, 180, 13, 18, 6)
    print(totalCost, gasCost, hotelNights, lunchDays, foodCostTotal)
    print("Four hour test done")
    #4.5 hour
    totalCost, gasCost, hotelNights, lunchDays, foodCostTotal = tripCostInfo(162, 10, 5, 1.57, 180, 13, 18, 6)
    print(totalCost, gasCost, hotelNights, lunchDays, foodCostTotal)
    print("Four and a half hour test done")
    #Exactly one day
    totalCost, gasCost, hotelNights, lunchDays, foodCostTotal = tripCostInfo(288, 10, 5, 1.57, 180, 13, 18, 6)
    print(totalCost, gasCost, hotelNights, lunchDays, foodCostTotal)
    print("One day test done")
    #Exactly two days
    totalCost, gasCost, hotelNights, lunchDays, foodCostTotal = tripCostInfo(576, 10, 5, 1.57, 180, 13, 18, 6)
    print(totalCost, gasCost, hotelNights, lunchDays, foodCostTotal)
    print("Two day test done")
    #Two and a half+ days
    totalCost, gasCost, hotelNights, lunchDays, foodCostTotal = tripCostInfo(1000, 13, 5, 1.57, 180, 13, 18, 6)
    print(totalCost, gasCost, hotelNights, lunchDays, foodCostTotal)
    print("Two day+ test done")

    return
    
def testQ2():

    bestVehicleForTrip(1000.0, "Bugatti", 100.0, 1.0, "Vespa", 27.0, 100.0, 2.10, 6.50, 11.0, 23.0, 55.0)
    print("Test 1: given done")
    bestVehicleForTrip(500.0, "Tesla", 25.0, 5.0, "Bug", 75.0, 75.0, 4.20, 2.40, 100.0, 5.0, 33.0)
    print("Test 2 done")
    bestVehicleForTrip(100.0, "BMW", 100.0, 25.0, "Ferrari", 100.0, 50.0, 4.20, 2.40, 100.0, 5.0, 33.0)
    print("Test 3: different mpg done")
    bestVehicleForTrip(10000.0, "Ford escape", 10.0, 25.0, "Chrysler", 80.0, 50.0, 4.20, 2.40, 100.0, 5.0, 33.0)
    print("Test 4: super long trip done")
    bestVehicleForTrip(1000.0, "Slow Limo", 30.0, 1.0, "Fast Limo", 60.0, 1.0, 4.20, 2.40, 100.0, 5.0, 33.0)
    print("Test 5: different mph done")
    
    #car names = ferrari, escape, BMW, Tesla, Bug, 
    return
