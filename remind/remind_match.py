# encoding:utf-8


def replace_mind():
    out_file = open('../data/remind_output.txt', 'w')
    for line in open('../data/remind_data.txt', 'r'):
        if '周一到周五' '七点' in line:
            line4 = line.replace('周一到周五', '周一至周五')
            out_file.write(line4)

    out_file.close()


if __name__ == '__main__':
    replace_mind()
