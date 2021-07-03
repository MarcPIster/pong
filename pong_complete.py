#!/usr/bin/env python3
import sys
import numpy as np
import math

def print_help():
  print('USAGE')
  print('\t./101pong x0 y0 z0 x1 y1 z1 n\n')
  print('DESCRIPTION')
  print('\tx0  ball abscissa at time t - 1')
  print('\ty0  ball abscissa at time t - 1')
  print('\tz0  ball abscissa at time t - 1')
  print('\tx1  ball abscissa at time t')
  print('\ty1  ball abscissa at time t')
  print('\tz1  ball abscissa at time t')
  print('\tn   time shift (greater than or equal to zero, integer)')
  exit(0)


def print_array(velocety):
    a = ("{:.2f}".format(velocety[0]))
    b = ("{:.2f}".format(velocety[1]))
    c = ("{:.2f}".format(velocety[2]))
    print('(', end='')
    print(a, end=', ')
    print(b, end=', ')
    print(c, end=')\n')

def get_velocety(argv):
    x = np.array([(float(argv[1])), (float(argv[2])), (float(argv[3]))])
    y = np.array([(float(argv[4])), (float(argv[5])), (float(argv[6]))])
    velocety = y - x
    return velocety

def get_timeshift(velocety, argv):
    a = float(argv[4]) + (float(argv[7]) * velocety[0])
    b = float(argv[5]) + (float(argv[7]) * velocety[1])
    c = float(argv[6]) + (float(argv[7]) * velocety[2])
    nvelocety = np.array([a, b, c])
    return nvelocety

def incind_angle(velocety, argv):
    if (float(argv[3]) < 0 and float(argv[6]) >= 0 or float(argv[3]) >= 0 and float(argv[6]) < 0):
        print("The ball won’t reach the paddle.")
        exit(84)
    a = pow(velocety[0], 2)
    b = pow(velocety[1], 2)
    c = pow(velocety[2], 2)
    normalvec = np.array([0.00, 0.00, 1.00])
    powarr = np.array([a, b, c])
    powsum = np.sum(powarr)
    lvelocety = np.sqrt(powsum)
    x = (velocety[0] * normalvec[0])
    y = (velocety[1] * normalvec[1])
    z = (velocety[2] * normalvec[2])
    uvecarr = np.array([x, y, z])
    uvecsqr = np.sqrt(pow(sum(uvecarr), 2))
    sinangle = round((uvecsqr / lvelocety), 4)
    angle = math.degrees(math.asin(sinangle))
    print("The incidence angle is:", end="\n")
    print("{:.2f}".format(angle), end="")
    print(" degrees", end="\n")
    return angle

def check_argv(argv):
    try:
        x = len(argv) - 1
        if int(argv[7]) < 0:
            exit(84)
        while x > 0:
            check = isinstance(float(argv[x]), float)
            x -= 1
    except:
        #print(argv[1])
        print('False input, try ./pong101 -h for more informations')
        exit(84)

def check_import(argv):
    if (len(argv) == 8):
        check_argv(argv)
    elif (len(argv) == 2):
        if (argv[1] == "-h"):
            print_help()
        else:
            print('Did you mean -h? Try ./pong101 -h for more informations')
            exit(84)
    else:
        print('False input, try ./pong101 -h for more informations')
        exit(84)

def main(argv):
    check_import(argv)
    print('The velocity vector of the ball is:')
    print_array(get_velocety(argv))
    print('At time t + ', end='')
    print(argv[7], end='')
    print(', ball coordinates will be:')
    print_array(get_timeshift(get_velocety(argv), argv))
    incind_angle(get_velocety(argv), argv)

if __name__ == '__main__':
    main(sys.argv)
