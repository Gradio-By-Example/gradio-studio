import gradio as gr

with gr.Blocks() as demo:
    textbox_2 = gr.Textbox()
    textbox = gr.Textbox()

demo.launch()