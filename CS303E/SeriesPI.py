# Excercise 5.27
def main ():

  total = 0
  for i in [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]:
    for k in range (1, 2 * i + 1, 2):
      sign = - (k % 4 - 2)
      total += float (sign) / k
    print ("i =", i, "PI =", 4 * total)
    total -= total


main ()