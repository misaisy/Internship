"""
Модуль простого API калькулятора.

Содержит функции:
- summarise: функция Суммирования
- multiply: функция умножения
- divide: функция деления
"""

from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/calc/sum")
async def summarise(num1: float, num2: float):
    """Функция суммирования.

    :param num1: первое слагаемое
    :param num2: второе слагаемое
    :return: результат сложения
    """
    summa = num1 + num2
    return {
        "result": summa
    }


@app.get("/calc/multiply")
async def multiply(num1: float, num2: float) -> dict:
    """Функция умножения.

    :param num1: первый множитель
    :param num2: второй множитель
    :return: результат умножения
    """
    multiply = num1 * num2
    return {
        "result": multiply
    }


@app.get("/calc/divide")
async def divide(num1: float, num2: float):
    """Функция деления.

    :param num1: делимое
    :param num2: делитель
    :return: результат деления (частное)
    """
    if num2 == 0:
        raise HTTPException(status_code=422, detail="Нельзя делить на ноль!")
    divide = num1 / num2
    return {
        "result": divide
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
