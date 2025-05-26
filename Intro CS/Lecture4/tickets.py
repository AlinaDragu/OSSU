#alyssa, ben and cindy are selling tickets to a fundraiser
#ben sells 20 fewer than alyssa
#cindy sells twice as many as alyssa
#1000 total tickets were sold by the three people
#how many did alyssa sell

#guess and check

for alyssa in range(1001):
    ben = max(alyssa-20,0)
    cindy = alyssa*2
    if ben + cindy + alyssa == 1000:
        print(f'Alyssa sold {alyssa} tickets')
        print(f'Ben sold {ben} tickets')
        print(f'Cindy sold {cindy} tickets')