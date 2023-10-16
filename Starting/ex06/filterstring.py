import sys
from ft_filter import ft_filter


def filterstring():
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        return
    if all(sys.argv[1].isalpha() and sys.argv[1].isspace() for x in sys.argv[1]):
        return
    if not sys.argv[2].isnumeric():
        return

    string = sys.argv[1]
    number = int(sys.argv[2])
    slist = string.split()

    new_list = list(ft_filter(lambda x: len(x) >= number, slist))
    print(new_list)


def main():
    filterstring()


if __name__ == "__main__":
    main()
