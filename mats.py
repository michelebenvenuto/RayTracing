from usefullFunctions import color
import struct

class Material(object):
    def __init__(self, diffuse, albedo=(1, 0, 0, 0), specular = 0, refractive_index = 1):
        self.diffuse = diffuse
        self.albedo = albedo
        self.specular = specular
        self.refractive_index = refractive_index

class Texture(object):
    def __init__(self, path):
        self.path = path
        self.read()

    def read(self):
        image = open(self.path, "rb")

        image.seek(2 + 4 + 4)
        header_size = struct.unpack("=l", image.read(4))[0]
        image.seek(2 + 4 + 4 + 4 + 4)

        self.width = struct.unpack("=l", image.read(4))[0]  
        self.height = struct.unpack("=l", image.read(4))[0] 
        image.seek(header_size)

        self.pixels =[]

        for y in range(self.height):
            self.pixels.append([])
            for x in range(self.width):
                b = ord(image.read(1))
                g = ord(image.read(1))
                r = ord(image.read(1))
                self.pixels[y].append(color(r,g,b))
        image.close()
    
    def getColor(self, tx, ty, intensity=1):
        if tx >= 0 and tx <= 1 and ty >= 0 and ty <= 1:
            x = round(tx * self.width - 1)
            y = round(ty * self.height - 1)

            return self.pixels[y][x]
        else:
            return color(0,0,0)

# ivory = Material(diffuse=color(100, 100, 80), albedo=(0.6, 0.3, 0.1, 0), specular=50)
# rubber = Material(diffuse=color(80, 0, 0), albedo=(0.9, 0.1, 0, 0, 0), specular=10)
# glass = Material(diffuse=color(150, 180, 200), albedo=(0, 0.5, 0.1, 0.8), specular=125, refractive_index=1.5)
# mirror = Material(diffuse=color(255, 255, 255), albedo=(0, 10, 0.8, 0), specular=1425)
stone = Material(diffuse= color(184,176,155), albedo=(1, 0, 0, 0))
water = Material(diffuse=color(	135, 206, 235), albedo=(0, 5, 0.6,0), specular=1000, refractive_index=1.33)
grass = Material(diffuse=color(132, 192,17), albedo=(0.9, 0.1, 0, 0) )
cloud = Material(diffuse = color(255,255,255), albedo=(0.6, 0.3, 0, 0))
snow = Material(diffuse =(255,255,255), albedo=(0.9,0.2,0,0), specular=75)