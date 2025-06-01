#-----------------------------------------------------------------------
# body.py
#-----------------------------------------------------------------------

from enum import Enum
from matplotlib.patches import Circle
from vector import Vector

class Body:
    """
    构造一个新的Body对象，其属性由BodyUnit对象指定。或者更具体地，其位置由Vector对象r指定，
    其速度由Vector对象v指定，其质量由浮点数mass指定，其球体半径由浮点数radius指定。
    """
    def __init__(self, r, v, mass_radius):
        self._r = Vector(r[:])      # 位置Position
        self._v = Vector(v[:])      # 速度Velocity
        self._mass = mass_radius[0] # 质量Mass
        self._radius = mass_radius[1]  # 半径Radius

    # Move self by applying the force specified by Vector object
    # f for the number of seconds specified by float dt.
    def move(self, f, dt):
        a = f.scale(1 / self._mass)
        self._v = self._v + (a.scale(dt))
        self._r = self._r + self._v.scale(dt)

    # Return the force between Body objects self and other.
    def force_from(self, other):
        G = 6.67e-11
        delta = other._r - self._r
        dist = abs(delta)
        magnitude = (G * self._mass * other._mass) / (dist * dist)
        return delta.direction().scale(magnitude)

    # Return a string representation of self.
    def __str__(self):
        return "Body({}, {}, {:.2e}, {:.2e})".format(self._r.str(), self._v.str(), self._mass, self._radius)

class Planet(Enum):
    """
    构造一个定义星体的类，其中用二元组枚举了9大行星的质量和半径。
    """
    SUN     = (1.989e+30, 6.955e8)
    MERCURY = (3.303e+23, 2.4397e6)
    VENUS   = (4.869e+24, 6.0518e6)
    EARTH   = (5.976e+24, 6.37814e6)
    MARS    = (6.421e+23, 3.3972e6)
    JUPITER = (1.9e+27, 7.1492e7)
    SATURN  = (5.688e+26, 6.0268e7)
    URANUS  = (8.686e+25, 2.5559e7)
    NEPTUNE = (1.024e+26, 2.4746e7)
    MOON    = (7.35e+19, 1.738e6)

    # Create a planet: the value of the enum member will be passed to this method
    def __init__(self, mass, radius):
        self.mass = mass  # in kilograms
        self.radius = radius  # in meters

    # Return the surface gravity of self
    @property
    def surface_gravity(self):
        # universal gravitational constant  (m3 kg-1 s-2)
        G = 6.67300E-11
        return G * self.mass / (self.radius * self.radius)