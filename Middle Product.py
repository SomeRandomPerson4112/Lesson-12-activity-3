num = int(input("Enter a 4 or more digit number: "))
t = num
numLen = 0

while t > 0:
    numLen += 1
    t = t // 10

if numLen >= 4:
    halfLen = numLen // 2
    chk = 0
    mid1, mid2 = None, None  
    
    while num > 0:
        rem = num % 10
        if chk == halfLen:
            mid1 = rem
        elif chk == (halfLen - 1):
            mid2 = rem
        num = num // 10
        chk += 1
    
    # Ensure mid1 and mid2 are found
    if mid1 is not None and mid2 is not None:
        prod = mid1 * mid2
        print(f"Product of mid digits {mid1} * {mid2} = {prod}")
    else:
        print("ERROR: Couldn't determine middle digits!")
else:
    print("ERROR: Number must have 4 or more digits!")

