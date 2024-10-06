""" This is the main app"""

from typing import Union, Optional
from fastapi import FastAPI
from pydantic import BaseModel

from models._allmodels import ItemIn, ResponseOut, Visual, BarData, PieData


app = FastAPI()

# Crear el endpoint POST
@app.post("/ia-process/", response_model=ResponseOut)
async def create_item(item: ItemIn):
    # Mensaje de salida
    message = f"Texto de analisis generado por openai de ejemplo .. y este texto: {item.name} fue pasado desde el cliente"

    # Ejemplo de visualización para gráfico de barras
    bar_data = BarData(
        title='Titulo de Bar char generado por ia',
        explanation='Explicacion del grafico generado por ia',
        labels=["Category 1", "Category 2"],
        values=[10.0, 20.0]
    )

    # Ejemplo de visualización para gráfico de torta
    pie_data = PieData(
        title='Titulo de Pie  char generado por ia',
        explanation='Explicacion del grafico generado por ia',
        labels=["Category 1", "Category 2"],
        percentages=[50.0, 50.0]
    )

    # Crear la lista de visuales (gráfico de barras y gráfico de torta)
    visuals = [
        Visual(char_type="bar", data=bar_data),
        Visual(char_type="pie", data=pie_data)
    ]

    # Retornar la respuesta con el mensaje y los gráficos
    return ResponseOut(message=message, visual=visuals)
