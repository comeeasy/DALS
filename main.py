import os
import gradio as gr
import argparse

from PIL import Image

from src.api import DALS_API
from src.utils import read_config


def mirror(x):
    return x

def show_image(selected_label):
    image_path = image_options[selected_label]
    return Image.open(image_path)

def process_input(prompt, img_path):
    
    print(f"process_input: img_path: {img_path}")
    
    if img_path:
        return api.generate_image(prompt, img_path)
    else:
        # Generate image from prompt using API
        return api.generate_image(prompt)

image_options = {
    "3CPM_1": "/home/hm086/joono/DALS/3CPM_examples/far_sighted/npp1.png",
    "3CPM_2": "/home/hm086/joono/DALS/3CPM_examples/one_vanishing_point/opp1.png",
    "3CPM_3": "/home/hm086/joono/DALS/3CPM_examples/two_vanishing_points/tpp1.png",
    # Add as many images as you like
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str)
    args = parser.parse_args()
    print(args.config)

    cfg = read_config(args.config)
    print(f"[cfg]: {cfg}")

    api = DALS_API(cfg)

    with gr.Blocks() as demo:
        with gr.Row():
            threeCPM_img = gr.Image(type="pil")
            result_img = gr.Image(type="pil")

        with gr.Row():
            input_prompt = txt = gr.Textbox(label="Input", lines=2)

        btn = gr.Button(value="Submit")
        btn.click(process_input, inputs=[input_prompt, threeCPM_img], outputs=[result_img])

        gr.Markdown("## Image Examples")
        gr.Examples(
            examples=[
                os.path.join(os.path.dirname(__file__), "3CPM_examples/far_sighted/npp1.png"),
                os.path.join(os.path.dirname(__file__), "3CPM_examples/one_vanishing_point/opp1.png"),
                os.path.join(os.path.dirname(__file__), "3CPM_examples/two_vanishing_points/tpp1.png"),
            ],
            inputs=threeCPM_img,
            outputs=threeCPM_img,
            fn=mirror,
            cache_examples=True,
        )

    demo.launch()
