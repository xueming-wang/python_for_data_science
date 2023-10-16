import sys

def ft_filter(function, iterable) -> list:
    """
    :param function a function
    :param iterable is an iterable like sets, lists, tuples etc
    """
    for i in iterable:
        if function:
            if function(i) is True:
                yield i
        else:
            yield i

def main():
    # new_list = list(ft_filter(None, [0, 1, 2]))
    # print(new_list)
    print(ft_filter.__doc__)
    print(filter.__doc__)

if __name__ == "__main__":
    main()


