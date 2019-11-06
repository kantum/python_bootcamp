def ft_reduce(function_to_apply, list_of_inputs):
    if len(list_of_inputs) == 0:
        return None
    tmp = list_of_inputs[0]
    for i in range(1, len(list_of_inputs)):
        tmp = function_to_apply(tmp, list_of_inputs[i])
    return tmp
