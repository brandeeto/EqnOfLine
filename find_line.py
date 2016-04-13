import sys
from fractions import Fraction


def try_get_slope(x1, y1, x2, y2):
    try:
        slope = (y1 - y2)/(x1 - x2)
        return Fraction(slope).limit_denominator()
    except ZeroDivisionError:
            print "x=%d" % (x1)
            sys.exit(0)


def main():
        # Parse the command line for user args
        if len(sys.argv) == 5:
            x1 = float(sys.argv[1])
            y1 = float(sys.argv[2])
            x2 = float(sys.argv[3])
            y2 = float(sys.argv[4])
        else:
            print "Usage: find_line.py x1 y1 x2 y2"
            sys.exit()

        # Calculate the slope in fractional form
        slope = try_get_slope(x1, y1, x2, y2)
        slope_d = slope.denominator
        slope_n = slope.numerator

        # Calculate x1 in both decimal and fractional forms
        x1 = slope*(-x1)
        x1_fraction = Fraction(x1).limit_denominator()

        # Calculate y1
        y1 = slope.denominator*(y1)

        total = x1_fraction.numerator + y1

        print "%dy%+dx=%d" % (slope_d, -slope_n, total)

if __name__ == '__main__':
    main()
