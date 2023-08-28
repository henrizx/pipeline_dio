import pandas as pd

# Leitura do arquivo CSV
df = pd.read_csv('data.csv')
print(df)


def update_character(id, attribute, updated_value):
    df.loc[df['ID'] == id, attribute] = updated_value
    df.to_csv('data.csv', index=False)


# Atualização do personagem com ID 1
update_character(1, "Abilities", "['Lightsaber Mastery','Force Push']")
updated_df = pd.read_csv('data.csv')
print(updated_df)
