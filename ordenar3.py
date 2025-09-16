"""
El programa lee los tres numeros dados por el usuario y los muestra de mayor a menor
"""

# Declaraciones


# Entradas
primer_num = int(input())
segundo_num = int(input())
tercer_num = int(input())

# Proceso
num_mayor = max(primer_num,segundo_num,tercer_num)
num_menor = min(primer_num,segundo_num,tercer_num)
num_en_medio = primer_num+segundo_num+tercer_num - num_mayor - num_menor

# Salidas
print(num_mayor,num_en_medio,num_menor)
