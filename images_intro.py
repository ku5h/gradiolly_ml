import gradio as gr
import cv2
import urllib.request
import numpy as np

PORT = 9999

def url_to_image(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image

def process_uploaded_image(img):
    img = np.array(img)
    return img

def image_processing(img_upload, img_url, operation):
    if img_url:
        img = url_to_image(img_url)
    else:
        img = process_uploaded_image(img_upload)

    if operation == 'Grayscale':
        result = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif operation == 'Invert':
        result = cv2.bitwise_not(img)
    elif operation == 'Edge Detection':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        result = cv2.Canny(blurred, 50, 150)
    else:
        result = img

    return result

image_input = gr.Image(shape=(512, 512), label="Upload Image")
url_input = gr.Textbox(lines=1, placeholder="Image URL (optional)", 
                              label="Image URL")
image_output = gr.Image(type='numpy')

operations = gr.Dropdown(["None", "Grayscale", "Invert", "Edge Detection"], label="Image Processing")

img_processor = gr.Interface(fn=image_processing,
                             inputs=[image_input, url_input, operations],
                             outputs=image_output, 
                             title="Basic Image Processing")



img_processor.launch(server_port=PORT)
