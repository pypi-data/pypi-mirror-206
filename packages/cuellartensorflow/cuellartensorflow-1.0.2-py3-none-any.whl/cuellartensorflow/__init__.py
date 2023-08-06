import wikipedia
import tensorflow as tf
import numpy as np
import pickle
from tqdm import tqdm
import random

def train_language_model(language, num_articles, num_epochs):
    # Establecer idioma de wikipedia
    wikipedia.set_lang(language)

    # Obtener una lista aleatoria de títulos de artículos
    titles = wikipedia.random(pages=num_articles)

    # Unir los contenidos de los artículos en una sola cadena de texto
    text = ""
    for title in tqdm(titles):
        try:
            page = wikipedia.page(title)
            content = page.content
            text += content + "\n"
        except wikipedia.exceptions.DisambiguationError:
            # Si el título es ambiguo, simplemente continúa con el siguiente artículo
            continue

    # Crear un tokenizador con TensorFlow
    tokenizer = tf.keras.preprocessing.text.Tokenizer(filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n')
    tokenizer.fit_on_texts([text])

    # Guardar el tokenizador como un archivo pickle
    with open('tokenizer.pkl', 'wb') as f:
        pickle.dump(tokenizer, f)

    # Convertir el texto en una secuencia de tokens
    sequences = tokenizer.texts_to_sequences([text])[0]

    # Crear una lista de ventanas deslizantes con longitud de 100 tokens
    window_size = 100
    windows = []
    for i in range(len(sequences) - window_size):
        window = sequences[i:i + window_size]
        windows.append(window)

    # Convertir las ventanas a un array de numpy
    windows = np.array(windows)

    # Crear conjuntos de entrenamiento y validación
    train_size = int(0.8 * len(windows))
    train_data = windows[:train_size]
    val_data = windows[train_size:]

    # Definir modelo de lenguaje
    model = tf.keras.models.Sequential([
        tf.keras.layers.Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=64),
        tf.keras.layers.LSTM(128),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(len(tokenizer.word_index) + 1, activation='softmax')
    ])

    # Compilar modelo
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Entrenar modelo
    model.fit(x=train_data[:, :-1], y=tf.keras.utils.to_categorical(train_data[:, -1], num_classes=len(tokenizer.word_index) + 1), 
              validation_data=(val_data[:, :-1], tf.keras.utils.to_categorical(val_data[:, -1], num_classes=len(tokenizer.word_index) + 1)), 
              epochs=num_epochs, batch_size=128)

    # Guardar modelo entrenado
    model.save('tf_model.h5')

def generate_text(seed_text, num_words, temperature):
    # Cargar el modelo entrenado y el tokenizador desde los archivos
    model = tf.keras.models.load_model("tf_model.h5")
    with open("tokenizer.pkl", 'rb') as f:
        tokenizer = pickle.load(f)

    # Definir la longitud de la secuencia de entrada y la temperatura
    sequence_length = 100
    temperature = temperature

    # Convertir la semilla inicial del texto en una secuencia de tokens
    seed_sequence = tokenizer.texts_to_sequences([seed_text])[0]

    # Generar texto
    generated_text = ""
    for i in range(num_words):
        # Cortar la secuencia de entrada a la longitud deseada
        input_sequence = seed_sequence[-sequence_length:]
        # Rellenar la secuencia de entrada si es necesario
        input_sequence = tf.keras.preprocessing.sequence.pad_sequences([input_sequence], maxlen=sequence_length, truncating='pre')
        # Predecir la siguiente palabra utilizando el modelo
        prediction = model.predict(input_sequence, verbose=0)[0]
        # Muestrear una palabra de acuerdo a la distribución de probabilidad predicha
        next_index = np.random.choice(len(prediction), p=prediction)
        # Convertir el índice de la palabra en la palabra real utilizando el tokenizador
        next_word = tokenizer.index_word[next_index]
        # Agregar la palabra generada al texto generado
        generated_text += " " + next_word
        # Agregar la palabra generada a la secuencia de entrada
        seed_sequence.append(next_index)

    # Construir el texto completo generado
    full_text = seed_text + generated_text

    # Devolver el texto generado
    return full_text