def ft_map(function_to_apply, list_of_inputs):
    tmp = []
    for i in list_of_inputs:
        tmp.append(function_to_apply(i))
    return tmp
    pass
