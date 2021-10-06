def debug_control(*args,**kwargs):
    ints=0
    strs=0
    floats=0
    for i in args:
        if isinstance(i,int):
            ints+=1
        elif isinstance(i,float):
            floats+=1
        elif isinstance(i,str):
            strs+=1
    for i in kwargs:
        if isinstance(i,int):
            ints+=1
        elif isinstance(i,float):
            floats+=1
        elif isinstance(i,str):
            strs+=1
    return f"str: {strs} int: {ints} float: {floats}"
