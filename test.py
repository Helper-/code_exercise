from code_exercise import checkInput

print(" ")

# Test #1 Make sure it doesn't print 0
print("Test 1")
print("You have entered", 3, "and want it rounded to", 10)
print("We should expect 10: ", end = "", flush = True)
checkInput("3", "10")

print(" ")

# Test #2 Make sure the first input doesn't accept letters.
print("Test 2")
print("You have entered", "abc", "and want it rounded to", 10)
print("We should expect, First input is not a number: ", end = "", flush = True)
checkInput("abc", "10")

print(" ")

# Test #3 Make sure it doesn't accept letters.
print("Test 3")
print("You have entered", 7, "and want it rounded to", "abc")
print("We should expect, Second input is not a number: ", end = "", flush = True)
checkInput("7", "abc")

print(" ")

# Test #4 Make sure it doesn't print 0 should still round up to 50
print("Test 4")
print("You have entered", 0, "and want it rounded to", 50)
print("We should expect 50: ", end = "", flush = True)
checkInput("0", "50")

print(" ")

# Test #5 Make sure it doesn't print 0
print("Test 5")
print("You have entered", 25, "and want it rounded to", 0)
print("We should expect, You can not round a number to 0: ", end = "", flush = True)
checkInput("25", "0")

print(" ")

# Test #6 Make sure it only accepts integers.
print("Test 6")
print("You have entered", "!", "and want it rounded to", 5)
print("We should expect, First input is not a number: ", end = "", flush = True)
checkInput("!", "5")

print(" ")