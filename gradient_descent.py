import gradio as gr
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_gradient_descent(learning_rate, num_iterations):
    # Define the function to optimize (in this case, a simple parabola)
    def f(x):
        return x**2 + 5

    # Define the derivative of the function
    def df(x):
        return 2*x

    # Define the range of x values to plot
    x_vals = np.linspace(-10, 10, 100)

    # Define the initial value of x
    x = -9

    # Set up the plot
    fig, ax = plt.subplots()
    ax.plot(x_vals, f(x_vals))
    ax.set_xlim([-10, 10])
    ax.set_ylim([0, 100])
    line, = ax.plot([], [], 'ro')

    # Define the update function for the animation
    def update(frame):
        nonlocal x
        x -= learning_rate * df(x)
        line.set_data([x], [f(x)])
        return line,

    # Create the animation
    anim = FuncAnimation(fig, update, frames=np.arange(num_iterations), interval=500, blit=True)

    # Display the animation
    return anim.to_html5_video()

app = gr.Interface(
    fn=animate_gradient_descent,
    inputs=[gr.Number(label="Learning Rate"),
            gr.Number(label="Number of Iterations")],
    outputs=gr.outputs.HTML(label="Animation"),
    title="Gradient Descent Animation",
    description="An animation that explains how gradient descent works.",
    theme="default"
)

app.launch()
