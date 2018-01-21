#pass message to the notifier
#notifier will check the conf file and accordingly
#it will activate the  message
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("MESSAGE", help="Enter the Message")

args = parser.parse_args()

print args.MESSAGE
