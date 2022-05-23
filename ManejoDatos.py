from tabulate import tabulate
import os
import csv
import pandas as pd
import numpy as np

# print(os.listdir())

# csvs = []
# for file in os.listdir("Datos\Impares"):
#     print(file)
#     csvs.append(file)
# for archivo_csv in csvs:
#     lista = []
#     with open(f'Datos\\Impares\\{archivo_csv}', encoding="Latin-1") as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         line_count = 0
#         for row in csv_reader:
#             if line_count == 0:
#                 print(f'Column names are {", ".join(row)}')
#                 line_count += 1
#     print("")
    
vuelos = f"Datos\Impares\\vuelos.csv"
csv_para_crear = ["aeronaves.csv", "companias.csv", "rutas.csv", "tickets.csv", "vuelosV2.csv"]
with open(vuelos, "r", encoding="Latin-1") as csv_file:
    df_vuelos = pd.read_csv(csv_file)
    line_count = 0
    col_aeronave = ["codigo_aeronave", "nombre_aeronave", "modelo", "peso"]
    # col_compañias = ["nombre_compania", "codigo_compania"]
    col_ticket = ["valor"]
    col_vuelosV2 = ["vuelo_id", "codigo_vuelo", "codigo_compania", "fecha_salida", "fecha_llegada",\
        "velocidad", "altitud","ruta_id", "codigo_aeronave", "aerodromo_salida_id", "aerodromo_llegada_id", \
        "estado"]
        #OJO CON LOS IDS DE LOS AERODROMOS, DEBERIA SER IACO
    # col_csvs = [col_aeronave, col_compañias, col_ticket, col_vuelosV2]
    # tuplas_csv = list(zip(csv_para_crear, col_csvs))
    
    nombre_csv = "vuelosV2.csv"
    cols_csv = col_vuelosV2
    df_csv = df_vuelos[cols_csv]
    for vuelo in df_csv.values:
        # print(vuelo[-3], vuelo[-2])
        pass
    aerodromos = f"Datos\Impares\\aerodromos.csv"
    icao_salida = []
    icao_llegada = []
    print(df_csv)
    with open(aerodromos, 'r', encoding='Latin-1') as csv_file2:
        df_aerodromo = pd.read_csv(csv_file2)
        # print(df_aerodromo)
        for vuelo in df_csv.values:
            for aerodromo in df_aerodromo.values:
                # print(aerodromo)
                if vuelo[-2] == aerodromo[0]:
                    # print(aerodromo[1], vuelo[-1], aerodromo[0])
                    icao_llegada.append(aerodromo[2])
                if vuelo[-3] == aerodromo[0]:
                    icao_salida.append(aerodromo[2])
        df_csv["aerodromo_salida_id"] = icao_salida
        df_csv["aerodromo_llegada_id"] = icao_llegada 
            # print(ruta, nueva_ruta) 
    print(df_csv)

    # df_csv.to_csv(f"Datos\Impares\{nombre_csv}", index=False,)


# with open("Datos\Impares\\aeronaves.csv", 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow()
#     for row in x:
#         writer.writerow(row)
#     pass

# vuelos = f"Datos\Impares\\companias.csv"
# with open(vuelos, "r", encoding="Latin-1") as csv_file:
#     df_companias = pd.read_csv(csv_file)
#     df_c = df_companias.drop_duplicates()
#     col_companis = ["codigoCA", "nombre"]
#     nombre_csv = "companias2.csv"
#     df_csv = df_c[col_companis]
#     # print(df_csv)
#     df_csv.to_csv(f"Datos\Impares\{nombre_csv}", index=False,)

# naves = f"Datos\Impares\\aeronaves.csv"
# with open(naves, "r", encoding="Latin-1") as csv_file:
#     df_naves = pd.read_csv(csv_file)
#     df_c = df_naves.drop_duplicates()
#     nombre_csv = "aeronaves.csv"
#     df_c.to_csv(f"Datos\Impares\{nombre_csv}", index=False,)

# aerodromos = f"Datos\Impares\\aerodromos.csv"
# with open(aerodromos, 'r', encoding='Latin-1') as csv_file2:
#     df_aerodromo = pd.read_csv(csv_file2)
#     df_c = df_aerodromo.drop_duplicates()
#     df_c = df_c.sort_values(by=["aerodromo_id"])
#     df_c.to_csv(aerodromos, index=False,)
    

# rutas = f"Datos\Impares\\rutas.csv"
# csv_para_crear = ["rutasV2.csv", "puntos.csv"]
# with open(rutas, "r", encoding="Latin-1") as csv_file:
#     df_rutas = pd.read_csv(csv_file)
#     df_c = df_rutas.drop_duplicates()
#     # df_c = df_c.sort_values(by=["idruta", "cardinalidad"])
#     df_c = df_c.sort_values(by=["idruta", "cardinalidad"])
#     col_rutas = ["idruta","nombre_ruta","cardinalidad","nombre_punto","latitud","longitud"]
#     col_rutas2 = ["idruta", "nombre_ruta", "cardinalidad", "nombre_punto"]
#     col_punto = ["idpunto", "nombre_punto", "latitud", "longitud", "cardinalidad"]
#     nombre_csv_ruta = "rutasV2.csv"
#     nombre_csv_punto = "puntos.csv"
#     df_csv = df_c[col_rutas2]
#     idpunto = []
#     id = 1
#     df_puntos = df_c[["nombre_punto", "latitud", "longitud"]]
#     for punto in df_puntos.drop_duplicates().values:
#         # print(id)
#         idpunto.append(id)
#         id += 1
#     df_puntos = df_puntos.drop_duplicates()
#     df_puntos["idpunto"] = idpunto
#     cols = df_puntos.columns.tolist()
#     cols = cols[-1:] + cols[:-1]
#     df_puntos = df_puntos[cols]
#     lista_ruta_punto = []
#     nuevas_rutas = []
#     for ruta in df_csv.values:
#         for punto in df_puntos.values:
#             if ruta[-1] == punto[1]:
#                 # print(ruta[-1], punto[1], punto[0])
#                 lista_ruta_punto.append(punto[0])
#         nueva_ruta = [ruta[0],ruta[1], ruta[2]]
#         nuevas_rutas.append(nueva_ruta)
#         # print(ruta, nueva_ruta)
#     df_csv = df_csv.drop(columns=["nombre_punto"])
#     df_csv["idpunto"] = lista_ruta_punto
#     # print(df_puntos)
#     # print(df_csv)

    # df_puntos.to_csv(f"Datos\Impares\{nombre_csv_punto}", index=False,)
    # df_csv.to_csv(f"Datos\Impares\{nombre_csv_ruta}", index=False,)

# nombre_csv = tupla_csv[0]
#         col_csv = tupla_csv[1]
#         new_dict = []
#         filas = []
#         for col in df_vuelos.columns:
#             if col in col_csv:
#                 valores = df_vuelos[col].values.tolist()
#                 # print(valores)
#                 filas.append({col:valores})
#         # with open(f"Datos\Impares\{nombre_csv}", 'w', encoding='UTF8', newline='') as f:
#         #     writer = csv.DictWriter(f, fieldnames=col_csv)
#         #     writer.writeheader()
#         #     writer.writerows(rows)
#         # print(filas)