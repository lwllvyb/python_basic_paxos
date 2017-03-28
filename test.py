from __future__ import print_function


class Test(object):
    def __init__(self):
        self.test = {"100": {}}

    def fun1(self):
        for port, value in self.test.items():
            value["hello"] = "123"
    def fun2(self):
        print (self.test)


t = Test()
t.fun1()
t.fun2()