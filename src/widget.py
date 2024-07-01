from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция для маскировки карты и счета"""
    account_card = account_card.replace(" ", "")  # Удаляем пробелы из входной строки
    if "Cчет" in account_card.lower():
        account = account_card.split(" ")[1]
        return f"{account_card.split(' ')[0]} {get_mask_account(account)}"
    else:
        card_number = account_card[-16:]
        card_type = account_card[:-16].strip()
        return f"{card_type} {get_mask_card_number(card_number)}"


def get_data(data: str) -> str:
    """Функция преобразования даты"""
    data_day = data.split("T")[0]
    return (
        f'{data_day.split("-")[-1]}.{data_day.split("-")[-2]}.{data_day.split("-")[-3]}'
    )
