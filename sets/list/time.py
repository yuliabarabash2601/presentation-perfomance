from timeit import repeat

setup = """
a = [4,2,1,5,6,3,7,8,9,14,20,11,76,34]
"""
timestame_f = """
c = add(a, b, d, k, p, s)
"""
print(repeat(stmt=timestame_f, setup=setup, number=1, repeat=8))
