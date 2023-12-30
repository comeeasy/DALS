import torch
import diffusers

from safetensors.torch import load_file



class DALS:
    
    def __init__(self, cfg) -> None:
        self.cfg = cfg
        
        # load 3CPM ControlNet
        self.ctrlNet_3CPM = diffusers.ControlNetModel.from_pretrained(self.cfg["controlnet_3CPM_path"])
        
        # load Stable Diffusion
        self.pipe = diffusers.StableDiffusionControlNetPipeline.from_pretrained(self.cfg["model_path"], controlnet=self.ctrlNet_3CPM)
        self.pipe.load_lora_weights(self.cfg["lora_path"])
        self.pipe = self.pipe.to(self.cfg["device"])
        
        # We use DDIM scheduler
        self.pipe.scheduler = diffusers.DDIMScheduler.from_config(self.pipe.scheduler.config)
        
        # default inference configures
        self.num_inference_steps = self.cfg["num_inference_steps"]
        self.default_neg_prompt = self.cfg["default_neg_prompt"]
        self.default_prompt = self.cfg["default_prompt"]
        
        
    def txt2sketch(self, prompt, threeCPM=None):
        input_prompt = ", ".join([prompt, self.default_prompt])
        
        if threeCPM is None:
            sketches = self.pipe(
                input_prompt, 
                None,
                negative_prompt=self.default_neg_prompt,
                num_inference_steps=self.cfg["num_inference_steps"],
                guidance_scale=self.cfg["guidance_scale"],
                num_images_per_prompt=4
            )
        else: # use 3CPM
            sketches = self.pipe(
                input_prompt, 
                threeCPM,
                controlnet_conditioning_scale=self.cfg["controlnet_3CPM_weight"],
                negative_prompt=self.default_neg_prompt,
                num_inference_steps=self.cfg["num_inference_steps"],
                guidance_scale=self.cfg["guidance_scale"],
                num_images_per_prompt=4
            )
        
        return sketches.images
                
        
        
    def img2sketch(self, img, threeCPM=None):
        ...
        
    