def costOfTrip(distanceInKilometers, speedInKPH, KmPerLiter, gasCostPerLiter):
    timeRequired = distanceInKilometers / speedInKPH
    gas = distanceInKilometers / KmPerLiter
    gasCost = gasCostPerLiter * gas

    return timeRequired, gasCost

