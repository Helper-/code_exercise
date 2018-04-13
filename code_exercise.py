def roundNearest(userNum, nearestNum):
  # First mod the userNub by nearestNum
  modOfInput = int(userNum) % int(nearestNum)
  # print("Modulus of input:", modOfInput)

  # Need to know what nearestNum divided by 2 is so I know to round up or down.
  halfNearestNum = int(nearestNum) / 2
  # print("Half of nearestNum:", int(halfNearestNum))

  # If subtracting the modOfInput from the number input makes the value less then 0 just return what you want it rounded to.
  if((int(userNum) - int(modOfInput)) < 0):
    print(nearestNum)
  # Since we know it won't go to 0 we now need to know to round up or round down.
  else:
    # If nearestNum divided by 2 is bigger than the mod of input we round down.
    if( (int(halfNearestNum) > modOfInput) and ((int(userNum) - (int(modOfInput))) > 0) ):
      print(int(userNum) - modOfInput)
    # We round up.
    else:
      print(int(userNum) + (int(nearestNum) - int(modOfInput)))

# Need to make sure input is a real number and that the number is positive.
def checkInput(input1, input2):

  if(input1.lstrip('-').isdigit() != True):
    return print("First input is not a number.")
  elif(input2.isdigit() != True):
    return print("Second input is not a number.")
  elif(int(input2) == 0):
    return print("You can not round a number to 0.")
  
  roundNearest(input1, input2)    

def main():
  print("Welcome to Round to the nearest X!")
  userNum = input("Please enter a number: ")
  nearestNum = input("Please enter a positive number to round it to: ")
  print("You have entered", userNum, "and want it rounded to", nearestNum)

  checkInput(userNum, nearestNum)

if __name__ == "__main__": main()