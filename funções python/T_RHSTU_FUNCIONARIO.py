from faker import Faker
import pandas as pd
from datetime import date
import random

fake = Faker()

registros = []

contador = 1  # Inicialize o contador com 1

while contador <= 2:  # Condição para gerar 2 registros
    id_func = str(contador)  # ID crescente
    id_superior = str(contador)  # ID de um superior aleatório
    nm_func = fake.name()
    ds_cargo = fake.random_element(elements=("Faxineiro", "Entregador", "Recepcionista", "Balconista"))
    dt_nascimento = fake.date()
    vl_salario = round(random.uniform(1500, 5000), 2)  # Salário em reais
    nr_rg = str(fake.random_int(min=1000000, max=9999999, step=1))
    nr_cpf = fake.unique.random_int(min=10000000000, max=99999999999, step=1)
    st_func = fake.random_element(elements=("A", "I"))
    dt_cadastro = fake.date()
    nm_usuario = fake.user_name()

    registro = {
        "ID_FUNC": id_func,
        "ID_SUPERIOR": id_superior,
        "NM_FUNC": nm_func,
        "DS_CARGO": ds_cargo,
        "DT_NASCIMENTO": dt_nascimento,
        "VL_SALARIO": vl_salario,
        "NR_RG": nr_rg,
        "NR_CPF": nr_cpf,
        "ST_FUNC": st_func,
        "DT_CADASTRO": dt_cadastro,
        "NM_USUARIO": nm_usuario
    }

    registros.append(registro)
    contador += 1

# Criar um DataFrame Pandas com os registros
df = pd.DataFrame(registros)

# Imprimir os registros
print(registros)
