import itertools


SYMETRIC_1 = ('0', '1', '8')
SYMETRIC_2 = {
    '0': '0',
    '1': '1',
    '6': '9',
    '8': '8',
    '9': '6'
}

TEST_39 = ['0', '1', '8', '11', '69', '88', '96', '101', '111', '181', '609', '619', '689', '808', '818', '888', '906', '916', '986', '1001', '1111', '1691', '1881', '1961', '6009', '6119', '6699', '6889', '6969', '8008', '8118', '8698', '8888', '8968', '9006', '9116', '9696', '9886', '9966']

def is_symmetric(s):
    if s[0] == '0' and s != ('0', ):
        return False

    for i in range(len(s) // 2):
        if SYMETRIC_2[s[i]] != s[-1 - i]:
            return False

    if len(s) % 2 == 1:
        if s[len(s) // 2] not in SYMETRIC_1:
            return False
        else:
            return True
    else:
        return True

def generator():
    i = 1
    while True:
        c = itertools.product('01689', repeat=i)
        for elem in c:
            if is_symmetric(elem):
                yield ''.join(elem)
        i += 1


"""
def num_gen(n):
    lista = []
    iter = generator()
    for i in range(n):
        lista.append(next(iter))
    return lista
"""


#for i, n in enumerate(generator()):
#    print(i+1, n)


iter = generator()

n = [next(iter) for _x in range(39)]


# print(num_gen(1000))
assert generator()[:39] == TEST_39
# assert is_symmetric(('9', '6'))

