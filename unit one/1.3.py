"""
date: 2020/5/10
author: Z alert
title:　保留最后Ｎ个元素
question: 在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？
"""
from collections import deque
# deque 为双向队列 保留有限历史记录正是deque大显身手的时候
# 代码在多行上面做简单的文本匹配，并返回所在行的最后N行


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# Example use on a file
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'Python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
