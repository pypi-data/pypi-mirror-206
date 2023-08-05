from importlib.metadata import version


class Info:
    def __init__(self):
        ver = version('libsrg')
        print(f"In version {ver} {__file__} ")


if __name__ == '__main__':
    Info()
