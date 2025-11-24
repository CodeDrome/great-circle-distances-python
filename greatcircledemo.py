import greatcircle


def main():

    """
    Creates two lists of dictionaries for start and destination city names and locations.
    Iterates list, setting GreatCircle object attributes,
    then calculating and printing full details.
    """

    print("-------------------------")
    print("| codedrome.com         |")
    print("| Great Circle Distance |")
    print("-------------------------\n")

    starting_cities = [{"name": "London", "latitude1_degrees": 51.507222, "longitude1_degrees": -0.1275},
                       {"name": "London", "latitude1_degrees": 51.507222, "longitude1_degrees": -0.1275},
                       {"name": "London", "latitude1_degrees": 51.507222, "longitude1_degrees": -0.1275},
                       {"name": "London", "latitude1_degrees": 51.507222, "longitude1_degrees": -0.1275},
                       {"name": "London", "latitude1_degrees": 51.507222, "longitude1_degrees": -0.1275},
                       {"name": "London", "latitude1_degrees": 51.507222, "longitude1_degrees": -0.1275},
                       {"name": "London", "latitude1_degrees": 51.507222, "longitude1_degrees": -0.1275}]

    destination_cities = [{"name": "Tokyo", "latitude1_degrees": 35.683333, "longitude1_degrees": 139.683333},
                          {"name": "New York", "latitude1_degrees": 40.7127, "longitude1_degrees": -74.0059},
                          {"name": "New Delhi", "latitude1_degrees": 28.613889, "longitude1_degrees": 77.208889},
                          {"name": "Sydney", "latitude1_degrees": -33.865, "longitude1_degrees": 151.209444},
                          {"name": "Cape Town", "latitude1_degrees": -33.925278, "longitude1_degrees": 18.423889},
                          {"name": "Rio de Janeiro", "latitude1_degrees": -22.908333, "longitude1_degrees": -43.196389},
                          {"name": "Oblivion", "latitude1_degrees": 91, "longitude1_degrees": 360}]

    gc = greatcircle.GreatCircle()

    for i in range(0, len(starting_cities)):

        gc.name1 = starting_cities[i]["name"]
        gc.latitude1_degrees = starting_cities[i]["latitude1_degrees"]
        gc.longitude1_degrees = starting_cities[i]["longitude1_degrees"]

        gc.name2 = destination_cities[i]["name"]
        gc.latitude2_degrees = destination_cities[i]["latitude1_degrees"]
        gc.longitude2_degrees = destination_cities[i]["longitude1_degrees"]

        gc.calculate()

        output(gc)


def output(gc):

    """
    Prints out all details in a neatly annotated format.
    """

    if gc.valid == True:

        print("Name 1: " + gc.name1)
        print("Latitude %f degrees / %f radians" % (gc.latitude1_degrees, gc.latitude1_radians))
        print("Longitude %f degrees /  %f radians" % (gc.longitude1_degrees, gc.longitude1_radians))

        print("Name 2: " + gc.name2)
        print("Latitude %f degrees / %f radians" % (gc.latitude2_degrees, gc.latitude2_radians))
        print("Longitude %f degrees /  %f radians" % (gc.longitude2_degrees, gc.longitude2_radians))

        print("Valid: " + str(gc.valid))
        print("Central angle %f radians / %f degrees" % (gc.central_angle_radians, gc.central_angle_degrees))
        print("Distance %f kilometers / %f miles" % (gc.distance_kilometres, gc.distance_miles))

    else:

        print("Latitude and/or longitude for %s and %s are invalid" % (gc.name1, gc.name2))

    print("")


main()
