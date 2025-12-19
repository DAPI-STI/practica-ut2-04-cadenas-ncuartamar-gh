"""
Ejercicio 8: leer un precio con dos decimales y mostrar euros y céntimos por separado.

La función:

Recibe una cadena como "123.45" o "123,45".

Devuelve una tupla (euros, centimos) como enteros.

Valida que haya exactamente dos decimales; en caso contrario, ValueError.
"""

def euros_cents(price_str: str) -> tuple[int, int]:
    """Separa la parte entera (euros) y los céntimos a partir de una cadena."""
    # TODO: sustituye coma por punto, separa, valida y convierte a enteros
    price_str = price_str.replace(",", ".")
    parts = price_str.split(".")
    if len(parts) != 2 or len(parts[1]) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
        raise ValueError("El precio debe tener exactamente dos decimales.")
    euros = int(parts[0])
    centimos = int(parts[1])
    return (euros, centimos)