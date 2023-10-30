from faker import Faker
import pandas as pd
from datetime import date

fake = Faker()

registros = []

contador = 1  # Inicialize o contador com 1

while contador <= 2:  # Condição para gerar 2 registros
    id_paciente = str(contador)  # ID crescente
    id_contato = str(contador)  # ID crescente
    id_tipo_contato = str(contador)
    nm_contato = fake.name()
    nr_ddi = "+55"  # DDI do Brasil
    nr_ddd = "0" + str(fake.random_int(min=10, max=99, step=1))  # DDD do Brasil
    nr_telefone = "9" + str(fake.random_int(min=900000000, max=999999999, step=1))  # Número de telefone do Brasil
    dt_cadastro = fake.date()
    nm_usuario = fake.user_name()

    registro = {
        "ID_PACIENTE": id_paciente,
        "ID_CONTATO": id_contato,
        "ID_TIPO_CONTATO": id_tipo_contato,
        "NM_CONTATO": nm_contato,
        "NR_DDI": nr_ddi,
        "NR_DDD": nr_ddd,
        "NR_TELEFONE": nr_telefone,
        "DT_CADASTRO": dt_cadastro,
        "NM_USUARIO": nm_usuario
    }

    registros.append(registro)
    contador += 1

# Criar um DataFrame Pandas com os registros
df = pd.DataFrame(registros)

# Imprimir os registros
print(registros)
