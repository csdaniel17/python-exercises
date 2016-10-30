from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()"
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # print out last scene
        current_scene.enter()


class Death(Scene):

    quips = [
        "you died. you kinda suck at this.",
        "your mom would be proud.. if she were smarter",
        "such a luser.",
        "i have a small puppy that's better at this"
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print "the gothons of planet percal #25 have invaded your ship and destroyed"
        print "your entire crew. you are the last surviving member and your last"
        print "mission is to get the neutron destruct bomb from the weapons armory,"
        print "put it in the bridge, and blow the ship up after getting into an"
        print "escape pod."
        print "\n"
        print "you're running down the central corridor to the weapons armory when"
        print "a gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        print "flowing around his hate filled body. he's blocking the door to the"
        print "armory and about to pull a weapon to blast you"

        action = raw_input("> ")

        if action == "shoot!":
            print "quick on the draw you yank out your blaster nd fire it at the gothon."
            print "his clown costume is flowing and moving around his body, which throws"
            print "off your aim. your laser hits his ostume but misses him entirely. this"
            print "completely ruins his brand new costume his mother bought him, which"
            print "makes him fly into an insane rage and blast you repeatedly in the face until"
            print "you are dead. then he eats you."
            return 'death'

        elif action == "dodge!":
            print "like a world class boxer you dodge, weave, slip and slide right"
            print "as the gothon's blaster cranks a laser past your head"
            print "in the middle of your artful dodge your foot slips and you"
            print "bang your head on the metal wall and pass out"
            print "you wake up shortly after only to die as the gothon stomps on"
            print "your head and eats you."
            return 'death'

        elif action == "tell a joke":
            print "lucky for you they made you learn gothon insults in the academy."
            print "you tell the one gothon joke you know:"
            print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
            print "the gothon stops, tries not to laugh, then busts out laughing and can't move"
            print "while he's laughing you run up and shoot him square in the head"
            print "putting him down, then jump through the weapon armory door"
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print "you do a dive roll into the weapon armory, crouch and scan the room"
        print "for more gothons that might be hiding. it's dead quiet, too quiet."
        print "you stand up and run to the far side of the room and find the"
        print "neutron bomb in its container. there's a keypad lock on the box"
        print "and you need the code to get the bomb out. if you get the code"
        print "wrong 10 times then the lock closes forever and you can't"
        print "get the bomb. the code is three digits"
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "the container clicks open and the seal breaks, letting gas out."
            print "you grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return 'the_bridge'
        else:
            print "the lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "you decide to sit there, and finally the gothons blow up the"
            print "ship from their ship and you die"
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print "you burst onto the bridge with the neutron destruct bomb"
        print "under your arm and surprise 5 gothons who are trying to"
        print "take control of the ship. each of them has an even uglier"
        print "clown costume than the last. they haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm adn don't want to set it off."

        action = raw_input("> ")

        if action == "throw the bomb":
            print "in a panic ou throw the bomb at the group of gothons"
            print "and make a leap for the door. right as you drop it a"
            print "gothon shoots you right in the back killing you."
            print "as you die you see another gothon frantically try to disarm"
            print "the bomb. you die knowing they will probably blow up when"
            print "it goes off."
            return 'death'

        elif action == "slowly place the bomb":
            print "you point your blaster at the bomb under your arm"
            print "and the gothons put their hands up and start to sweat."
            print "you inch backward to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "you then jump back through the door, punch the close button"
            print "and blast the lock so the gothons can't get out."
            print "now that the bomb is placed you run to the escape pod to"
            print "get off this tin can."
            return 'escape pod'

        else:
            print "DOES NOT COMPUTE!"
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print "you rush through the ship desperatey trying to make it to"
        print "the escape pod before the whole ship explodes. it seems like"
        print "hardly any gothons are on the ship. so your run is clear of"
        print "interference. you get to the chamber with the escape pods, and"
        print "now need to pick one to take. some of them could be damaged"
        print "but you don't have time to look. there's 5 pods, which one"
        print "do you take?"

        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "you jump into pod %s and hit the eject button." % guess
            print "the pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            return 'death'

        else:
            print "you jump into pod %s and hit the eject button." % guess
            print "the pod easily slides out into space heading to"
            print "the planet below. as it flies to the planet, you look"
            print "back and see your ship implode then explode like a"
            print "bright star, taking out the gothon ship at the same"
            print "time. you won!"
            return 'finished'


class Finished(Scene):

    def enter(self):
        print "you won! good job!"
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
