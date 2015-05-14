import sys

def fizzbuzz(n):
  numbers = range(1, n+1)
  print("Fizz buzz counting up to {}".format(n))
  for i in numbers:
    output = ""
    if i % 3 == 0:
      output = "fizz "
    if i % 5 == 0:
      output = output + "buzz"
    if output:
      print output.rstrip()
    else:
      print i

number = None
if len(sys.argv) > 1:
  try:
    number = int(sys.argv[1])
  except ValueError:
    print "Please supply a numeric value"
while not number:
  input = raw_input("What number should I FizzBuzz until? ")
  try:
    number = int(input)
  except ValueError:
    print "Please supply a numeric value"
fizzbuzz(number)