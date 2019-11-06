def ft_filter(function_to_apply, list_of_inputs):
    tmp = []
    for i in list_of_inputs:
        if function_to_apply(i):
            tmp.append(i)
    return tmp
