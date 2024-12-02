


data = open('input.txt').read().strip().split("\n")
data = [list(map(int, x.strip().split(" "))) for x in data]

def less(a, b):
    return a<b
def more(a, b):
    return a>b
q = lambda a, b: abs(a-b)<=3

def safe1(l, f=None):
    if not f:
        if l[0]<l[1]:
            f = less
        elif l[0]>l[1]:
            f = more
        else:
            return False
    return all(f(a, b) and q(a, b) for a, b in zip(l, l[1:]))


def safe2(l):
    for i in range(len(l)):
        t = l[:]
        del t[i]
        if safe1(t):
            return True
    return False

def safe3(l):
    cl = 0
    cm = 0
    cq = 0
    il, im, iq = None, None, None
    for i, (a, b) in enumerate(zip(l, l[1:]), 1):
        if a>=b:
            cl += 1
            if not il:
                il = i
        if a<=b:
            cm += 1
            if not im:
                im = i
        if not q(a, b):
            cq += 1
            if not iq:
                iq = i
    if cq==0 and (cm==0 or cl==0):
        return True
    if cq>2 or cl>2 and cm>2:
        return False
    if cq==2:
        del l[iq]
        return safe1(l)
    if iq:
        t = l[:]
        del t[iq-1]
        del l[iq]
        return safe1(l) or safe1(t)
    if 0<cl<=2:
        t = l[:]
        del t[il-1]
        del l[il]
        return safe1(l) or safe1(t)
    if 0<cm<=2:
        t = l[:]
        del t[im-1]
        del l[im]
        return safe1(l) or safe1(t)
    return False

try:
    import pytest
        
    @pytest.mark.parametrize("l", data)
    def test_safe2_vs_safe3(l):
        assert safe2(l)==safe3(l)

    def test_len():
        assert all(len(x)>3 for x in data)
except:
    pass

if __name__ == "__main__":
    print(sum(1 for x in data if safe1(x)))
    print(sum(1 for x in data if safe3(x)))
