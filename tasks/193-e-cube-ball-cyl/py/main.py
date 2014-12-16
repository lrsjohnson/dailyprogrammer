import math

###
# Shape Functions: take in a volume, and return a string representing the dimensions of a shape that
# has that volume.
###

## Ratio of height / radius
CONE_HEIGHT_TO_RADIUS = 2.0
CYLINDER_HEIGHT_TO_RADIUS = 2.0

def cube(vol):
    """ vol = s^3 """
    side = vol ** (1 / 3.0)
    return "Cube: width %1.2fm, length %1.2fm, height %1.2fm" % (side, side, side)

def sphere(vol):
    """ vol = 4 / 3 * pi * r^3"""
    r_cubed = 3 / (4.0 * math.pi)
    r = r_cubed ** (1 / 3.0)
    return "Sphere: radius %1.2fm"

def cylinder(vol):
    """ vol = pi * r^2 * h
        vol = pi * r^2 * r * CYLINDER_HEIGHT_TO_RADIUS"""
    r_cubed = vol / (math.pi * CYLINDER_HEIGHT_TO_RADIUS)
    r = r_cubed ** (1 / 3.0)
    h = r * CYLINDER_HEIGHT_TO_RADIUS
    return "Cylinder: radius %1.2fm, height %1.2fm" % (r, h)

def cone(vol):
    """ vol = 1/3 * pi * r^2 * h
        vol = 1/3 * pi * r^2 * r * CONE_HEIGHT_TO_RADIUS """
    r_cubed = vol * 3.0 / (math.pi * CONE_HEIGHT_TO_RADIUS)
    r = r_cubed ** (1 / 3.0)
    h = r * CONE_HEIGHT_TO_RADIUS
    return "Cone: radius %1.2fm, height %1.2fm" % (r, h)

SHAPES = (cube, cylinder, sphere, cone)

###
# Interface for interacting with shape functinos
###

def get_output(inp):
    """Input to output"""
    try:
        vol = float(inp)
    except ValueError:
        return "Error: %s is not a valid number" % inp
    output = ""
    for shape_func in SHAPES:
        output += shape_func(vol) + "\n"
    return output


def main():
    inp = input()
    output = get_output(inp)
    print output,

if __name__ == "__main__":
    main()
