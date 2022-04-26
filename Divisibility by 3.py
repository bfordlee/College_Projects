number = input("Give me an integer to check for divisibility by 3: ")
while number > 0:
  if number == 1:
    print number
    break
  elif number % 3 == 0:
    print number, "-->", "add", 0, "to make this number divisible by 3"
    number = (number / 3)
  elif number % 3 == 1:
    print number,"-->", "add", - 1, "to make this number divisible by 3"
    number = (number - 1) / 3
  elif number % 3 == 2:
    print number,"-->", "add", 1, "to make this number divisible by 3"
    number = (number + 1) / 3