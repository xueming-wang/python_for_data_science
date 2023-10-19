import sys


try:
	if len(sys.argv) == 1:
		sys.exit()
	if len(sys.argv) > 2:
		raise AssertionError
	else:
		arg = sys.argv[1]
		if arg.startswith('-'):
			arg = arg[1:]
		if not arg.isdigit():
			print("AssertionError: argument is not an integer")
		else:
			print("I'm Even." if int(arg) % 2 == 0 else "I'm Odd.")
except AssertionError:
	print("AssertionError:  more than one argument is provided")



