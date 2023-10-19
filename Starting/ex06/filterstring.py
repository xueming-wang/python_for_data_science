import sys
from ft_filter import ft_filter

def filterstring():
    try:
        if len(sys.argv) == 1 or len(sys.argv) != 3:
            raise AssertionError
        if not all(x.isalpha() or x.isspace() for x in sys.argv[1]):
            raise AssertionError
        if not sys.argv[2].isnumeric():
            raise AssertionError
        else:
            string = sys.argv[1]
            number = int(sys.argv[2])
            slist = string.split()
            new_list = list(ft_filter(lambda x: len(x) >= number, slist))
            print(new_list)
    except AssertionError:
        print("AssertionError: the arguments are bad")


def main():
    filterstring()


if __name__ == "__main__":
    main()
