def view(order):
    count = 1
    subtotal = 0
    for j in order:
        print(f"{count:{2}}.  {j:{30}}  {order[j][0]:{10}}")  # Printing item ID and item cost
        subtotal += order[j][0]
        count += 1
    print("\nTotal Cost: ", subtotal)