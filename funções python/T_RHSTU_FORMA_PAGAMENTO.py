from faker import Faker
import pandas as pd
from datetime import date

fake = Faker()

registros = []

contador = 1  # Inicialize o contador com 1

while contador <= 2:  # Condição para gerar 2 registros
    id_forma_pagto = str(contador)  # ID crescente
    nm_forma_pagto = fake.random_element(elements=("Cartão de Crédito", "Dinheiro", "Boleto Bancário"))
    ds_forma_pagto = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
    st_forma_pagto = fake.random_element(elements=("A", "I"))
    dt_cadastro = fake.date()
    nm_usuario = fake.user_name()

    registro = {
        "ID_FORMA_PAGTO": id_forma_pagto,
        "NM_FORMA_PAGTO": nm_forma_pagto,
        "DS_FORMA_PAGTO": ds_forma_pagto,
        "ST_FORMA_PAGTO": st_forma_pagto,
        "DT_CADASTRO": dt_cadastro,
        "NM_USUARIO": nm_usuario
    }

    registros.append(registro)
    contador += 1

# Criar um DataFrame Pandas com os registros
df = pd.DataFrame(registros)

# Imprimir os registros
print(registros)
