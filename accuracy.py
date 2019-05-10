f = open('20171066_20171062.txt', "r")
right = 0
total = 0
for x in f:
    total += 1
    s = x.split(' ')
    frame = s[0].split('_')
    slide = s[1].split('_')
    if(slide[0] == frame[0] and slide[1] == frame[1]):
        right += 1
    else:
        print(x)
        print("wrong")
print(right, "/", total)
