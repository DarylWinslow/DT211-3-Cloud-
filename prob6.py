def main():
    n = 100
    sum1, sum2 =0, 0
    for i in range(1, n+1):
        sum1 += 1
        sum2 += pow(i,2)
    return pow(sum1,2) -sum2

if '__main__' == __name__:
    print(main())
