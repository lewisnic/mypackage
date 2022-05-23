def try_me(string):
    if isinstance(string, str):
        reversed = string[::-1]
        return reversed
    else:
        return 'Please input a string'
