from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

@app.get("/calc/sum")
async def summarise(num1: float, num2: float):
    """
        Функция Суммирования

        :param num1: первое слагаемое
        :param num2: второе слагаемое
        :return: результат сложения
    """
    sum = num1 + num2
    return {
        "result": sum
    }

@app.get("/calc/multiply")
async def multiply(num1: float, num2: float) -> dict:
    """
        Функция Умножения

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
    """
        Функция Деления

        :param num1: делимое
        :param num2: делитель
        :return: результат деления (частное)
    """
    if num2 == 0:
        raise HTTPException(status_code = 422, detail="Нельзя делить на ноль!")
    divide = num1 / num2
    return {
        "result": divide
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)