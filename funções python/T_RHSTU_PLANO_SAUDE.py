from faker import Faker
import random
import pandas as pd
from datetime import date

fake = Faker()


registros = []

contador = 1  # Inicialize o contador com 1

while contador <= 2:  # Condição para gerar 100 registros
    id_plano_saude = str(contador)  # ID crescente
    ds_razao_social = fake.company()
    nm_fantasia_plano_saude = fake.company_suffix()
    ds_plano_saude = fake.random_element(elements=("Plano Básico", "Plano Premium", "Plano Familiar"))
    nr_cnpj = fake.unique.random_int(min=10000000000000, max=99999999999999, step=1)
    nm_contato = fake.name()
    ds_telefone = fake.random_element(elements=("Medico", "Doutor","Enfermeira" ))
    dt_inicio = fake.date()
    dt_fim = fake.date()
    nm_usuario = fake.name()
    dt_cadastro = fake.date()

    registro = {
        "ID_PLANO_SAUDE": id_plano_saude,
        "DS_RAZAO_SOCIAL": ds_razao_social,
        "NM_FANTASIA_PLANO_SAUDE": nm_fantasia_plano_saude,
        "DS_PLANO_SAUDE": ds_plano_saude,
        "NR_CNPJ": nr_cnpj,
        "NM_CONTATO": nm_contato,
        "DS_TELEFONE": ds_telefone,
        "DT_INICIO": dt_inicio,
        "DT_FIM": dt_fim,
        "DT_CADASTRO": dt_cadastro,
        "NM_USUARIO": nm_usuario
    }

    registros.append(registro)
    contador += 1

# Criar um DataFrame Pandas com os registros
df = pd.DataFrame(registros)

# Imprimir os registros
print(registros)
