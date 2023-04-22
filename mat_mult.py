#display a data
import gradio as gr
import pandas as pd
import numpy as np
import plotly.express as px

def create_heatmap(matrix):
    heatmap = px.imshow(matrix.round(2), color_continuous_scale='RdYlGn', text_auto=True)
    heatmap.update_layout(width=500, height=500)
    heatmap.update_layout(xaxis_title="Row", yaxis_title="Column")
    return heatmap
def mat_mult(A, B):

    #convert dataframes A and B to numpy arrays, and multiply them
    A = A.to_numpy().astype(np.float32)
    B = B.to_numpy().astype(np.float32)
    #Matrix multiplication
    C = np.dot(A, B)
    #convert matrix C to a heatmap image
    return create_heatmap(C)

#Some Interesting examples

example0 = [pd.DataFrame([[1, 1, -1]]), pd.DataFrame([[-1], [1], [0]])]
example1 = [pd.DataFrame([[1, 2], [3, 4]]), pd.DataFrame([[5, 6], [7, 8]])]
example2 = [pd.DataFrame([[-1, 2], [3, 0]]), pd.DataFrame([[0, 2], [1, -2]])]
example3 = [pd.DataFrame([[1, 2, 3], [4, 5, 6]]), pd.DataFrame([[7, 8], [9, 10], [11, 12]])]
example4 = [pd.DataFrame([[1, 0, -1], [0, 1, 0], [1, 0, 1]]), pd.DataFrame([[1, 1, 1], [-1, -1, -1], [0, 0, 0]])]
example5 = [pd.DataFrame(np.random.randn(10, 10)).round(2), pd.DataFrame(np.random.randn(10, 10)).round(2)]
examples = [example0, example1, example2, example3, example4, example5]

title = "Matrix Multiplication"
description = "Multiply two matrices and display the resulting heatmap."

app = gr.Interface(mat_mult, 
                    inputs=[gr.DataFrame(row_count=(1, 'dynamic'), col_count=(1, 'dynamic'), headers=None), 
                            gr.DataFrame(row_count=(1, 'dynamic'), col_count=(1, 'dynamic'), headers=None)], 
                    outputs=gr.Plot(),
                    examples=examples, title=title, description=description)
app.launch()
