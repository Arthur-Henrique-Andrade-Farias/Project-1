with open("Gerador.txt", "r") as arquivo:
    xse, yse, xid, yid = map(int, arquivo.readline().split())
    while True:
        try:
            xs1, ys1, xi1, yi1 = map(int, arquivo.readline().split())
            xsf = min(xs1,xse)
            ysf = max(ys1,yse)
            xif = max(xi1,xid)
            yif = min(yi1,yid)
            xse = xsf 
            yse = ysf 
            xid = xif 
            yid = yif
        except ValueError:
            break
    print('1')
    print("({},{}), ({},{})".format(xse, yse, xid, yid))
