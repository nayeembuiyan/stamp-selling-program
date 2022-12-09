import csv

country = {}
with open('Countries and Zones.csv', 'r') as data:
    for line in csv.reader(data):
        country[line[0]] = line[1]  # Matching country to the corresponding zone no

letter_price = {}
with open('../../Desktop/Assessment 1/Economy letter Price Guide.csv', 'r') as data:
    for line in csv.reader(data):
        letter_price[line[0]] = line[1:]  # Retrieving letter prices for the various weights

parcel_price = {}
with open('Economy parcel Price Guide.csv', 'r') as data:
    for line in csv.reader(data):
        parcel_price[line[0]] = line[1:]  # Retrieving parcel prices for the various weights


def amend(order):
    select_item = int(input("Enter item ID: "))

    if select_item in order:
        typ = order[select_item][1]
        size = order[select_item][3]
        qty = order[select_item][4]
        con = order[select_item][5]
        zone = country[con]
        zone = zone.split()[1]
        zone = int(zone)

        weight = float(input("Enter new weight: "))

        if typ.lower() == 'letter':
            if weight <= 0.5:
                zone_value = letter_price['Up to 500g'][zone - 1]
            elif weight <= 1.0:
                zone_value = letter_price['Up to 1kg'][zone - 1]
            elif weight <= 1.5:
                zone_value = letter_price['Up to 1.5kg'][zone - 1]
            elif weight <= 2.0:
                zone_value = letter_price['Up to 2kg'][zone - 1]
            else:
                print("Weight up to 2kg only")
        elif typ.lower() == 'parcel':
            if 2.5 < weight <= 3.5:
                zone_value = parcel_price['Over 2.5 kg up to 3kg'][zone - 1]
            elif weight <= 5.0:
                zone_value = parcel_price['Up to 5kg'][zone - 1]
            elif weight <= 10.0:
                zone_value = parcel_price['Up to 10kg'][zone - 1]
            elif weight <= 15.0:
                zone_value = parcel_price['Up to 15kg'][zone - 1]
            elif weight <= 20.0:
                zone_value = parcel_price['Up to 20kg'][zone - 1]
            else:
                print("Weight up to 20 kg only")
        else:
            print("Invalid weight")

        cost = float(zone_value) * qty  # Calculating the cost
        if size == 'small':
            cost = float(cost)
        elif size == 'medium':
            cost += (cost * 10/100)
        elif size == 'large':
            cost += (cost * 15/100)
        else:
            print("Invalid size")

        # Adding items in order
        order[select_item] = [cost, typ, weight, size, qty, con, zone_value]
        print("Item/s updated")
    else:
        print("Item not found")

    return order