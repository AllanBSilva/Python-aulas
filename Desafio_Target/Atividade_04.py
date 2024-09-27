# a)
seq_a = [1, 3, 5, 7]
next_a = seq_a[-1] + 2

# b)
seq_b = [2, 4, 8, 16, 32, 64]
next_b = seq_b[-1] * 2

# c)
seq_c = [0, 1, 4, 9, 16, 25, 36]
next_c = (len(seq_c)) ** 2

# d)
seq_d = [4, 16, 36, 64]
next_d = (len(seq_d) + 1) ** 2 * 4 

# e)
seq_e = [1, 1, 2, 3, 5, 8]
next_e = seq_e[-1] + seq_e[-2]

# f)
seq_f = [2, 10, 12, 16, 17, 18, 19]
next_f = 200

print("-" * 80)
print("Descubra a lógica e complete o próximo elemento:")
print("-" * 80)
print("Sequência a):", seq_a," "*14, "-> Próximo elemento:", next_a)
print("Sequência b):", seq_b," "*5, "-> Próximo elemento:", next_b)
print("Sequência c):", seq_c," "*2, "-> Próximo elemento:", next_c)
print("Sequência d):", seq_d," "*11, "-> Próximo elemento:", next_d)
print("Sequência e):", seq_e," "*8, "-> Próximo elemento:", next_e)
print("Sequência f):", seq_f, "-> Próximo elemento:", next_f,"\n")

