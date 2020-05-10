"""
1、星号表达式基础应用
date: 2020/5/10
author: Z alert
"""
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name)             # 'Dave'
print(email)            # 'dace@example.com'
print(phone_numbers)    # ['773-555-1212', '847-555-1212'] 变量永远是列表类型

"""
2、星号表达式在迭代元素为可变长元祖的序列时是很有用的
"""
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print("bar", s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

"""
3、星号表达式用于字符串的分割
"""
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
u_name, *fields, homedir, sh = line.split(':')
# 丢弃元素
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)     # 'ACME'
print(year)     # '2012'
# 切割列表
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)     # '1'
print(tail)     # [10, 7, 4, 5, 9]

