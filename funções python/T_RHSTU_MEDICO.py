from faker import Faker
import pandas as pd
from datetime import date

fake = Faker()

registros = []

contador = 1  # Inicialize o contador com 1

while contador <= 2:  # Condição para gerar 2 registros
    id_func = str(contador)  # ID crescente
    nr_crm = str(fake.unique.random_int(min=10000, max=99999, step=1))  # Número de registro médico
    ds_especialidade = fake.random_element(elements=("Ginecologista", "Cardiologista", "Dermatologista", "Pediatra"))
    dt_cadastro = fake.date()
    nm_usuario = fake.user_name()

    registro = {
        "ID_FUNC": id_func,
        "NR_CRM": nr_crm,
        "DS_ESPECIALIDADE": ds_especialidade,
        "DT_CADASTRO": dt_cadastro,
        "NM_USUARIO": nm_usuario
    }

    registros.append(registro)
    contador += 1

# Criar um DataFrame Pandas com os registros
df = pd.DataFrame(registros)

# Imprimir os registros
print(registros)
