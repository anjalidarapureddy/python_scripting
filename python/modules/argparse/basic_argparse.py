import argparse

parser = argparse.ArgumentParser()# create CLI parser

parser.add_argument("--name") #define input parameter

args = parser.parse_args() # read CLI input

print(args.name)

'''
types of arguments
req argument:
    parser.add_argument("--env", required=True) #if missing error
default argument:
    parser.add_argument("--env", default="dev")
choice arguments:
    parser.add_argument("--env", choices=["dev", "prod"])
type validation:
    parser.add_argument("--port", type=int)

'''
