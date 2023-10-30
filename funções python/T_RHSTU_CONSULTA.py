from faker import Faker
import pandas as pd
from datetime import date

fake = Faker()

registros = []

contador = 1  # Inicialize o contador com 1

while contador <= 2:  # Condição para gerar 2 registros
    id_unid_hospital = str(contador)  # ID crescente
    id_consulta = str(contador)  # ID crescente
    id_paciente = str(contador)  # ID crescente
    id_func = str(contador)  # ID crescente
    dt_hr_consulta = fake.date()
    nr_consultorio = str(fake.random_int(min=1, max=1000, step=1))
    dt_cadastro = fake.date()
    nm_usuario = fake.user_name()

    registro = {
        "ID_UNID_HOSPITAL": id_unid_hospital,
        "ID_CONSULTA": id_consulta,
        "ID_PACIENTE": id_paciente,
        "ID_FUNC": id_func,
        "DT_HR_CONSULTA": dt_hr_consulta,
        "NR_CONSULTORIO": nr_consultorio,
        "DT_CADASTRO": dt_cadastro,
        "NM_USUARIO": nm_usuario
    }

    registros.append(registro)
    contador += 1

# Criar um DataFrame Pandas com os registros
df = pd.DataFrame(registros)

# Imprimir os registros
print(registros)
