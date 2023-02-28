
def fizzBuzz():
  x = 16 # enter the value up to which you want to print values
  for n in range(1,x):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
        continue
    elif n % 3 == 0:
        print("Fizz")
        continue
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 != 0 and n % 5 != 0:
       print(int(n))
       continue

fizzBuzz()
