def bold(func):
    def inner():
        return f"<b>{func()}</b>"
    return inner

def italic(func):
    def inner():
        return f"<i>{func()}</i>"
    return inner

@bold
@italic
def text():
    return "Hello"

print(text())
