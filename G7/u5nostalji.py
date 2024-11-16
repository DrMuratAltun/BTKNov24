import cv2 as cv
import numpy as np
import gradio as gr

def nostalji(image):
    image=np.array(image)
    gray_image=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    return gray_image
#£gradio ara yüzünü oluşturma 

with gr.Blocks() as demo:
    gr.Markdown("# Nostalji")
    gr.Markdown("## Görsel yükleyin ve gri tona çevirsin")

    image_input=gr.Image(type='pil',label="Görsel")
    image_output=gr.Image(type='numpy',label="Gri Görsel")

    btn=gr.Button("Nostalji")
    btn.click(fn=nostalji,
              inputs=image_input,
              outputs=image_output)
    if __name__=="__main__":
        demo.launch(share=True)
'''
requirements.txt içeriği
opencv-python
numpy
'''