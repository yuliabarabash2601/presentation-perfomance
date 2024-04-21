from timeit import repeat

setup = """
a = "sss"
b = "ssss"
"""
timestame_f = """
c = f"A message with {a}{b}"
"""
print(repeat(stmt=timestame_f, setup=setup, number=1000000, repeat=8))
