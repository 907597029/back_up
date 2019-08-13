low =1.4
high = 1.5
def sqrt2():
    global low
    global high
    while (high - low)>0.000000000000001:
        mid = (low + high)/2.0
        if mid * mid > 2.0:
            high = mid
        else:
            low = mid
        print(mid)

if __name__ == '__main__':
    sqrt2()
    print("end")
#1.4142135623731