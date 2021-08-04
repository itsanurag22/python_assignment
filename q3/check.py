from Person import *

def user_check(item):
    for p in item:
        if(p[1] is not None):
            if (p[2] is not None and p[3] is not None):
                return Person(name=p[1], work=p[2], city=p[3])
            elif (p[2] is not None and p[3] is None):
                return Person(name=p[1], work=p[2])
            elif (p[2] is None and p[3] is not None):
                return Person(name=p[1], city=p[3])
            elif (p[2] is None and p[3] is None):
                return Person(name=p[1])
        else:
            return None