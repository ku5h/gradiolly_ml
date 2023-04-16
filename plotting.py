import gradio as gr
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

gr.close_all() # close all running gradio processes (else you might get 'Port In Use' error)
PORT = 8080

title = "Plotting"

def plot_bivariate_normal(num_points):
    #create a random matrix of size m x n
    matrix = np.random.randn(int(num_points), 2)
    # round a matrix to 2 decimal places
    matrix = np.round(matrix, 2)
    df = pd.DataFrame(matrix)
    # create plotly scatter and heatmap plots from the first two columns of df
    fig = px.scatter(df, x=df.columns[0], y=df.columns[1])
    fig2 = px.density_heatmap(df, x=df.columns[0], y=df.columns[1])

    return fig, fig2            

def plot_mount_bruno():
    # Read data from a csv
    z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

    fig = go.Figure(data=[go.Surface(z=z_data.values)])
    fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                    highlightcolor="limegreen", project_z=True))
    fig.update_layout(title='Mt Bruno Elevation', autosize=False,
                    scene_camera_eye=dict(x=1.87, y=0.88, z=-0.64),
                    width=500, height=500,
                    margin=dict(l=65, r=50, b=65, t=90)
    )

    return fig
    
bi_normal = gr.Interface(fn = plot_bivariate_normal, inputs="number", 
                   outputs=[gr.Plot(label='Scatter'), gr.Plot(label='Density Heatmap')])
mount_bruno = gr.Interface(fn = plot_mount_bruno, inputs=None, outputs=[gr.Plot(label='Mount Bruno Elevation')])

app = gr.TabbedInterface([bi_normal, mount_bruno], tab_names=['Bivariate Normal', 'Mount Bruno'])

app.launch(server_port=PORT)