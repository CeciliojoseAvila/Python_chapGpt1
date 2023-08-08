import os
import openai
import spacy
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

'''
modelos = openai.Model.list()
print(modelos)
'''
modelo = "text-davinci-002"
prompt = "Cuenta una historia breve sobre un viaje a un pais Europeo."

respuesta=openai.Completion.create(
    engine=modelo,
    prompt=prompt,
    n=3,
    temperature=1,
    max_tokens=100
)
""" 
for index, opcion in enumerate(respuesta.choices):
    texto_generado = opcion.text.strip()
    print(f"Respuesta {index + 1 }: {texto_generado}\n")
"""
texto_generado = respuesta.choices[0].text.strip()
print(texto_generado)

print("****")

modelo_spacy = spacy.load("es_core_news_md")
analisis = modelo_spacy(texto_generado)

ubicacion = None

""" 
for token in analisis:
    print(token.text, token.dep_, token.head.text)
"""

for ent in analisis.ents:
    if ent.label_ == "LOC":
        ubicacion = ent
        break

if ubicacion:
    prompt2= f"Dime más acerca de {ubicacion}"
    respuesta2= openai.Completion.create(
        engine=modelo,
        prompt=prompt2,
        n=1,
        max_tokens=100
    )
    print(respuesta2.choices[0].text.strip())




