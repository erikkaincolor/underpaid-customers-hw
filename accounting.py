melon_cost = 1.00

def file_to_list(filename):
    """function that organizes file"""
    file = open(filename)
    
    for line in file: #for each item in list
        profile=line.rstrip().split("|") #list
        del profile[0]
        name= profile[0]
        melons = float(profile[1])
        paid = float(profile[2])
        correct_price = (melons * melon_cost)
        if correct_price == paid: #correct price = price cust paid
            print(f"{name} paid ${paid:.2f},",
                f"expected ${correct_price:.2f}" #":.2f" ==Fix point number format...round 2 dec places
                )
    file.close()
            

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )
