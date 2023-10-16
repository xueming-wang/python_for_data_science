import sys

if len(sys.argv) == 1:
	sys.exit()
if len(sys.argv) > 2:
	print("AssertionError:  more than one argument is provided")
	sys.exit()

arg = sys.argv[1]

if arg.startswith('-'):
	arg = arg[1:]
		
if not arg.isdigit():
	print("AssertionError: argument is not an integer")
	sys.exit()

else:
	if int(arg) % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")


