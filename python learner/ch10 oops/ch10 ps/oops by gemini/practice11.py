class parent:
    def __init__(self):
        print("i am a parent")

class child(parent):
    def __init__(self):
        super().__init__()
        print("i am a child")

a = child()
# print(a.car, a.mycar)