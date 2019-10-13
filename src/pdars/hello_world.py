#!/usr/bin/python
import argparse


def main(args):

    print("Hi {0}".format(args.name))


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-n", "--name", help="specify the name to say hi to", default="noname")

    parsed_args = parser.parse_args()

    main(parsed_args)

