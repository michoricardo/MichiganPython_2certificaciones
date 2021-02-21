score = input("Enter Score: ")
s=float(score)
if s>0 and s<=1:
    if s==.9:
        print('A')
    elif s==.8:
        print('B')
    elif s==.7:
        print('C')
    elif s==.6:
        print('D')
    elif s<.6:
        print('F')