from faker import Faker
import random
import pandas as pd
from datetime import date

fake = Faker()

registros = []

contador = 1  # Inicialize o contador com 1

while contador <= 2:  # Condição para gerar 2 registros
    id_email = str(contador)  # ID crescente
    id_paciente = str(contador)
    ds_email = fake.email()
    tp_email = fake.random_element(elements=("Pessoal", "Profissional"))
    st_email = fake.random_element(elements=("A", "I"))
    dt_cadastro = fake.date()
    nm_usuario = fake.user_name()

    registro = {
        "ID_EMAIL": id_email,
        "ID_PACIENTE": id_paciente,
        "DS_EMAIL": ds_email,
        "TP_EMAIL": tp_email,
        "ST_EMAIL": st_email,
        "DT_CADASTRO": dt_cadastro,
        "NM_USUARIO": nm_usuario
    }

    registros.append(registro)
    contador += 1

# Criar um DataFrame Pandas com os registros
df = pd.DataFrame(registros)

# Imprimir os registros
print(registros)
