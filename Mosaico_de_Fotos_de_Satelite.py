r = 0
xir = 0
yir = 0
xfr = 0
yfr = 0
x = "sim"
while x == "sim":
    npr = int(input())
    for t in range(npr):
        xi,yi,xf,yf = map(int,input().split())
        xi1,yi1,xf1,yf1 = map(int, input().split())
        if xi1 >= xi and xi1 <= xf1 and yi1 <= yi and yi1 >= yf and xf1 > xf and yf1 <= yi and yf1 >= yf:
            xfr = xf1
            yfr = yf
            yir = yi
            xir = xi
            r += 1
    print("{}\n({},{}) ({},{})".format(r,xir, yir, xfr, yfr))
    x = input("Deseja adicionar mais alguma área?(sim ou nao)\n")
