#!/usr/bin/python
import argparse

import numpy


def main(args):

    print(create_message(args.name))

    x = numpy.array([1,2,3])

    print("Printing numpy array")
    print(x)


def create_message(name):
    return "Hi {0}".format(name)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-n", "--name", help="specify the name to say hi to", default="noname")

    parsed_args = parser.parse_args()

    main(parsed_args)

