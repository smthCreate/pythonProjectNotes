import datetime
def identificator():
    tm = [int(x) for x in list(str(datetime.datetime.now().time()).replace(":","").replace(".",""))]
    ident = [str(tm[i]+tm[i-1]) for i in range(1,len(tm),2)]
    while len(ident)>5:
        ident = [str(ident[i]+ident[i-1]) for i in range(1,len(ident),2)]
    ident = "".join(ident)
    return ident

