#Lab #8
#Due Date: 04/24/2021, 11:59PM
'''
# Collaboration Statement:

'''

def mulDigits(num, fn):
    '''
        >>> isTwo = lambda num: num == 2
        >>> mulDigits(5724892472, isTwo)
        8
        >>> def divByFour(num):
        ...     return not num%4
        ...
        >>> mulDigits(5724892472, divByFour)
        128
        >>> mulDigits(155794, isTwo)
        1
        >>> mulDigits(67945125482222152, isTwo)
        64
        >>> mulDigits(679451254828822152, divByFour)
        8192
    '''
    value = 1
    temp = num
    while temp > 0:
        val = temp % 10
        if fn(val):
            value *= val
        temp = temp // 10
    return value




def getCount(x):
    '''
        >>> getCount(6)(62156)
        2
        >>> digit = getCount(7)
        >>> digit(9457845778457077076)
        7
        >>> digit(-945784578457077076)
        6
        >>> getCount(6)(-65062156)
        3
    '''
    def Count(num):
        temp = num
        nonlocal x
        if num < 0:
            num *= -1
        count = 0
        while num != 0:
            digit = num % 10
            num = num // 10
            if digit == x:
                count += 1
        return count
    return Count





def genAccum(seq, fn):
    '''
        >>> add = lambda x, y: x + y
        >>> mul = lambda x, y: x * y
        >>> type(genAccum([7, 2, 3, 4, 5, 6, 7, 8, 9, 10], add))
        <class 'generator'>
        >>> list(genAccum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], add))
        [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        >>> list(genAccum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], mul))
        [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
        >>> list(genAccum([7, 2, 3, 4, 5, 6, 7, 8, 9, 10], add))
        [7, 9, 12, 16, 21, 27, 34, 42, 51, 61]
        >>> list(genAccum([2.5, 2, 3, 4, 5, 0, 7, 8, 9, 10], mul))
        [2.5, 5.0, 15.0, 60.0, 300.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        >>> list(genAccum([0, 2, 3, 4, 5, 6, 7, 8, 9, 10], mul))
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        >>> list(genAccum([1, 2, 3, 4, 5, 0, 7, 8, 9, 10], mul))
        [1, 2, 6, 24, 120, 0, 0, 0, 0, 0]
    '''
    if len(seq) > 0:
        yield seq[0]
    itr = iter(seq)
    running = fn(next(itr), next(itr))
    yield running
    for i in itr:
        running = fn(running, i)
        yield running
