# In this problem, you need to write a program to calculate the electricity bill based on the units of the electricity the household consumes. The price for a unit varies based on the slab. The charges per unit for different slabs are as mentioned below:

# For the first 50 units (0-50), the charge is 2/unit
# For the next 100 units (51-150), the charge is 3/unit
# For the next 100 units (151-250), the charge is 5/unit
# For above 250 units (251 and above) the charge is 8/unit
# Apart from these charges, there is also an additional surcharge of 20% on the total amount is added to the bill

# Input Format

# The input will be a single line containing an integer

# Output Format

# The output should be a single line containing the calculated bill amount

def generate_electricity_bill(units):
    bill = 0
    while units > 0:
        if units > 0 and units <= 50:
            # charge is 2/unit
            # print("1",units)
            bill += 2 * units
            units = 0
        elif units > 50 and units <= 150:
            # charge is 3/unit
            # print("2",units - 50)
            bill += 3 * (units - 50)
            units = 50
        elif units > 150 and units <= 250:
            # charge is 5/unit
            # print("3",units - 150)
            bill += 5 * (units - 150)
            units = 150
        else:
            # charge is 8/unit
            # print("4",units - 250)
            bill += 8 * (units - 250)
            units = 250
    
    # Add extra 20% charge on the bill
    bill += 0.2 * bill

    return bill


if __name__ == '__main__':
    # units = int(input("Enter the Number of units : "))
    units = int(input())
    total_bill = generate_electricity_bill(units)
    # print("So the total bill should be", total_bill)
    print(total_bill)