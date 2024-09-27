def count_a_in_string(s):
    s_lower = s.lower()
    count = s_lower.count('a')
    return count

print("-" * 80)
print("Vamos verificar a quantidade de letras 'a' que aparecem na string.")
print("-" * 80)
input_string = input("Informe uma string: ")

count = count_a_in_string(input_string)

if count > 0:
    print(f"\nA letra 'a' está contida na string digitada! Ocorre {count} vez(es) na string.")
else:
    print("\nA letra 'a' não ocorre na string digitada!")

print("-" * 80)
