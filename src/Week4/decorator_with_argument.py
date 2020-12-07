from functools import wraps


def make_html(element):
    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{element}>{func(*args, **kwargs)}</{element}>'
        return wrapper
    return real_decorator


@make_html('p')
@make_html('strong')
def foo(text="Hello"):
    return f"{text}"

print(foo())





