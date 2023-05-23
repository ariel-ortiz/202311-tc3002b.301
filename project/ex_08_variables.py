from delta import Compiler, Phase


source = '''
var x, y, var;         // First statement
x = 2;
y = (x + 1) * 3;
var z;
z = y - 1;        // Last statement
x + y + z         // Resulting expression
'''

c = Compiler('program')
c.realize(source, Phase.SEMANTIC_ANALYSIS)
print()
# print(c.parse_tree_str)
print(c.symbol_table)
# print(c.wat_code)
# print()
# print(c.result)
