from usefullFunctions import color

class Material(object):
    def __init__(self, diffuse, albedo, specular):
        self.diffuse = diffuse
        self.albedo = albedo
        self.specular = specular


ivory = Material(diffuse = color(100,100,80), albedo = (0.6, 0.3), specular = 50)
rubber = Material(diffuse=color(80, 0, 0), albedo=(0.9,  0.1), specular=10)
christmasbulb = Material(color(255,0,0), (0.7,0.2), 40)
brownfuzz = Material(color(244,164,96), (0.6, 0.3), 25)
darkbrown = Material(color(139,69,19), (0.6, 0.3), 25)
eyesout = Material(color(255,255,255), (0.7,0.2), 50)
eyesin = Material(color(0,0,0), (0.7,0.2), 50)