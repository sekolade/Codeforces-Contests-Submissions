w_1,h_1,w_2,h_2=map(int,input().split())

if w_1 > w_2:
    t=(w_1-w_2)*h_2
    print((h_2+h_1+2)*(w_1+2)-t-w_1*h_1-w_2*h_2)
else:
    t=(w_2-w_1)*h_1
    print((h_1+h_2+2)*(w_2+2)-t-w_2*h_2-w_1*h_1)