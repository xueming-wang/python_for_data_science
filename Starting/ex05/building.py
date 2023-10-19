import sys
import string

def main():
	"""
	main function
	"""
	# more than one argument
	if len(sys.argv) > 2:
		print("AssertionError: Invalid number of arguments")
		return

	if len(sys.argv) == 2:
		text = sys.argv[1]
	else:
		text = input('What is the text to count?\n')
	# print the result
	print("The text contains", len(text), "characters:")
	print(sum(1 for i in text if i.isupper()),  "upper letters")
	print(sum(1 for i in text if i.islower()), "lower letters")
	print(sum(1 for i in text if i in string.punctuation), "punctuation marks")
	print(sum(1 for i in text if i.isspace()), "spaces")
	print(sum(1 for i in text if i.isdigit()), "digits")
	

if __name__ == "__main__":
	main()


