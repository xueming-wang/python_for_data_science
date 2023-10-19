import inspect

def NULL_not_found(object: any) -> int:
    # get the name of the object
    frame = inspect.currentframe()
    frame = inspect.getouterframes(frame)[1]
    string = inspect.getframeinfo(frame[0]).code_context[0].strip()
    args = string[string.find('(') + 1:-1].split(',')
    names = []
    for i in args:
        if i.find('=') != -1:
            names.append(i.split('=')[1].strip())
        else:
            names.append(i)

    ## replace name
    variable_name = names[0].replace("Garlic", "Cheese")

    ## get type
    myType = type(object)
    if myType is str and len(object) != 0:
        print("Type not found")
        return 1

    ## print name. value, and type
    print(f"{variable_name}:", object, myType)
    return 0
