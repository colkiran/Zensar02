
def begin_end(fnc):
    def innerFun(*args):
        fnc(*args)

    return innerFun

