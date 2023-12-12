
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Edge()
driver.get('https://datosmacro.expansion.com/pib/ecuador')

def reemplazar_n(texto):
    return texto.replace('Ñ', 'N')
contenido = driver.page_source
soup = BeautifulSoup(contenido, 'html.parser')


tabla_pib = soup.find('table')


anios = []
pib_millones_dolares = []
variacion_porc = []


if tabla_pib:
    filas = tabla_pib.find_all('tr')
    for fila in filas[1:]:
        columnas = fila.find_all('td')
        anios.append(reemplazar_n(columnas[0].text.strip()))
        pib_millones_dolares.append(reemplazar_n(columnas[2].text.strip()))
        variacion_porc.append(reemplazar_n(columnas[3].text.strip()))


df_pib = pd.DataFrame({
    'Año': anios,
    'PIB (Millones de Dólares)': pib_millones_dolares,
    'Variación %': variacion_porc
})
df_pib.to_csv('pib_ecuador.csv', index=False, encoding='utf-8-sig')
driver.quit()

print(df_pib)

'''
DOMENICA ANCHUNDIA 
BRYAN REVELO
DARLING MEDINA
JAME YEPEZ 
'''