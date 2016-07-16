# ex8: Printing, printing

formatter = "%r %r %r %r"

# will print: 1 2 3 4
print formatter % (1, 2, 3, 4)

# will print: 'one' 'two' 'three' 'four'
print formatter % ("one", "two", "three", "four")

# will print: True, False, False, True
print formatter % (True, False, False, True)

# will print: '%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
print formatter % (formatter, formatter, formatter, formatter)

# will print: 'I had this this.' 'That you could type up right.' 'But it didn't sing.' 'So I said goodnight.'
print formatter % (
    "I had this this.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
