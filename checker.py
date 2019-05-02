f = open('20171066_20171062.txt', "r")
for x in f:
    s = x.split(' ')
    frame = s[0].split('_')
    slide = s[1].split('_')
    if(slide[0] == frame[0] and slide[1] == frame[1]):
        continue
    else:
        print(x)
        print("wrong")
