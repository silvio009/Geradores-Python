from faker import Faker
import random
import pandas as pd
from datetime import date

fake = Faker()

registros = []

contador = 1  # Inicialize o contador com 1

while contador <= 2:  # Condição para gerar 2 registros
    id_paciente = str(contador)  # ID crescente
    id_telefone = str(contador)  # ID crescente
    nr_ddi = "+55"  
    nr_ddd = "0" + str(fake.random_int(min=10, max=99, step=1))  
    nr_telefone = str(fake.random_int(min=20000000, max=999999999, step=1)) 
    tp_telefone = fake.random_element(elements=("Comercial", "Residencial", "Recado", "Celular"))
    st_telefone = fake.random_element(elements=("A", "I"))
    dt_cadastro = fake.date()
    nm_usuario = fake.user_name()

    registro = {
        "ID_PACIENTE": id_paciente,
        "ID_TELEFONE": id_telefone,
        "NR_DDI": nr_ddi,
        "NR_DDD": nr_ddd,
        "NR_TELEFONE": nr_telefone,
        "TP_TELEFONE": tp_telefone,
        "ST_TELEFONE": st_telefone,
        "DT_CADASTRO": dt_cadastro,
        "NM_USUARIO": nm_usuario
    }

    registros.append(registro)
    contador += 1

# Criar um DataFrame Pandas com os registros
df = pd.DataFrame(registros)

# Imprimir os registros
print(registros)
