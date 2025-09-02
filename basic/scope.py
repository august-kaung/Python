g = "This is global variable."

def func():
    global g
    g = "This is local variable."
    en = "This is local variable eeeee."
    print(g)
     
    def innerFunc():
        l = "This is real local variable."
        nonlocal en
        en = "This is real local variable from inner function."
        print(l)
        print(f"en from innerFunc: {en}")
    print(en)
    innerFunc()

func()
 
print(g)