# ex40: Modules, Classes, and Objects

## oop: uses classes
# a class is a way to take a grouping of functions and data and place them inside a container so you can access them with the . operator

# # dictionary with a key 'apple'
# mystuff = {'apple': "I AM APPLES!"}
# # to get it:
# print mystuff['apple']

## modules:
# 1. a python file with some functions or variables in it
# 2. you import that file
# 3. you can access the functions or variables in that module with the . operator

### three ways to get things from things:
# # dict style
# mystuff['apples']
#
# # module style
# mystuff.apples()
# print mystuff.tangerine
#
# # class style
# thing = MyStuff()
# thing.apples()
# print thing.tangerine

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
happy_bday = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family", "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
