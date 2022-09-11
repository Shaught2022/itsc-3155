numberOfItems = int(input("Number of Items :"))
myList = []
myTup = ()
for i in range(int(numberOfItems)):
    getItemPrice = input(("Input item and price: "))
    myTup = (getItemPrice)
    myList.append(myTup)
myList.sort()
print(*myList,sep='\n')