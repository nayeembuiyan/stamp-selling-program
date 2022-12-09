def remove(order):
    rmv_id = int(input("Enter item ID to be removed: "))
    option = input("To confirm press Y else N: ")

    if option.lower() == 'n':
        order = order
    elif option.lower() == 'y':
        order.pop(rmv_id)  # Removing an item from the order
        print("Item removed")
    else:
        print("Invalid option")

    return order