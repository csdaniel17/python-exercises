# ex18: Names, variables, code, functions


# this function is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args  # unpacks arguments
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# that *args is the same as:
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this takes just one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this takes no arguments
def print_none():
    print "I got nothing!"

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
