import openai

# Establece las credenciales de OpenAI API
openai.api_key = "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"

# Constantes, representan los miembros de la conversacion
SEMPAI = "Sempai: "
TSUNDERE = "Tsundere: "

# Define el prompt inicial
ai_description = "Eres una chica tsundere y estas hablando con tu sempai."

# Define los parametros para la solicitud a la API
model_engine = "davinci"
temperature = 1.0
max_tokens = 100
stop_sequence = ["\n", SEMPAI]

# Inicia el bucle de conversacion
while True:
    # Obtiene la entrada del usuario
    user_input = input(SEMPAI)

    # Si el usuario escribe "bye" se termina la conversacion
    if user_input.lower() == "bye":
        print(TSUNDERE + "Adios!")
        break

    # Envia el prompt(mensaje de usuario) y la entrada del usuario a la API
    response = openai.Completion.create(
        engine=model_engine,
        prompt=ai_description + f"\n{SEMPAI}" + user_input + "\n{TSUNDERE}:",
        temperature=temperature,
        max_tokens=max_tokens,
        stop=stop_sequence
    )

    # Obtiene la respuesta del chatbot desde la API de OpenAI
    chatbot_response = response.choices[0].text.strip()

    # Imprime la respuesta del chatbot
    print(TSUNDERE + chatbot_response)
