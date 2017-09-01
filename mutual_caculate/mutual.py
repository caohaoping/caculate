# encoding:utf-8

import math


def get_participle():
    print('get participle')
    f = open('../data/input.txt', 'r')
    s = set()
    while True:
        line = f.readline()
        if not line:
            break
        ps = line[0:-2]
        ps = ps.split()
        for p in ps:
            if p not in s:
                s.add(p)
    f.close()
    return s


def get_relativity(ps, c):
    print('get relativity')
    d = dict()

    for p in ps:
        is_line = True
        A = 0.0
        B = 0.0
        C = 0.0
        N = 0.0
        f = open('../data/input.txt', 'r')
        while is_line:
            line = f.readline()
            if not line:
                is_line = False
            if is_line:
                N += 1.0
                if line[-2:-1] == c:
                    if p in line:
                        A += 1.0
                    else:
                        C += 1.0
                else:
                    if p in line:
                        B += 1.0
        f.close()
        D = (A + C) * (A + B)
        if D != 0:
            E = (A * N / D)
            if E != 0:
                i = math.log10(E)
                d[p] = i

    return d


if __name__ == '__main__':
    # 提取分词
    participles = get_participle()
    print('set: ', participles.__len__(), participles)

    # 1计算相关度并排序
    data = get_relativity(participles, '1')
    data1 = sorted(data.items(), key=lambda d: d[1], reverse=True)
    out_file = open('../data/output1.txt', 'w')
    out_file.write(data1.__str__())
    out_file.close()
    # 打印分词及相关度
    print('data1', data1.__len__(), data1)

    # 0计算相关度并排序
    data = get_relativity(participles, '0')
    data0 = sorted(data.items(), key=lambda d: d[1], reverse=True)
    out_file = open('../data/output0.txt', 'w')
    out_file.write(data0.__str__())
    out_file.close()
    # 打印分词及相关度
    print('data0', data0.__len__(), data0)
