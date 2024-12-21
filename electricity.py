...
#write a python program to input electricty units and calculate total electricity bill according to given condition
 
#for first 50 units Rs 0.45 per unit
 
#for second 100 units rs 0.65 perunit
 
#for third 150 units  rs 1.00 per unit
 
#for fourth 200 units rs 1.55 perunit
 
#for fifth 250units Rs 1.75 perunit
 
#additional charges is 10% to the bill

def calculate_bill(units):
    if units <=50:
        bill = units*0.45
    elif units <=150:
        bill = 50*0.45 + (units-50)*0.65
    elif units<=200:
        bill = 50*0.45 + 100*0.65 + (units-150)*1.00
    elif units<=250:
        bill = 50*0.45 + 100*0.65 + 50*1.00 + (units-200)*1.55
    else:
        bill = 50*0.45 + 100*0.65 + 50*1.00 + 50*1.55 + (units-250)*1.75

        bill*=1.10
        
        return bill
    
    units=float(input("enter the no.of electricity units:"))
    bill=calculate_bill(units)
    print("your electricity bill is : Rs{:.2f}".format(bill))

