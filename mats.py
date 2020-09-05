from usefullFunctions import getcolor

class Material(object):
    def __init__(self, diffuse):
        self.diffuse = diffuse


ivory = Material(diffuse = getcolor(100,100,80))
snowWhite = Material(diffuse = getcolor(255,255,255))
charcoal = Material(diffuse = getcolor(54,69,79))
orange = Material(diffuse= getcolor(255,69,0))