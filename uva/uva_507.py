def read_int():
    try:
        return int(input())
    except EOFError:
        exit(0)


def solve():
    size = read_int()
    for i in range(size):
        lis_size = read_int()
        lis = []
        for x in range(lis_size - 1):
            lis.insert(x, read_int())
        frm, to = kadane(lis)
        if frm == -1:
            print("Route {0} has no nice parts".format(i + 1))
        else:
            print("The nicest part of route {0} is between stops {1} and {2}".format((i + 1), (frm + 1), (to + 2)))


def kadane(lis):
    max_ = 0
    sum_till_now = 0
    frm, to = -1, -1
    max_frm, max_to = -1, -1
    first_time = True
    for i in range(len(lis)):
        zz = lis[i] + sum_till_now
        if zz > 0:
            if first_time:
                frm = i
                first_time = False

            if zz >= max_:
                to = i
                if (max_frm == -1 and max_to == -1) or (to - frm > max_to - max_frm) or (zz > max_):
                    max_frm = frm
                    max_to = to
                max_ = zz
        sum_till_now += lis[i]

        if sum_till_now < 0:
            sum_till_now = 0
            first_time = True

    return max_frm, max_to


if __name__ == '__main__':
    solve()
