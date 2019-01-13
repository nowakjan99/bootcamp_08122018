def bold(funkcja):
    def wrapper1(*args, **kwargs):
        return f'<b>{funkcja(*args, **kwargs)}</b>'
    return wrapper1

def italic(funkcja):
    def wrapper2(*args, **kwargs):
        return f'<i>{funkcja(*args, **kwargs)}</i>'
    return wrapper2

@bold
@italic

def foo(arg):
    return f'To jest {arg}'

def test_decorated_foo():
    assert foo("x") == "<b><i>To jest x</i></b>"