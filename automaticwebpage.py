import instaloader
import pprint
import google.generativeai as palm

# Crear una instancia de la clase Instaloader

L = instaloader.Instaloader()

# Nombre de usuario del perfil de Instagram que deseas analizar
username = 'instagramusername'

# Obtener información del perfil
profile = instaloader.Profile.from_username(L.context, username)

# Obtener la descripción del perfil
description = profile.biography

# Imprimir la descripción del perfil
print("Descripción del perfil:", description)

palm.configure(api_key='pon aqui tu api')
#Api key de:  https://makersuite.google.com/app/apikey
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
print(model)
prompt = f"Translate this to english: Create a description for generating a fictional web page for the Instagram profile '{username}' with the following description: '{description}'."
#print(prompt)
completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
)
prompt = completion.result


completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
)
print("La descripción para generar la pagina es: ",completion.result)

prompt = f"Write a captivating message offering to make a web page to the owner of the instagram page named'{username}' with the following description: '{description}'Considering that my name is Andrés"


completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
)
print("El mensaje para el cliente es: ",completion.result)