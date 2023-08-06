import os


def desktop(name=''):
    return os.path.join(os.path.expanduser("~"), 'Desktop', name)
