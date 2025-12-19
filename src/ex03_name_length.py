"""
Ejercicio 3: leer un nombre y mostrarlo en mayúsculas y cuántas letras tiene.

La función devolverá una tupla:
(nombre_en_mayusculas, numero_de_letras_sin_espacios)
"""

def name_upper_and_length(name: str) -> tuple[str, int]:
    """Devuelve (NAME_EN_MAYUSCULAS, numero_de_letras_sin_espacios)."""
    # TODO: pasa el nombre a mayúsculas y cuenta las letras sin espacios
    name_upper = name.upper()
    length_without_spaces = len(name.replace(" ", ""))

    return (name_upper, length_without_spaces)