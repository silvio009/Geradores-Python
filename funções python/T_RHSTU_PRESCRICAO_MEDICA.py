from faker import Faker
import random
import pandas as pd
from datetime import date

fake = Faker()

dt_cadastro = date.today()

registros = []

contador = 1  # Inicialize o contador com 1

while contador <= 100:  # Condição para gerar 100 registros
    id_prescricao_medica = int(contador)  # ID crescente
    id_unid_hospital = int(contador)
    id_consulta =int(contador)
    id_medicamento = int(contador)
    ds_posologia = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
    ds_via = fake.random_element(elements=("Oral", "Injeção", "Tópica", "Inalatória"))
    ds_observacao_uso = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
    qt_medicamento = fake.random_int(min=1, max=10, step=1)
    nm_usuario = fake.name()
    dt_cadastro = fake.date()

    registro = {
        "ID_PRESCRICAO_MEDICA": id_prescricao_medica,
        "ID_UNID_HOSPITAL": id_unid_hospital,
        "ID_CONSULTA": id_consulta,
        "ID_MEDICAMENTO": id_medicamento,
        "DS_POSOLOGIA": ds_posologia,
        "DS_VIA": ds_via,
        "DS_OBSERVACAO_USO": ds_observacao_uso,
        "QT_MEDICAMENTO": qt_medicamento,
        "DT_CADASTRO": dt_cadastro,
        "NM_USUARIO": nm_usuario
    }

    registros.append(registro)
    contador += 1

# Criar um DataFrame Pandas com os registros
df = pd.DataFrame(registros)

# Imprimir os registros
print(registros)
