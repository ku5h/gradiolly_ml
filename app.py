import gradio as gr

gr.close_all() # close all running gradio processes (else you might get 'Port In Use' error)

def user_greeting(name):
    return "Hi! " + name + " Welcome to ECO6800, yet again!"
    
#define gradio interface and other parameters
app =  gr.Interface(fn = user_greeting, inputs="text", outputs="text")

app.launch(server_port=8080)