#-----------------------------------------------------------------------
# universe.py
#-----------------------------------------------------------------------

from n_body.body import Body,Planet
from n_body.vector import Vector

class UniBase:
    """
    构造一个包含n个Body对象的Universe类，其中Body对象的数量为n，bodies是Body对象表。
    """
    # Create a universe of n bodies
    def __init__(self, n, r_v_mr_list):
        self.n = n
        assert(6 * n == len(r_v_mr_list))
        self.bodies = n * [0]
        for i in range(n):
            self.bodies[i] = Body(r_v_mr_list[2 * i:2 * i + 2], r_v_mr_list[2 * i + 2:2 * i + 4],
                                  (r_v_mr_list[2 * i + 4] , r_v_mr_list[2 * i + 5]))

    # Return a string representation of self.
    def __str__(self):
        return "Universe{}".format([b.__str__() for b in self.bodies])

    # Simulate the passing of dt seconds in self.
    def increase_time(self, dt):
        # Initialize the forces to zero.
        f = [Vector([0,0])] * self.n
        assert(self.n == len(f))

        # Compute the forces.
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    bodyi = self.bodies[i]
                    bodyj = self.bodies[j]
                    f[i] = f[i] + bodyi.force_from(bodyj)

        # Move the bodies.
        for i in range(self.n):
            self.bodies[i].move(f[i], dt)

class Universe(UniBase):
    """
    构造一个包含n个Body对象的Universe类，其Body对象都是以PLANETS命名的，数量为n，bodies是Body对象表。
    """
    PLANETS = ['SUN', 'MERCURY', 'VENUS', 'EARTH', 'MARS', 'JUPITER', 'SATURN', 'URANUS', 'NEPTUNE', 'MOON']

    # Create a universe of n bodies, starting from the i_th planet
    def __init__(self, n, i_th, r_v_list):
        self.n = n
        assert (4 * n == len(r_v_list))
        self.i_th = n * [0]
        for i in range(n):
            self.i_th[i] = (i_th - 1 + i) % len(Universe.PLANETS)

        self.bodies = n * [0]
        for i in range(n):
            planet = eval('Planet.{}'.format(Universe.PLANETS[(self.i_th[i])]))
            self.bodies[i] = Body(r_v_list[2 * i:2 * i + 2], r_v_list[2 * i + 2:2 * i + 4], planet.value)

    # Return a short string representation of self.
    def __str__(self):
        planets = [eval('Planet.{}'.format(Universe.PLANETS[i])) for i in self.i_th]
        return "Universe{}{}".format(self.i_th[0], [p.name for p in planets])
    # Return a long string representation of self.
    def str(self):
        return "Universe{}{}".format(self.i_th[0], [b.__str__() for b in self.bodies])


def main():
    uni = Universe(2, 7, [0.0e00, 4.5e10, 1.0e04, 0.0e00, 1.0e04, 4.5e10, 0.5e00, 0.0e00])
    uni.increase_time(2)
    print(uni.str())

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python universe.py 2bodyTiny.txt 20000

# python universe.py 2body.txt 20000

# python universe.py 3body.txt 20000

# python universe.py 4body.txt 20000

