def read_int():
    return int(raw_input())

def solve():
    size = read_int()
    for i in range(size):
        lis_size = read_int()
        lis = []
        for x in range(lis_size - 1):
            lis.insert(x, read_int())
        frm,to = kadane(lis)
        if frm == -1:
            print "Route %d has no nice parts" % (i)
        else:
            print "The nicest part of route %d is between stops %d and %d" % ((i + 1), frm, to)

def kadane(lis):
    print "list : "
    print lis
    max_ = 0
    sum_till_now = 0
    frm, to = 0, 0
    max_frm, max_to  = -1, -1
    first_time = True
    for i in range(len(lis)):
        if lis[i] + sum_till_now > 0:
            if first_time:
                frm = i
            else:
                to = i
            sum_till_now += lis[i]
        else:
            if sum_till_now > max_:
                max_ = sum_till_now
                max_frm = frm
                max_to = to_
            sum_till_now = 0
    return max_frm, max_to

if __name__ == '__main__':
    print 'coming'
    solve()
