from timeit import repeat

setup = """
a = "Hello "
b = "World"
"""
timestame_f = """
c = f"MSG: " + a + b
"""
print(repeat(stmt=timestame_f, setup=setup, number=1000000, repeat=8))
