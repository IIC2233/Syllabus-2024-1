Yo soy el culpable de romper el PEP8, pero nunca adivinarás quien soy! Sólo podrás encontrarme si tienes conocimientos de listas ligadas, iteradores, generadores y funciones built-ins de python, MUAJAJAJAJAJA.

Dejé dos archivos, letras.txt y nums.txt, que juntos contienen un mensaje encriptado con mi identidad! Para desencriptarlo, debes:

* El primer paso será unir ambos archivos generando tuplas, donde el primer elemento tendrá la primera letra de letras.txt y el primer número de nums.txt, y así con el resto de los elementos.
* Los únicos elementos válidos serán aquellos donde el número será un número de fibonacci.
* El segundo paso será reordenar los elementos válidos, con el siguiente procedimiento: debes recorrer en orden las tuplas válidas, e irlas poniendo en una lista, intercalando agregar el elemento al comienzo y al final (partiendo por el comienzo).
* Deberás sólo mantener las letras en el orden resultante y olvidarte de los números.
* El tercer paso será descifrar cada letra de la lista, aplicando a cada elemento la función `descifrar_letra`
* Finalmente, deberás unir todas las letras resultantes para obtener el mensaje desencriptado.
