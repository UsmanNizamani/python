import math
print(math.sqrt(6464))

print("zero")
print("one")
print("two")
print("three")
print("four")
print("five")

#It write all in one line
print("zero",end="       ")
print("one",end="        ")
print('two' ,end="       ")
print("three", end="     ")
print("four" ,end="      ")
print("five",end="       ")

print("one","two","three",sep="   + print  +    ")
print("one","two ","three",sep="\n")

#It shows in single digit after decimal


print(format(12345.67898686,'.1f'))

#It is used for scintefic notation

print(format(12345.6789,'.2e'))

#to put comma in large values

print(format(123456789,'3,'))

print(format(12345.67895475474563465436, '3.2f'))
print(format(12345.6789, '3.4f'))

#cahnging into percentage

print(format(5.99,'.2%'))

name = "usman"
n = 12345667
print("%s %d" % (name,n))

INTEREST_RATE = 0.069
balance = int(input("what is your balance "))
amount = balance * INTEREST_RATE

print(amount)