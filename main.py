from ray import RayTracer
from ray import White
from sphere import Sphere
from usefullFunctions import V3
from light import Light
from mats import *
from usefullFunctions import color
from cube import Cube
from plane import Plane


r = RayTracer(500, 500)

r.light = Light(
  position=V3(20, 20, 20),
  intensity=1.5
)

r.backgroundColor = color(50, 50, 200)

r.scene = [
  Cube(V3(2,0,-10), rubber)
]
r.render()
r.glFinish()