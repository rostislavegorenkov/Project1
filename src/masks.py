def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает её маску в формате XXXX XX** **** XXXX
    """
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску в формате **XXXX
    """
    return f"**{account[-4:]}"
