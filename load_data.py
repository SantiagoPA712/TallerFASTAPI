import pandas as pd
from sqlalchemy import create_engine

# Cambia la ruta del archivo CSV por la correcta
csv_file = '/mnt/c/Users/santi/Downloads/all_players.csv'


# Crea la conexión a la base de datos PostgreSQL
engine = create_engine('postgresql://postgres:santiago1@localhost/taller_fastapi')

# Cargar el CSV a un DataFrame
all_players_df = pd.read_csv(csv_file)

# Guarda el DataFrame en la tabla 'all_players' en PostgreSQL
# Si la tabla no existe, la creará automáticamente
all_players_df.to_sql('all_players', engine, if_exists='replace', index=False)

print("Datos cargados exitosamente a la base de datos.")
