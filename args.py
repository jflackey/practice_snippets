def test_var_args(f_arg, *args):
    print("first arg:", f_arg)
    for arg in args:
        print("another arg in *args:", arg)

test_var_args('arg1', 'arg2', 'arg3', 'arg4')
