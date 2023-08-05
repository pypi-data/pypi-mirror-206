from model_manager import ModelManager
from skimage import exposure
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



def predict(dict, sd_mask_blur = 0, sd_steps = 50, prompt = "background", negative_prompt= "", scale=0.75):
    init_img =  dict['image'].convert("RGB")
    mask_img = dict['mask'].convert("L")
    # init_img = init_img.resize((int(init_img.size[0]/64)*64,int(init_img.size[1]/64)*64))
    # mask_img = mask_img.resize((int(init_img.size[0]/64)*64,int(init_img.size[1]/64)*64))
    cfg = get_config(HDStrategy.CROP, LDMSampler.plms, sd_mask_blur, sd_steps, prompt, negative_prompt, scale)
    
    with torch.inference_mode():
        init_img= control_model(np.array(init_img),np.array(mask_img.convert("L")), cfg)
    init_img = Image.fromarray(cv2.cvtColor(init_img.astype(np.uint8), cv2.COLOR_BGR2RGB))
    return init_img
    
def remove_product(image,mask, sd_steps = 50, prompt = "", scale=0.75):
    # dim = 720
    # height_percent = (dim / float(img.size[0]))
    # width_size = int((float(img.size[1]) * float(height_percent)))
    # img = img.resize((dim, width_size))
    # msk = msk.resize((dim, width_size))
    input = {'image':image, 'mask':mask}
    fg_removed = predict(input, sd_steps = sd_steps, prompt = prompt, scale = scale)
    return fg_removed
    # out.save("/home/ec2-user/output_inpaint.png")

# if __name__=="__main__":
#     img_file = "/home/ec2-user/folder1/shower-gel_1152_768.jpg"
#     msk_file = "/home/ec2-user/masks_m/shower-gel_1152_768_.jpg"

#     img = Image.open(img_file)
#     msk = Image.open(msk_file)

#     dim = 720
#     height_percent = (dim / float(img.size[0]))
#     width_size = int((float(img.size[1]) * float(height_percent)))
#     img = img.resize((dim, width_size))
#     msk = msk.resize((dim, width_size))
   
#     inp = {'image':img, 'mask':msk}
#     out = predict(inp)

    # matched = exposure.match_histograms(np.array(out), ((255 - np.array(msk))//255) * np.array(img) , multichannel=True)
    out.save("/home/ec2-user/output_before.png")
    # Image.fromarray(matched).save("/home/ec2-user/output_after.png")
    # print(((255 - np.array(msk))//255).max(), ((255 - np.array(msk))//255).shape)
    # Image.fromarray(((255 - np.array(msk))//255) * np.array(img)).save("/home/ec2-user/output_1.png")
    # Image.fromarray(np.array(out)*((np.array(msk))//255)).save("/home/ec2-user/output_2.png")
    # Image.fromarray(np.array(msk)).save("/home/ec2-user/output_3.png")