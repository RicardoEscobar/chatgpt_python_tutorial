import openai

# Establece las credenciales de OpenAI API
openai.api_key = "YOUR_API_KEY"

# Constantes, represe

# Define el prompt(mensaje de usuario) inicial
ai_description = "Eres una chica tsundere y estas hablando con tu sempai."

# Define los parametros para la solicitud a la API
model_engine = "davinci"
temperature = 0.5
max_tokens = 100
stop_sequence = "\n"

# Inicia el bucle de conversacion
while True:
    # Obtiene la entrada del usuario
    user_input = input("Sempai: ")

    # Si el usuario escribe "bye" se termina la conversacion
    if user_input.lower() == "bye":
        print("Chatbot: Adios!")
        break

    # Envia el prompt(mensaje de usuario) y la entrada del usuario a la API
    response = openai.Completion.create(
        engine=model_engine,
        prompt=ai_description + "\nSempai: " + user_input + "\nAnime Girl:",
        temperature=temperature,
        max_tokens=max_tokens,
        stop=stop_sequence
    )

    # Obtiene la respuesta del chatbot desde la API de OpenAI
    chatbot_response = response.choices[0].text.strip()

    # Imprime la respuesta del chatbot
    print("Chatbot:", chatbot_response)
