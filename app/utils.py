import calendar
from datetime import timedelta, datetime


def count_deposite(
        date: str,
        periods: int,
        amount: int,
        rate: float
) -> dict[str, float]:
    """Вычисление депозита по входным данным."""

    data = dict()
    KOEF = 1 + rate / 12 / 100
    current = amount
    date = datetime.strptime(date, "%d.%m.%Y")

    for _ in range(periods):
        current *= KOEF
        data[date.strftime("%d.%m.%Y")] = round(current, 2)
        days = calendar.monthrange(date.year, date.month % 12 + 1)[1]
        date += timedelta(days=days)

    return data
