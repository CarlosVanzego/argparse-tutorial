# import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)


# making "echo" more useful
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the stirng you use here")
args = parser.parse_args()
print(args.echo)


# making "echo" even MORE useful
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",
                    type=int)
args = parser.parse_args()
print(args.square**2)