a = "AAA"
b = "BBB"
c = 1.1

# string = 'a={} b={} c={:.2f}'
string = 'a={1} b={0} c={2:.2f}' #adicionando índices
formato = string.format(a,b,c)
print(formato)
