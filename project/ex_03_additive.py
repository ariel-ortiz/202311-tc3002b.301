from delta import Compiler, Phase


source = '1 + 2 - 1 - 2 + 5'

c = Compiler('program')
c.realize(source, Phase.EVALUATION)
print()
# print(c.parse_tree_str)
# print()
print(c.wat_code)
print()
print(c.result)
