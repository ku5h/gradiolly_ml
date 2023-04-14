import gradio as gr
import pandas as pd
import numpy as np

gr.close_all() # close all running gradio processes (else you might get 'Port In Use' error)
PORT = 8080

title = "Dataframes"

#app 1
def greet(name):
    return "Hi! " + name + "! This seems to easier than flask, ain't it?"

#app 2
def help(do):
    return "Please focus on the class, and you won't need this help section! 😎"

def display_randn_matrix(rows, columns):
    #create a random matrix of size m x n
    matrix = np.random.rand(int(rows), int(columns))
    # round a matrix to 2 decimal places
    matrix = np.round(matrix, 2)
    return pd.DataFrame(matrix)

app1 =  gr.Interface(fn = greet, inputs="text", outputs="text")
app2 = gr.Interface(fn = display_randn_matrix, inputs=["number", "number"], outputs=gr.DataFrame(label="Matrix"))
app3 =  gr.Interface(fn = help, inputs=gr.Textbox("Question"), outputs=gr.Textbox(label='Answer'))

app = gr.TabbedInterface([app1, app2, app3], ["Welcome", "Matrix", "Help"])

app.launch(server_port=PORT)