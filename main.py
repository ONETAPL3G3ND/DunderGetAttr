class test:
    def __init__(self):
        self.a = "a"
        self.b = "b"

    def __getattr__(self, item):
        raise Exception

if __name__ == "__main__":
    t = test()
    print(t.a)
    print(t.b)
    print(t.c)