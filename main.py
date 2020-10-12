from ray import RayTracer
from ray import White
from sphere import Sphere
from usefullFunctions import V3
from light import Light
from mats import Texture, water, grass, stone, cloud, snow
from usefullFunctions import color
from cube import Cube
from plane import Plane


r = RayTracer(2048, 2048)

r.light = Light(
  position=V3(0,20, -2),
  intensity= 1.5
)

r.backgroundColor = color(50,50,200)

r.scene = [
  #Sky
  Cube(V3(-1,4.9,-15), cloud , Texture('textures/cloud.bmp')),
  Cube(V3(0,4.9,-15), cloud , Texture('textures/cloud.bmp')),
  Cube(V3(1,4.9,-15), cloud , Texture('textures/cloud.bmp')),
  Cube(V3(2,4.9,-15), cloud , Texture('textures/cloud.bmp')),
  Cube(V3(3,4.9,-15), cloud , Texture('textures/cloud.bmp')),
  Cube(V3(4,4.9,-15), cloud , Texture('textures/cloud.bmp')),

  Cube(V3(0,5.9,-14), cloud , Texture('textures/cloud.bmp')),
  Cube(V3(1,5.9,-14), cloud , Texture('textures/cloud.bmp')),
  Cube(V3(2,5.9,-14), cloud , Texture('textures/cloud.bmp')),
  Cube(V3(3,5.9,-14), cloud , Texture('textures/cloud.bmp')),
  Cube(V3(4,5.9,-14), cloud , Texture('textures/cloud.bmp')),
  Cube(V3(5,5.9,-14), cloud , Texture('textures/cloud.bmp')),

  Cube(V3(1,6.9,-13), cloud , Texture('textures/cloud.bmp')),
  Cube(V3(2,6.9,-13), cloud , Texture('textures/cloud.bmp')),
  Cube(V3(3,6.9,-13), cloud , Texture('textures/cloud.bmp')),
  Cube(V3(4,6.9,-13), cloud , Texture('textures/cloud.bmp')),

  # background
  #Fith layer
  Cube(V3(-3,4.9,-13), stone , Texture('textures/stone.bmp')),
  Cube(V3(5,4.9,-13), stone, Texture('textures/stone.bmp')),
  Cube(V3(6,4.9,-13), snow, Texture('textures/snow.bmp')),
  Cube(V3(7,4.9,-13), snow, Texture('textures/snow.bmp')),

  #Forth Layer
  Cube(V3(-4,3.9,-12), stone, Texture('textures/stone.bmp')),
  Cube(V3(-3,3.9,-12), snow, Texture('textures/snow.bmp')),
  Cube(V3(-3,3.9,-13), stone, Texture('textures/stone.bmp')),
  Cube(V3(4,3.9,-12), stone, Texture('textures/stone.bmp')),
  Cube(V3(5,3.9,-12), snow, Texture('textures/snow.bmp')),
  Cube(V3(6,3.9,-12), snow, Texture('textures/snow.bmp')),


  #Third layer
  Cube(V3(-4,2.9,-11), stone, Texture('textures/stone.bmp')),
  Cube(V3(-3,2.9,-11),snow, Texture('textures/snow.bmp')),
  Cube(V3(-2,2.9,-11), stone, Texture('textures/stone.bmp')),
  Cube(V3(3,2.9,-11), stone, Texture('textures/stone.bmp')),
  Cube(V3(4,2.9,-11), snow, Texture('textures/snow.bmp')),
  Cube(V3(5,2.9,-11), snow, Texture('textures/snow.bmp')),
  Cube(V3(6,2.9,-11), snow, Texture('textures/snow.bmp')),
  
  #Second layer
  Cube(V3(-4.5,1.9,-10), stone, Texture('textures/stone.bmp')),
  Cube(V3(-3.5,1.9,-10), snow, Texture('textures/snow.bmp')),
  Cube(V3(-2.5,1.9,-10), snow, Texture('textures/snow.bmp')),
  Cube(V3(-1.5,1.9,-10), stone, Texture('textures/stone.bmp')),
  Cube(V3(2,1.9,-10), stone, Texture('textures/stone.bmp')),
  Cube(V3(3,1.9,-10), stone, Texture('textures/stone.bmp')),
  Cube(V3(4,1.9,-10), snow, Texture('textures/snow.bmp')),
  Cube(V3(5,1.9,-10), snow, Texture('textures/snow.bmp')),

  
  #First layer
  Cube(V3(-5,0.9,-9), stone, Texture('textures/stone.bmp')),
  Cube(V3(-4,0.9,-9), stone, Texture('textures/stone.bmp')),
  Cube(V3(-3,0.9,-9), stone, Texture('textures/stone.bmp')),
  Cube(V3(-2,0.9,-9), stone, Texture('textures/stone.bmp')),
  Cube(V3(-1,0.9,-9), stone, Texture('textures/stone.bmp')),
  Cube(V3(0,0.9,-9), stone, Texture('textures/stone.bmp')),
  Cube(V3(1,0.9,-9), stone, Texture('textures/stone.bmp')),
  Cube(V3(2,0.9,-9), stone, Texture('textures/stone.bmp')),
  Cube(V3(3,0.9,-9), stone, Texture('textures/stone.bmp')),
  Cube(V3(4,0.9,-9), stone, Texture('textures/stone.bmp')),
  Cube(V3(5,0.9,-9), stone, Texture('textures/stone.bmp')),
  #Fore Ground
  # Forth layer
  Cube(V3(-5,-0.1,-10), grass, Texture('textures/grass.bmp')),
  Cube(V3(-4,-0.1,-10), grass, Texture('textures/grass.bmp')),
  Cube(V3(-3,-0.1,-10), grass, Texture('textures/grass.bmp')),
  Cube(V3(-2,-0.1,-10), grass, Texture('textures/grass.bmp')),
  Cube(V3(-1,-0.1,-10), grass, Texture('textures/grass.bmp')),
  Cube(V3(0,-0.1,-10), grass, Texture('textures/grass.bmp')),
  Cube(V3(1,-0.1,-10), water),
  Cube(V3(2,-0.1,-10), water),
  Cube(V3(3,-0.1,-10), grass, Texture('textures/grass.bmp')),
  Cube(V3(4,-0.1,-10), grass, Texture('textures/grass.bmp')),
  Cube(V3(5,-0.1,-10), grass, Texture('textures/grass.bmp')),
  #Third layer
  Cube(V3(-5,-1.1,-9), grass, Texture('textures/grass.bmp')),
  Cube(V3(-4,-1.1,-9), grass, Texture('textures/grass.bmp')),
  Cube(V3(-3,-1.1,-9), grass, Texture('textures/grass.bmp')),
  Cube(V3(-2,-1.1,-9), grass, Texture('textures/grass.bmp')),
  Cube(V3(-1,-1.1,-9), grass, Texture('textures/grass.bmp')),
  Cube(V3(0,-1.1,-9), grass, Texture('textures/grass.bmp')),
  Cube(V3(1,-1.1,-9), water),
  Cube(V3(2,-1.1,-9), water),
  Cube(V3(3,-1.1,-9), water),
  Cube(V3(4,-1.1,-9), grass, Texture('textures/grass.bmp')),
  Cube(V3(5,-1.1,-9), grass, Texture('textures/grass.bmp')),

  #Second layer
  Cube(V3(-4,-2.1,-8), grass, Texture('textures/grass.bmp')),
  Cube(V3(-3,-2.1,-8), grass, Texture('textures/grass.bmp')),
  Cube(V3(-2,-2.1,-8), grass, Texture('textures/grass.bmp')),
  Cube(V3(-1,-2.1,-8), grass, Texture('textures/grass.bmp')),
  Cube(V3(0,-2.1,-8), water),
  Cube(V3(1,-2.1,-8), water),
  Cube(V3(2,-2.1,-8), water),
  Cube(V3(3,-2.1,-8), water),
  Cube(V3(4,-2.1,-8), grass, Texture('textures/grass.bmp')),
  #First layer
  Cube(V3(-4,-3.1,-7), grass, Texture('textures/grass.bmp')),
  Cube(V3(-3,-3.1,-7), grass, Texture('textures/grass.bmp')),
  Cube(V3(-2,-3.1,-7), grass, Texture('textures/grass.bmp')),
  Cube(V3(-1,-3.1,-7), water),
  Cube(V3(0,-3.1,-7), water),
  Cube(V3(1,-3.1,-7), water),
  Cube(V3(2,-3.1,-7), water),
  Cube(V3(3,-3.1,-7), water),
  Cube(V3(4,-3.1,-7), grass, Texture('textures/grass.bmp')),
  

]
r.render()
r.glFinish()