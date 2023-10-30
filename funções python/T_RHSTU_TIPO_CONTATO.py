from faker import Faker
import random
import pandas as pd
from datetime import date

dt_cadastro = date.today()
dt_fim = date.today()
dt_inicio = date.today()

fake = Faker()

registros = []

contador = 1  

while contador <= 10:  # Condição para gerar 100 registros
    id_tipo_contato = str(contador) 
    nm_tipo_contato = fake.random_element(elements=("Mãe", "Pai", "Prima(o)", "Irmã(o)", "Amiga(o)", "Colega de trabalho"))
    dt_inicio = fake.date()
    dt_fim = fake.date()
    dt_cadastro = fake.date()
    nm_usuario = fake.user_name()

    registro = {
        "ID_TIPO_CONTATO": id_tipo_contato,
        "NM_TIPO_CONTATO": nm_tipo_contato,
        "DT_INICIO": dt_inicio,
        "DT_FIM": dt_fim,
        "DT_CADASTRO": dt_cadastro,
        "NM_USUARIO": nm_usuario
    }

    registros.append(registro)
    contador += 1


df = pd.DataFrame(registros)


print(registros)