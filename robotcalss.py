class Robot(object):
    def __init__(self,name=None):
        self.name=name
    def say_hi(self):
        if self.name:
            print "Hi Myname is "+self.get_name()
            print "Hi, I am an anonemus Robot"

    def set_name(self,name):
        self.name=name

    def get_name(self):
        return self.name


mavan=Robot("mavan")
haris=Robot()
mavan.say_hi()
haris.say_hi()
haris.set_name("haris")
haris.say_hi()
mavan.get_name()