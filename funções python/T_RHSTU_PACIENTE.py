from faker import Faker
import random
import pandas as pd
from datetime import date

fake = Faker()

registros = []

contador = 1  # Inicialize o contador com 1

while contador <= 1000:  # Condição para gerar 1000 registros
    id_paciente = str(contador)  # ID crescente
    nm_paciente = fake.name()
    nr_cpf = fake.unique.random_int(min=10000000000, max=99999999999, step=1)
    nm_rg = str(fake.random_int(min=1000000, max=9999999, step=1))
    dt_nascimento = fake.date()
    fl_sexo_biologico = fake.random_element(elements=("M", "F" , "I"))
    ds_escolaridade = fake.random_element(elements=("Ensino Fundamental", "Ensino Médio", "Ensino Superior"))
    ds_estado_civil = fake.random_element(elements=("Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viúvo(a)"))
    nm_grupo_sanguineo = fake.random_element(elements=("A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"))
    nr_altura = round(random.uniform(1.50, 2.00), 2) 
    nr_peso = round(random.uniform(40, 120), 2) 
    dt_cadastro = fake.date()
    nm_usuario = fake.user_name()

    registro = {
        "ID_PACIENTE": id_paciente,
        "NM_PACIENTE": nm_paciente,
        "NR_CPF": nr_cpf,
        "NM_RG": nm_rg,
        "DT_NASCIMENTO": dt_nascimento,
        "FL_SEXO_BIOLOGICO": fl_sexo_biologico,
        "DS_ESCOLARIDADE": ds_escolaridade,
        "DS_ESTADO_CIVIL": ds_estado_civil,
        "NM_GRUPO_SANGUINEO": nm_grupo_sanguineo,
        "NR_ALTURA": nr_altura,
        "NR_PESO": nr_peso,
        "DT_CADASTRO": dt_cadastro,
        "NM_USUARIO": nm_usuario
    }

    registros.append(registro)
    contador += 1


df = pd.DataFrame(registros)


print(registros)