class StartStop:

    def __init__(self, fnc):
        self.fnc = fnc


    def __call__(self, *args):
        self.fnc(*args)