ft_list  = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set   = {"Hello", "tutu!"}
ft_dict  = {"Hello" : "titi!"}

# list 
ft_list[1] = "World!"

# tuple
ft_tuple_lst= list(ft_tuple)
ft_tuple_lst[1] = "France!"
ft_tuple = tuple(ft_tuple_lst)

# set
ft_set.remove("tutu!")
ft_set.add("Paris!")

# dict
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)