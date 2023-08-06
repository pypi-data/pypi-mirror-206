Una libreria simple para crear modelos de lenguaje de forma practica y sencilla usando tensorflow en pocas lineas de codigo

instalacion de la libreria:

```shell
pip install cuellartensorflow
```

Creando nuestro primer modelo:
el modelo se entrena con datos directos de wikipedia por lo que no es necesario descargar ningun dataset.

```python
from cuellartensorflow import train_language_model

modelo = train_language_model(
    language="es",
    num_articles=10,
    num_epochs=10
)
```
cambia el parametro "es" de la funcion  languaje="es"  para entrenar el modelo con un idioma distinto consulta la documentacion de wikipedia para mayor informacion, "num_articles" para especificar el numero de articulos a usar para el entrenamiento, "num_epochs" para especificar el numero de epocas a usar para el entrenamiento del modelo

Para generar texto usando nuestro modelo recien creado puedes usar el siguiente codigo:

```python
from cuellartensorflow import generate_text

texto=generate_text(
    seed_text="La educacion",
    num_words=15,
    temperature=0.7
)

print(texto)
```
usa el apartado "seed_text" para especificar la palabra semilla para generar texto a partir de ella, "num_words" sirve para especificar el numero de palabras a generar por el modelo
"temperature" controla la temperatura para la creatividad del modelo


la libreria es muy facil de usar para cualquier principiante que quiera crear su propio modelo de lenguaje de forma rapida y sencilla