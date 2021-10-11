def decor(typeof):
    def actual(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            if typeof == 'str':
                for _ in args:
                    _ = str(_)
                    print(type(_))
            elif typeof == 'int':
                for _ in args:
                    _ = int(_)
                    print(type(_))
            elif typeof == 'float':
                for _ in args:
                    _ = float(_)
                    print(type(_))
            elif typeof == 'tuple':
                for _ in args:
                    _ = tuple('_',)
                    print(type(_))
            elif typeof == 'list':
                for _ in args:
                    _ = list('_')
                    print(type(_))
        return wrapper
    return actual


@decor(typeof='list')
def somefunction(*args):
    return args


somefunction(1, 2, 3, 4, 5)
