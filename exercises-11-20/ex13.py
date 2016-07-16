# ex13: Parameters, unpacking, variables


# import - how you add features to your script - keeps your programs small, but also acts as documentation for other programmers to read your code - modules
from sys import argv  # argv: argument variablew - sys: system module

script, first, second, third = argv  # unpacks argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
