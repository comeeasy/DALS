import os
import cv2
import requests
import json

import base64
import matplotlib.pyplot as plt

import numpy as np

from PIL import Image
from io import BytesIO



class DALS_API:
    def __init__(self, cfg) -> None:
        self.cfg = cfg
        
        self.url = self.cfg['url']

    def get_available_loras(self) -> requests.Response:
        url = "/".join([self.url, "sdapi", "v1", "loras"])
        
        response = requests.get(url=url)
        # Check the response (optional)
        if response.status_code == 200:
            print("Request successful.")
        else:
            print(f"Request failed with status code {response.status_code}.")
            
        return response
    
    def generate_image(self, prompt="cafe", threeCPM: Image=None):
        url = "/".join([self.url, "sdapi", "v1", "txt2img"])

        prompt = ", ".join([prompt, self.cfg["default_prompt"]])

        print(f"prompt: {prompt}, 3CPM_path: {threeCPM.size}")
        
        # Prepare the headers
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare the data payload
        data = {
            "prompt": prompt,
            "negative_prompt": self.cfg["default_neg_prompt"],
            "seed": -1,
            "steps": 25,
            "cfg_scale": 7.5
        }
        
        # 3CPM
        if threeCPM:
            # Read Image in RGB order
            img = self.pil_to_cv2(threeCPM)

            # Encode into PNG and send to ControlNet
            retval, bytes = cv2.imencode('.png', img)
            encoded_image = base64.b64encode(bytes).decode('utf-8')
            
            data["alwayson_scripts"] = {
                "controlnet": {
                    "args": [{
                        "input_image": encoded_image,
                        "model": "control_distMap_deliberate_v2_step8000 [868e4700]",
                        "weight": 0.8,
                        "resize_mode": 0
                    }]
                }
            }
            
        print(data)

        # Make the POST request
        response = requests.post(url, headers=headers, data=json.dumps(data))

        # Check the response (optional)
        if response.status_code == 200:
            print("Request successful.")
            return self.response_to_pil(response)
        else:
            print(f"Request failed with status code {response.status_code}.")
            return None
    
    @staticmethod
    def response_to_pil(response):
        # Assume 'response' is your requests response
        response_json = response.json()

        # Extract base64 encoded string (assuming the first image in the list)
        encoded_image = response_json['images'][0]

        # Decode the base64 string
        image_data = base64.b64decode(encoded_image)

        # Convert to an image
        image = Image.open(BytesIO(image_data))
        
        return image

    def __set_model(self):
        url = "/".join([self.url, "sdapi", "v1", "options"])
        model_name = "deliberateForInvoke_v08.ckpt"

        option_payload = {
            "sd_model_checkpoint": model_name,
            # "CLIP_stop_at_last_layers": 2
        }

        response = requests.post(url=url, json=option_payload)
        
        # Check the response (optional)
        if response.status_code == 200:
            print("Request successful.")
        else:
            print(f"Request failed with status code {response.status_code}.")
            
    @staticmethod
    def pil_to_cv2(pil_image):
        # Convert PIL Image to numpy array
        numpy_image = np.array(pil_image)

        # Convert from RGB to BGR (OpenCV format)
        opencv_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)

        return opencv_image