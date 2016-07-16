# What was that?

print "I am 6'2\" tall." # escape the double-quote inside string
print 'I am 6\'2" tall.' # escape the single-quote inside string

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

fat_cat_2 = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print fat_cat
print fat_cat_2

# escape       what it does
# \\           Backslash (\)
# \'	       Single-quote (')
# \"	       Double-quote (")
# \a	       ASCII bell (BEL)
# \b	       ASCII backspace (BS)
# \f	       ASCII formfeed (FF)
# \n	       ASCII linefeed (LF)
# \N{name}     Character named name in the Unicode database(Unicode only)
# \r	       Carriage Return (CR)
# \t	       Horizontal Tab (TAB)
# \uxxxx	   Character with 16-bit hex value xxxx(Unicode only)
# \Uxxxxxxxx   Character with 32-bit hex value xxxxxxxx(Unicode only)
# \v	       ASCII vertical tab (VT)
# \ooo         Character with octal value ooo
# \xhh	       Character with hex value hh


# while True:
#     for i in ["/", "-", "|", "\\", "|"]:
#         print "%s\r" % i,
    ## infinite loop
