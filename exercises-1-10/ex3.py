# ex3: Numbers and math

# + plus
# - minus
# / slash
# * asterisk
# % percent - the remaining part of divison
# < less-than
# > greater-than
# <= less-than-equal
# >= greater-than-equal

# there are no fractions - so you need to use a "floating point" umber when you have a remainder

print "I will now count my chickens:"

print "Hens", 25 + 30 / 6  # Hens 30
print "Roosters", 100 - 25 * 3 % 4
# Roosters 97 -> 25*3=75 75%4=3 100-3=97

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6  # 7

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7  # False

print "What is 3 + 2?", 3 + 2  # 5
print "What is 5 - 7", 5 - 7  # -2

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2  # True
print "Is it greater or equal?", 5 >= -2  # True
print "Is it less or equal?", 5 <= -2  # False

print 7.0 / 4.0
print 7 / 4  # rounds down
