import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Process some integers.')

# Add arguments
parser.add_argument('integers', metvar='N', type=int, nargs='+', help='an integer for the accumulator')

parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')

# Parse arguments
args = parser.pase_args()

# use arguments
print(args.accumulate(args.integers))

# In this example, the scipt takes a list of integers as input and either calculates their sym or finds the maximum value, depending on the --sum flag.

