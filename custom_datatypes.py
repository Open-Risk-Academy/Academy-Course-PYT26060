class URL(object):
    def __init__(self, value):
        self.value = value


def parser(s):
    return URL(s)


def unparser(x):
    return x.value
