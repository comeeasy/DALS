# DALS: Diffusion-based Artistic Landscape Sketch

<img src="https://github.com/comeeasy/DALS/blob/main/assets/txt2sketch_3CPM.png" width="1000">
---

## Abstract

Coming soon after publication...

---

# How to run demo

<img src="https://github.com/comeeasy/DALS/blob/main/assets/demo_example.png" width="1000">

### Step 1: Install AUTOMATIC1111 webui

```shell
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
```

### Step 2: Install ControlNet Extention into webui**

you can follow instructions [here](https://github.com/Mikubill/sd-webui-controlnet#installation).

### Step 3: Download weights

- Stable Diffusion weight: link
- LoRA weight: line
- ControlNet weight (3CPM): link

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
