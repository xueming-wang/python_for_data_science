
def all_thing_is_obj(object: any) -> int:

	type_lst = [list, tuple, set, dict, str]
	myType = type(object)

	if myType not in type_lst:
		print("Type not found")
	elif myType is str:
		print(object, "is in the kitchen :", myType)
	else:
		print(myType.__name__.capitalize(),":", myType)
	return 42