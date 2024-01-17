# [DALS: Diffusion-based Artistic Landscape Sketch](https://www.mdpi.com/2227-7390/12/2/238).

<img src="https://github.com/comeeasy/DALS/blob/main/assets/txt2sketch_3CPM.png" width="500">

## Abstract

We propose a framework that synthesizes artistic landscape sketches using a diffusion
model-based approach. Furthermore, we suggest a three-channel perspective map (3CPM) that
mimics the artistic skill used by real artists. We employ Stable Diffusion, which leads us to use
ControlNet to process 3CPM in Stable Diffusion. Additionally, we adopt the Low Rank Adaptation
(LoRA) method to fine-tune our framework, thereby enhancing the quality of sketch and resolving
the color-remaining problem, which is a frequently observed artifact in the sketch images using
diffusion models. We implement a bimodal sketch generation interface: text to sketch and image
to sketch. In producing a sketch, a guide token is used so that our method synthesizes an artistic
sketch in both cases. Finally, we evaluate our framework using quantitative and quantitative schemes.
Various sketch images synthesized by our framework demonstrate the excellence of our study.

# How to run demo

<img src="https://github.com/comeeasy/DALS/blob/main/assets/demo_example.png" width="500">

### Step 1: Install AUTOMATIC1111 webui

```shell
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
```

### Step 2: Install ControlNet Extention into webui**

you can follow instructions [here](https://github.com/Mikubill/sd-webui-controlnet#installation).

### Step 3: Download weights

- Weights (about 10GB+): [download link](https://drive.google.com/drive/folders/1c4WdTmARQCVlHv3p_7iXZTsyhyupgzmY?usp=sharing)

### Step 4: Locate each weight into

- Stable Diffusion weight: `<git repo path>/stable-diffusion-webui/models/Stable-diffusion`
- LoRA weight: `<git repo path>/stable-diffusion-webui/models/Lora`
- ControlNet (3CPM) weight: `<git repo path>/stable-diffusion-webui/models/ControlNet`

### Step 5: Run webui as a api server

```shell
cd stable-diffusion-webui
bash webui.sh --api
```

### Step 6: Run user interface for DALS

```shell
cd <git repo>
python main.py
```

---
