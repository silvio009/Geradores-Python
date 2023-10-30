from faker import Faker
import random
import pandas as pd
from datetime import date

fake = Faker()


registros = []

contador = 1  # Inicialize o contador com 1

while contador <= 2:  # Condição para gerar 100 registros
    id_paciente_ps = str(contador)  # ID crescente
    id_paciente = str(contador)
    id_plano_saude = str(contador)
    nr_carteira_ps = fake.unique.random_int(min=1000000, max=9999999, step=1)
    dt_inicio = fake.date()
    dt_fim = fake.date()
    nm_usuario = fake.name()
    dt_cadastro = fake.date()

    registro = {
        "ID_PACIENTE_PS": id_paciente_ps,
        "ID_PACIENTE": id_paciente,
        "ID_PLANO_SAUDE": id_plano_saude,
        "NR_CARTEIRA_PS": nr_carteira_ps,
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
