def log(func):
    def wrapper(*args, **kw):
        print('call %s()' % func)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2019')

now = log(now)
now()