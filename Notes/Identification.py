import datetime
def identificator():
    tm = [int(x) for x in list(str(datetime.datetime.now().time()).replace(":","").replace(".",""))]
    print(tm)
    ident = "".join([str(tm[i]+tm[i-1]) for i in range(1,len(tm),2)])
    return ident

