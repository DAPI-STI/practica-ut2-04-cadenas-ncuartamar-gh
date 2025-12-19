from ex01_repeat_name import repeat_name
from ex02_name_variants import name_variants
from ex03_name_length import name_upper_and_length
from ex04_phone_core import phone_core
from ex05_reverse_phrase import reverse_phrase
from ex06_emphasize_vowel import emphasize_vowel
from ex07_replace_domain import replace_domain
from ex08_euros_cents import euros_cents
from ex09_parse_date import parse_date
from ex10_split_products import split_products
from ex11_format_product import format_product

def main() -> None:

    # Ejemplo:
    print("=== Pruebas manuales ===")
    print(repeat_name("Ana", 3))
    print(name_variants("Carlos"))
    print(name_upper_and_length("Beatriz"))
    print(phone_core("+34-600123456-89"))
    print(reverse_phrase("Hola mundo"))
    print(emphasize_vowel("Nelson", "o"))
    print(replace_domain("ncuartamar@educacion.navarra.es"))
    print(euros_cents("12,34"))
    print(parse_date("15/06/2025"))
    print(split_products("manzana,pera,plátano"))
    print(format_product("manzana", 0.5, 3))
    

if __name__ == "__main__":
    main()