from functools import wraps
from functools import reduce
import profile


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logit
def addition_func(x):
    """Do some math."""
    return x + x


def test_speed():
    a = ['a', 'b', 'c']*100

    def mapping():
        # fastest
        upperA = map(str.upper, a)
        print(list(upperA))

    def appending():
        # slowest
        upperA = []
        for i in a:
            upperA.append(str.upper(i))
        print(upperA)

    def appending2():
        # better
        upperA = []
        app = upperA.append
        for i in a:
            app(str.upper(i))
        print(upperA)

    mapping()
    appending()
    appending2()


if __name__ == '__main__':
    # print(addition_func(4))

    # a = []
    # app = a.append
    # for i in range(10):
    #     app(i)
    # print(a)

    # profile.run('test_speed()')

    a = [[1,2],[3,4]]
    print(list(reduce(lambda x, y: x + y, a)))

