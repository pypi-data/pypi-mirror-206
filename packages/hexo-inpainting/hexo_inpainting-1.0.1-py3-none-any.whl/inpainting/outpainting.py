from model_manager import ModelManager
from schema import Config, HDStrategy, LDMSampler, SDSampler
import cv2
import numpy as np
import math
import numpy as np
import torch
from PIL import Image, ImageDraw

def get_config(strategy, ldm_sampler, sd_mask_blur, sd_steps, prompt, negative_prompt,controlnet_conditioning_scale,  **kwargs):
    data = dict(
        ldm_steps=50,
        ldm_sampler=ldm_sampler,
        sd_mask_blur=sd_mask_blur,    
        sd_strength= 0.75,
        sd_steps=sd_steps,
        sd_guidance_scale=7.5,
        sd_sampler=SDSampler.k_euler_a,
        prompt=prompt,
        negative_prompt=negative_prompt,
        hd_strategy=strategy,
        hd_strategy_crop_margin=128,
        hd_strategy_crop_trigger_size=1080,
        hd_strategy_resize_limit=1080,
        controlnet_conditioning_scale = controlnet_conditioning_scale,
        no_half = False,
        enable_xformers = True
    )
    data.update(**kwargs)
    return Config(**data)

def callback(i, t, latents):
    pass

sd_device = "cuda"
sd_steps = 100 if sd_device == "cuda" else 1

control_model = ModelManager(
        name="sd1.5",
        sd_controlnet=True,
        device=torch.device(sd_device),
        hf_access_token="",
        sd_run_local=False,
        disable_nsfw=False,
        sd_cpu_textencoder=False,
    )


def outpaint_help(init_img, direction, pixels, mask_blur):
    left = 0
    right = 0
    up = 0
    down = 0
    if "left" in direction:
        left = pixels #pixels if "left" in direction else 0
    if "right" in direction:
        right = pixels #pixels if "left" in direction else 0
    if "up" in direction:
        up = pixels #pixels if "left" in direction else 0
    if "down" in direction:
        down = pixels #pixels if "left" in direction else 0

    # mask_blur = 2

    # init_img = Image.open(r'/home/ec2-user/download (6).png')
    target_w = math.ceil((init_img.width + left + right) / 64) * 64
    target_h = math.ceil((init_img.height + up + down) / 64) * 64

    if left > 0:
        left = left * (target_w - init_img.width) // (left + right)
    if right > 0:
        right = target_w - init_img.width - left

    if up > 0:
        up = up * (target_h - init_img.height) // (up + down)

    if down > 0:
        down = target_h - init_img.height - up

    img = Image.new("RGB", (target_w, target_h))
    img.paste(init_img, (left, up))

    mask = Image.new("L", (img.width, img.height), "white")
    draw = ImageDraw.Draw(mask)
    draw.rectangle((
        left + (mask_blur * 2 if left > 0 else 0),
        up + (mask_blur * 2 if up > 0 else 0),
        mask.width - right - (mask_blur * 2 if right > 0 else 0),
        mask.height - down - (mask_blur * 2 if down > 0 else 0)
    ), fill="black")

    latent_mask = Image.new("L", (img.width, img.height), "white")
    latent_draw = ImageDraw.Draw(latent_mask)
    latent_draw.rectangle((
            left + (mask_blur//2 if left > 0 else 0),
            up + (mask_blur//2 if up > 0 else 0),
            mask.width - right - (mask_blur//2 if right > 0 else 0),
            mask.height - down - (mask_blur//2 if down > 0 else 0)
    ), fill="black")
    return img, mask

def predict(dict, sd_mask_blur = 1, sd_steps = 50, prompt = "background", negative_prompt= "", scale=0.75):
    init_img =  dict['image'].convert("RGB")
    mask_img = dict['mask'].convert("L")
    init_img = init_img.resize((int(init_img.size[0]/64)*64,int(init_img.size[1]/64)*64))
    mask_img = mask_img.resize((int(init_img.size[0]/64)*64,int(init_img.size[1]/64)*64))
    cfg = get_config(HDStrategy.CROP, LDMSampler.plms, sd_mask_blur, sd_steps, prompt, negative_prompt, scale)
    
    with torch.inference_mode():
        init_img= control_model(np.array(init_img),np.array(mask_img.convert("L")), cfg)
    init_img = Image.fromarray(cv2.cvtColor(init_img.astype(np.uint8), cv2.COLOR_BGR2RGB))
    return init_img
    

def extend_image(image, direction, pixels = 128, sd_steps = 50, prompt = "", scale=0.75):
    # img_file = "/home/ec2-user/TGS Nivea 300822-Main-Shot 03-0218 copy.jpg"
    # direction = ["up","down","left", "right"]
    Pixels = pixels
    Mask_merge = 10

    # image = Image.open(img_file)
    # dim = 720
    # height_percent = (dim / float(image.size[0]))
    # width_size = int((float(image.size[1]) * float(height_percent)))
    # image = image.resize((dim, width_size))
    img, msk = outpaint_help(image, direction, Pixels, Mask_merge)
    inp = {'image':img, 'mask':msk}
    out = predict(inp, sd_steps = sd_steps, prompt = prompt, scale = scale)
    return out

if __name__=="__main__":
    img_file = "/home/ec2-user/TGS Nivea 300822-Main-Shot 03-0218 copy.jpg"
    direction = ["up","down","left", "right"]
    Pixels = 128
    Mask_merge = 10

    image = Image.open(img_file)
    dim = 720
    height_percent = (dim / float(image.size[0]))
    width_size = int((float(image.size[1]) * float(height_percent)))
    image = image.resize((dim, width_size))
    img, msk = outpaint_help(image, direction, Pixels, Mask_merge)
    inp = {'image':img, 'mask':msk}
    out = predict(inp)
    out.save("/home/ec2-user/output_outpaint.png")