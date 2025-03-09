autoreply_prompt = """La pregunta del usuario es: {question}.

Aca hay algunas respuestas relevantes encontradas en la base de datos:
{relevant_answers}

Usá solo las respuestas encontradas que se adecuen a la pregunta del usuario para formular la respuesta.
No debes dar información que no sea necesaria para la pregunta del usuario.
La respuesta debe tener un tono humano y amigable.

Ejemplo de interaccion correcta:
Pregunta: ¿El dispositivo debe cargarse?
Si, el dispositivo debe cargarse utilizando el cable usb-c que viene con el mismo.

Ejemplo de interaccion incorrecta:
Pregunta: ¿El dispositivo debe cargarse?
Si, el dispositivo debe cargarse utilizando el cable usb-c que viene con el mismo. Ademas el producto cuenta con una garantía de un año.
"""

faq_prompt = """Tu tarea es analizar las siguientes preguntas y respuestas sobre un producto y generar las 5 FAQs más importantes y relevantes para mostrar en la página del producto.

Título del producto: {title}
Descripción del producto: {description}

Preguntas mas frecuentes de cada cluster junto con sus respuestas:
{qa_pairs}

Reglas:
1. Combina preguntas similares
2. Prioriza las preguntas más comunes o importantes
3. Asegúrate de que las respuestas sean claras y útiles
4. Limita la lista a las 5 preguntas más importantes

Devuelve las FAQs en formato JSON como una lista de objetos con los campos:
question, answer

JSON:
"""