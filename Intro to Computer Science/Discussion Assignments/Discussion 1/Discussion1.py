def costOfTrip(distanceInKilometers, speedInKPH, KmPerLiter, gasCostPerLiter):
    timeRequired = distanceInKilometers / speedInKPH
    gas = distanceInKilometers / KmPerLiter
    gasCost = gasCostPerLiter * gas

    return timeRequired, gasCost

def printTwoTripCosts(distanceInKilometers, veh1Name, veh1SpeedKPH, veh1KmPerLiter, veh2Name, veh2SpeedKPH, veh2KmPerLiter, gasCostPerLiter):
# I wrote this code before I knew what I was doing so I'm just commenting it to show my growth    
#    veh1TimeRequired = distanceInKilometers / veh1SpeedKPH
#    veh1Gas = distanceInKilometers / veh1KmPerLiter
#    veh1GasCost = veh1Gas * gasCostPerLiter

#    veh2TimeRequired = distanceInKilometers / veh2SpeedKPH
#    veh2Gas = distanceInKilometers / veh2KmPerLiter
#    veh2GasCost = veh2Gas * gasCostPerLiter

    time1, cost1 = costOfTrip(distanceInKilometers, veh1SpeedKPH, veh1KmPerLiter, gasCostPerLiter)
    time2, cost2 = costOfTrip(distanceInKilometers, veh2SpeedKPH, veh2KmPerLiter, gasCostPerLiter)
    
# Also messed up on this one
#    print("A trip of {} kilometers in {} takes {:.1f} hours and costs ${:.2f}. A trip of {} kilometers in {} takes {:.1f} hours and costs ${:.2f}.".format(distanceInKilometers, veh1Name, veh1TimeRequired, veh1GasCost, distanceInKilometers, veh2Name, veh2TimeRequired, veh2GasCost))

    print("A trip of {} kilometers in {} takes {:.1f} hours and costs ${:.2f}.".format(distanceInKilometers, veh1Name, time1, cost1) )
    print("A trip of {} kilometers in {} takes {:.1f} hours and costs ${:.2f}.".format(distanceInKilometers, veh2Name, time2, cost2) )

    return

