from timeit import repeat

setup = """
a = 1
b = 2
k = 3
d = 4
p = 5
s = 6
t = 7
w = 8
x = 9
l = 10
m = 11
n = 12
o = 13
a_1 = 1
b_1 = 2
k_1 = 3
d_1 = 4
p_1 = 5
s_1 = 6
t_1 = 7
w_1 = 8
x_1 = 9
"""
timestame_f = """
for i in range(10 ** 7):
    c = a + b + k + p + s + d
"""
print(repeat(stmt=timestame_f, setup=setup, number=1, repeat=8))
