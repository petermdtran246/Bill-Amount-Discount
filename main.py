def Discount():
    amount = int(input('Enter your Bill Amount: '))
    if(amount >= 5000):
        disAmount = float(amount-amount*(20/100.0))
        print(disAmount)
    else:
        if(2000 <= amount < 5000):
            disAmount = float(amount - amount*(10/100.0))
            print(disAmount)
        elif(amount < 2000):
            disAmount = float(amount - amount*(5/100.0))
            print(disAmount)

# Call function
Discount()

