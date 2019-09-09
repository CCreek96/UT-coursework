
def main():
  finalCost = 0
  group1 = ['English Breakfast', 'Earl Gray', 'Irish Breakfast', 'Lemon Balm', 'Sencha', 'Orange Breakfast']
  group2 = ['English Afternoon', 'Breakfast Berry', 'Pomegranate']
  group3 = ['Candied Chestnut', 'Hibiscus']
  priceDict3 = {'5':8, '10':15, '20': 20}
  priceDict4 = {'5':5, '10':10, '20': 15}
  while True:
    type = input("Enter type of tea: ")
    quantity = int(input("Enter quantity of tea: "))
    cost = 0
    if type in group1:
        cost += (quantity/2)
    elif type in group2:
        cost += ((quantity/2)+1)
    elif type in group3:
        for key in priceDict3:
            if str(quantity) == key:
                cost += priceDict3[key]
    elif type == 'Silver Needle':
        for key in priceDict4:
            if str(quantity) == key:
                cost += priceDict4[key]
    finalCost += cost
    cont = input('Add another?(y/n): ')
    if cont == 'n':
      break
  print("Total Cost = " + str(finalCost))
main()
