

def powersum(power,*args):
    ''' Return the sum of each raised to the specified power.'''

    total=0

    for i in args:
        total+=pow(i,power)
    return total

print(powersum(2,3,4))