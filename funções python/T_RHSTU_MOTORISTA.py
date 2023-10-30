from faker import Faker
import pandas as pd
from datetime import date

fake = Faker()

registros = []

contador = 1  # Inicialize o contador com 1

while contador <= 2:  # Condição para gerar 2 registros
    id_func = str(contador)  # ID crescente
    nr_cnh =  str(fake.unique.random_int(min=10000000000, max=99999999999, step=1))  # Número de CNH do Brasil
    nm_categoria_cnh = fake.random_element(elements=("A", "B", "C", "D", "E"))  # Categoria da CNH
    dt_validade_cnh = fake.date() # Data de validade da CNH
    dt_cadastro = fake.date()
    nm_usuario = fake.user_name()

    registro = {
        "ID_FUNC": id_func,
        "NR_CNH": nr_cnh,
        "NM_CATEGORIA_CNH": nm_categoria_cnh,
        "DT_VALIDADE_CNH": dt_validade_cnh,
        "DT_CADASTRO": dt_cadastro,
        "NM_USUARIO": nm_usuario
    }

    registros.append(registro)
    contador += 1

# Criar um DataFrame Pandas com os registros
df = pd.DataFrame(registros)

# Imprimir os registros
print(registros)
