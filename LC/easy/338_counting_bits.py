def countBits(n: int) -> list[int]:
    x = []
    for i in range(n+1):
        x.append(i)
    
    y = list(map(lambda num: bin(num).count('1'), x))
    return y
    
x = countBits(2)