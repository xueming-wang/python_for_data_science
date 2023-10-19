import sys

def ft_filter(function, iterable):
    """
    :param function a function
    :param iterable is an iterable like sets, lists, tuples etc
    """
    return [i for i in iterable if (function(i) if function else True)]
    # for i in iterable:
    #     if function:
    #         if function(i) is True:
    #             yield i
    #     else:
    #         yield i

def main():
    print(ft_filter.__doc__)
    print(filter.__doc__)
    # test:
    # new_list = (ft_filter(lambda x: x >= 1, [0, 1, 2]))
    # print(new_list)

if __name__ == "__main__":
    main()


