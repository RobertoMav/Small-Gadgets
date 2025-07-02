PATH = "/Users/robertomartins/Downloads/DNIT-Distancias.csv"

import pandas as pd
import numpy as np
df_dist = pd.read_csv(PATH)

city_arr = df_dist.head(0).columns.to_numpy()[0].split(";")

np_dist = df_dist.to_numpy()[:,0]



def find_distance(cidade_1, cidade_2):
    try:
        idx_cidade1 = city_arr.index(cidade_1)
        idx_cidade2 = city_arr.index(cidade_2)
    
    except ValueError:
        return "Wrong city Input"
    
    distance = np_dist[idx_cidade1].split(";")[idx_cidade2]

    return distance


print(find_distance("ARACAJU", "BELEM"))

