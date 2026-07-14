class Overload:
    def show(self, *args):
        if len(args)==1:
            print(f"one argument is {args[0]}")
        elif len(args)==2:
            print(f"two args are {args[0]},{args[1]} ")
        else:
            print("inavlid type of argument")
ov=Overload()
ov.show(1)
ov.show(1,2)
ov.show(1,2,3)
