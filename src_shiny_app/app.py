import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render
import pyodide.http

with ui.sidebar():
    ui.input_slider("n", "N", 0, 100, 20)

@render.plot(alt="A histogram")
async def histogram():
    url = 'https://api.gbif.org/v1/dataset/cd6e21c8-9e8a-493a-8a76-fbf7862069e5'
    response = await pyodide.http.pyfetch(url)
    if response.status != 200:
        raise Exception(f"Error fetching {url()}: {response.status}")
    data = await response.json()        
    title = data['title']    
    x = 100 + np.random.randn(500)
    plt.title(title, size=20)
    plt.hist(x=x, bins=input.slider(), color="grey", ec="black")
