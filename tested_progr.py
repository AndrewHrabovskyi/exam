

def main(n):
    r = 5
    for i in range(n):
        r+=2
    return r

if __name__ == '__main__':
    print(main(1))
    print(main(3))
    print(main(5))
    print(main(2.2))
    print(main([5,4]))
    print(main("aaaa"))
