from shiny import ui, render, App
import numpy as np
import matplotlib.pyplot as plt
import pyodide.http
app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.h2("Page Charts"),
            ui.hr(),
            ui.input_slider(id="slider", label="Number of bins:", min=5, max=25, value=15)
        ),
        ui.panel_main(
            ui.output_plot(id="histogram")
        )
    )
)

def server(input, output, session):
    @output
    @render.plot
    async def histogram():
        url = 'https://api.gbif.org/v1/dataset/cd6e21c8-9e8a-493a-8a76-fbf7862069e5'
        response = await pyodide.http.pyfetch(url)
        if response.status != 200:
            raise Exception(f"Error fetching {url()}: {response.status}")
        data = await response.json()        
        title = data['title']
        x = 100 + np.random.randn(500)
        fig, ax = plt.subplots()
        ax.hist(x=x, bins=input.slider(), color="grey", ec="black")
        ax.set_title(title)
        return fig

app = App(ui=app_ui, server=server)
