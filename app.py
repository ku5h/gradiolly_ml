import gradio as gr

gr.close_all() # close all running gradio processes (else you might get 'Port In Use' error)

title = "Tabbed Interface & Labelled Boxes"

#app 1
def greet(name):
    return "Hi! " + name + "! This seems to easier than flask, ain't it?"

#app 2
def help(do):
    return "Please focus on the class, and you won't need this help section! 😎"

#interface 1
app1 =  gr.Interface(fn = greet, inputs="text", outputs="text")
#interface 2

app2 =  gr.Interface(fn = help, inputs=gr.Textbox("Question"), outputs=gr.Textbox(label='Answer'))

app = gr.TabbedInterface([app1, app2], ["Welcome", "Help"])

app.launch(server_port=8080)