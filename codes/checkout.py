import datetime
from csv import writer


def checkout(order):
    print(order)
    t = datetime.datetime.now()
    print("-" * 20, "Invoice", "-" * 20)
    count = 1
    subtotal = 0
    for j in order:
        print(f"Item No: {count:{1}}  Item type: {order[j][1]:{10}}  Weight: {order[j][2]:{4}}kg Destination: {order[j][5]:{10}} Unit price: $ {order[j][0]:{6}}")
        subtotal += order[j][0]
        count += 1
    print("\nTotal Cost: ", subtotal)
    print("-" * 18, "End Invoice", "-" * 18)
    print()
    print("-" * 13, "Purchased Stamps", "-" * 13)
    print("letter")
    for j in order:
        if order[j][1] == 'letter':
            print(f"Destination: {order[j][5]: {10}}  Weight: {round(order[j][2], 1): {4}}kg")
    print('-' * 30)
    print("letter")
    for j in order :
        if order[j][1] == 'letter':
            print(f"Destination: {order[j][5]: {10}}  Weight: {round(order[j][2], 1): {4}}kg")
    print('-' * 30)

    z = str(t).split('.')[0]
    x = z.replace(':', '-')

    with open('Invoice.txt', 'a') as file:
        for key, value in order.items():
            file.write('%s:%s\n' % (key, value))

    with open('../../Desktop/Assessment 1/sales_history.csv', 'r') as f:
        data = f.readlines()
        index = data[-1].split(',')[0]  # Taking last sale id from sales_history.csv

    with open('../../Desktop/Assessment 1/sales_history.csv', 'a', newline="") as f_object:  # Adding the sales history to sales_history.csv file
        writer_object = writer(f_object)
        for j in order:
            size = ''
            if order[j][3] == 's':
                size = 'small'
            elif order[j][3] == 'm':
                size = 'medium'
            elif order[j][3] == 'l':
                size = 'large'

            p = [int(index) + 1, t, order[j][1], order[j][4], order[j][5], size, order[j][0]]
            writer_object.writerow(p)  # Writing all the values of sales
        f_object.close()





