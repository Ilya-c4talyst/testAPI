from datetime import datetime

from pydantic import BaseModel, Field, field_validator


class Task(BaseModel):
    """Модель для описания запроса на получение депозита."""

    date: str = Field()
    periods: int = Field(ge=1, le=60)
    amount: int = Field(ge=10_000, le=3_000_000)
    rate: float = Field(ge=1, le=8)

    @field_validator("date")
    def validate_date(cls, val):

        try:
            datetime.strptime(val, "%d.%m.%Y")

        except ValueError:
            raise ValueError("must be in format dd.mm.YYYY")

        return val
