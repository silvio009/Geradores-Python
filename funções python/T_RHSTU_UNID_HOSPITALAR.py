from faker import Faker
import pandas as pd
from datetime import date

fake = Faker()

registros = []

contador = 1  # Inicialize o contador com 1

while contador <= 2:  # Condição para gerar 2 registros
    id_unid_hospital = str(contador)  # ID crescente
    nm_unid_hospitalar = fake.company()
    nm_razao_social_unid_hosp = fake.company_suffix()
    dt_fundacao = fake.date()  # Data de fundação
    nr_logradouro = fake.street_address()  # Logradouro do Brasil
    ds_complemento_numero = fake.building_number()
    ds_ponto_referencia = fake.street_name()  # Ponto de referência do Brasil
    dt_inicio = fake.date()  # Data de início
    dt_termino = fake.date() # Data de término
    dt_cadastro = fake.date()
    nm_usuario = fake.user_name()

    registro = {
        "ID_UNID_HOSPITAL": id_unid_hospital,
        "NM_UNID_HOSPITALAR": nm_unid_hospitalar,
        "NM_RAZAO_SOCIAL_UNID_HOSP": nm_razao_social_unid_hosp,
        "DT_FUNDACAO": dt_fundacao,
        "NR_LOGRADOURO": nr_logradouro,
        "DS_COMPLEMENTO_NUMERO": ds_complemento_numero,
        "DS_PONTO_REFERENCIA": ds_ponto_referencia,
        "DT_INICIO": dt_inicio,
        "DT_TERMINO": dt_termino,
        "DT_CADASTRO": dt_cadastro,
        "NM_USUARIO": nm_usuario
    }

    registros.append(registro)
    contador += 1

# Criar um DataFrame Pandas com os registros
df = pd.DataFrame(registros)

# Imprimir os registros
print(registros)
