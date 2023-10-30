from faker import Faker
import random
import pandas as pd
from datetime import date

fake = Faker()

dt_cadastro = date.today()

registros = []

contador = 0

medicamentos = [
    "Paracetamol", "Aspirina", "Ibuprofeno", "Amoxicilina", "Omeprazol",
    "Atorvastatina", "Insulina", "Losartan", "Morfina", "Penicilina",
    "Lisinopril", "Metformina", "Simvastatina", "Albuterol", "Warfarina",
    "Ranitidina", "Diazepam", "Atenolol", "Fluoxetina", "Ritalina",
    "Metotrexato", "Levotiroxina", "Naproxeno", "Zolpidem", "Furosemida",
    "Ciprofloxacino", "Cetirizina", "Risperidona", "Metronidazol", "Prednisona",
    "Doxiciclina", "Loratadina", "Clonazepam", "Fenitoína", "Rivastigmina",
    "Naloxona", "Fentanil", "Carvedilol", "Amitriptilina", "Tamsulosina",
    "Cefalexina", "Duloxetina", "Metoclopramida", "Bisoprolol", "Budesonida",
    "Pregabalina", "Sertralina", "Acetaminofeno", "Ciclobenzaprina", "Ondansetrona",
    "Lansoprazol", "Hidroclorotiazida", "Escitalopram", "Lamotrigina", "Ranitidina",
    "Sinvastatina", "Digoxina", "Clindamicina", "Venlafaxina", "Rosuvastatina",
    "Sildenafil", "Tadalafil", "Montelucaste", "Salmeterol", "Vitamina D",
    "Dipirona", "Ceftriaxona", "Fexofenadina", "Dexametasona", "Levodopa",
    "Clorpromazina", "Metformina", "Metronidazol", "Loperamida", "Rifampicina",
    "Fluconazol", "Oxicodona", "Levozine", "Mirtazapina", "Lactulose",
    "Atropina", "Betametasona", "Pramipexol", "Levetiracetam", "Latanoprosta",
    "Naproxeno Sódico", "Dextrometorfano", "Ivermectina", "Dabigatrana", "Valsartana",
    "Donepezila", "Nifedipina", "Clortalidona", "Losartana Potássica", "Esomeprazol",
    "Levofloxacino", "Hidrocortisona", "Cetoprofeno", "Rabeprazol", "Vardenafila",
    "Alprazolam", "Fosfato de Codeína", "Meloxicam", "Bupropiona", "Propranolol",
    "Bromazepam", "Ciclosporina", "Fenobarbital", "Naproxeno Sódico", "Ezetimiba",
    "Etinilestradiol", "Miconazol", "Desogestrel", "Drospirenona", "Clotrimazol",
    "Dipiridamol", "Tacrolimo", "Olmesartana", "Gemfibrozil", "Rosiglitazona",
    "Dorzolamida", "Alendronato", "Dulaglutida", "Risedronato", "Adalimumabe",
    "Ciclofosfamida", "Escopolamina", "Hidroxicloroquina", "Vareniclina", "Cloridrato de Bupivacaína"
]

descricoes_de_uso = [
    "Analgésico e antipirético usado para aliviar dor e febre.",
    "Anti-inflamatório não esteroide usado para aliviar dor, febre e inflamação.",
    "Anti-inflamatório não esteroide usado para aliviar dor, febre e inflamação.",
    "Antibiótico usado para tratar infecções bacterianas, como infecções respiratórias e urinárias.",
    "Inibidor da bomba de prótons usado para tratar úlceras gástricas e refluxo ácido.",
    "Estatina usada para reduzir o colesterol e prevenir doenças cardíacas.",
    "Hormônio usado no tratamento de diabetes para regular os níveis de açúcar no sangue.",
    "Bloqueador do receptor de angiotensina usado para tratar hipertensão e insuficiência cardíaca.",
    "Analgésico narcótico usado para tratar dor intensa.",
    "Antibiótico usado para tratar infecções bacterianas, incluindo estreptococos e estafilococos.",
]

random.shuffle(medicamentos)
random.shuffle(descricoes_de_uso)

while contador <= 30:  # Loop infinito
    id_medicamento = contador

    nm_medicamento = medicamentos[contador % len(medicamentos)]
    ds_detalhada_medicamento = descricoes_de_uso[contador % len(descricoes_de_uso)]

    nr_codigo_barras = fake.unique.random_int(min=1000000000, max=9999999999, step=1)
    dt_cadastro = fake.date()
    nm_usuario = fake.user_name()

    registro = {
        "ID_MEDICAMENTO": id_medicamento,
        "NM_MEDICAMENTO": nm_medicamento,
        "DS_DETALHADA_MEDICAMENTO": ds_detalhada_medicamento,
        "NR_CODIGO_BARRAS": nr_codigo_barras,
        "DT_CADASTRO": dt_cadastro,
        "NM_USUARIO": nm_usuario
    }

    registros.append(registro)
    contador += 1


    print(registros)
