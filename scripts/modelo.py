import pandas as pd
from sklearn.neighbors import NearestNeighbors

def modelo_pred(age, overall, archivo='jugadores.csv'):
    '''
    Funcion que toma el archivo 'jugadores.csv' y predice el valor de un jugador y su salario semanal.
    
    :param age: edad del jugador que se ingresa (int), debe ser mayor a 16
    :param overall: media del jugador que se ingresa (int), debe estar entre 40 y 99
    :param archivo: archivo csv con los datos de los jugadores (str), se espera que se ignore este parametro
    :return : valor,salario de la prediccion (tupla de int) 
    '''
    if (age<16) or (overall<40) or (overall>=100):
        raise RuntimeError('Age tiene que ser mayor a 16 y overall tiene que estar entre 40 y 100.')
    
    fifa_data = pd.read_csv(archivo)

    overall_threshold = max(fifa_data['overall'])

    percentage_increase = 0.10  # 10%

    # Filtrar el conjunto de datos para incluir solo jugadores con "overall" mayor o igual al umbral
    filtered_data = fifa_data[fifa_data['overall'] >= overall_threshold]

    # Crear un DataFrame con las características de todos los jugadores
    features = fifa_data[['age', 'overall']]

    # Inicializar el modelo de búsqueda del vecino más cercano
    k = 1  # Buscar el jugador más cercano
    nn = NearestNeighbors(n_neighbors=k, algorithm='ball_tree')
    nn.fit(features)

    # Encontrar el jugador más similar al nuevo jugador
    new_player_features = [[age, overall]]
    distances, indices = nn.kneighbors(new_player_features)

    # Obtener el índice del jugador más similar
    closest_index = indices[0][0]

    # Aumentar el valor_eur si el nuevo jugador tiene un "overall" mayor al umbral
    if (overall > overall_threshold) and (closest_index < len(filtered_data)):
        #Estimado del valor:
        closest_player_value_eur = filtered_data.iloc[closest_index]['value_eur']
        closest_player_value_eur *= (1 + percentage_increase * (overall - overall_threshold))
        #Estimado del salario:
        closest_player_wage_eur = filtered_data.iloc[closest_index]['wage_eur']
        closest_player_wage_eur *= (1 + percentage_increase * (overall - overall_threshold))
        return round(closest_player_value_eur), round(closest_player_wage_eur)
    else:
        closest_player_value_eur = fifa_data.iloc[closest_index]['value_eur'] #Valor
        closest_player_wage_eur = fifa_data.iloc[closest_index]['wage_eur'] #Salario
        return round(closest_player_value_eur), round(closest_player_wage_eur)

def nuevas_valoraciones():
    pass

