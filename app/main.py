import uvicorn
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from models import Task
from utils import count_deposite


app = FastAPI()


@app.exception_handler(RequestValidationError)
def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
) -> JSONResponse:
    """Перехватчик исключений, формирует код 400 и сообщение об ошибке."""

    errors = [err["loc"][1] + err["msg"][5:] for err in exc.errors()]
    print(exc.errors())

    return JSONResponse(
        status_code=400,
        content={"error": errors[0]},
    )


@app.post('/task')
def get_deposite(task: Task) -> JSONResponse:
    """Обработка POST запроса для рассчета депозита."""

    data = count_deposite(task.date, task.periods, task.amount, task.rate)

    return JSONResponse(content=data, status_code=200)


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
