import requests
import time
import os

def txt2img(
        key:str=None,
        prompt:str="kittens on cloud",
        negative_prompt:str="bad drawn, low quality, low detailed, ugly, mutated, blurry, watermark",
        model:str="deliberate_v2.safetensors [10ec4b29]",
        sampler:str="Heun",
        aspect_ratio:str="square",
        steps:int=25,
        cfg_scale:int=7,
        seed:int=-1,
        upscale:bool=False):
    if key is None:
        print("API key cant be None, get your API kay at https://app.prodia.com/api")
    else:
        if prompt == "kittens on cloud":
            print("Prompt wasnt not defined, used default (kittens on cloud)")
        url = "https://api.prodia.com/v1/job"
        payload = {
            "prompt": prompt,
            "model": model,
            "sampler": sampler,
            "negative_prompt": negative_prompt,
            "steps": steps,
            "cfg_scale": cfg_scale,
            "seed": seed,
            "upscale": upscale,
            "aspect_ratio": aspect_ratio
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-Prodia-Key": key
        }
        headersrecieve = {
            "accept": "application/json",
            "X-Prodia-Key": key
        }
        print(f"txt2img image with params:\n{payload}")
        response = requests.post(url, json=payload, headers=headers)
        job_id = response.json()['job']
        time.sleep(5)

        rec_url = f'https://api.prodia.com/v1/job/{job_id}'
        stt = True
        while stt is True:
            rec = requests.get(rec_url, headers=headersrecieve)
            status = rec.json()['status']
            if status == "succeeded":
                print(f"Image {job_id} generated!")
                image_url = rec.json()['imageUrl']
                stt = False
                return image_url
            elif status == "queued":
                print("Still working...")
                time.sleep(5)
            elif status == "generating":
                print("Still working...")
                time.sleep(5)
            else:
                print(f"Something went wrong! Please try later, error: {status}")
                stt = False
                return status

def img2img(
        key:str=None,
        imageUrl:str=None,
        model:str="deliberate_v2.safetensors [10ec4b29]",
        prompt:str=None,
        denoising_strength:float=0.7,
        negative_prompt:str="badly drawn, low detailed, ugly, mutated, unralistic",
        steps:int=25,
        cfg_scale:int=7,
        seed:int=-1,
        upscale:bool=False,
        sampler:str="Heun"):
    if key is None:
        print("API key cant be None, get your API kay at https://app.prodia.com/api")
    elif imageUrl is None:
        print("Image URL is required and cannot be empty")
    elif prompt is None:
        print("Prompt is required and cannot be empty")
    else:
        url = "https://api.prodia.com/v1/transform"

        payload = {
            "steps": steps,
            "sampler": sampler,
            "imageUrl": imageUrl,
            "model": model,
            "prompt": prompt,
            "denoising_strength": denoising_strength,
            "negative_prompt": negative_prompt,
            "cfg_scale": cfg_scale,
            "seed": seed,
            "upscale": upscale
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-Prodia-Key": key
        }
        headersrecieve = {
            "accept": "application/json",
            "X-Prodia-Key": key
        }
        print(f"img2img image with params:\n{payload}")
        response = requests.post(url, json=payload, headers=headers)
        job_id = response.json()['job']
        time.sleep(5)

        rec_url = f'https://api.prodia.com/v1/job/{job_id}'
        stt = True
        while stt is True:
            rec = requests.get(rec_url, headers=headersrecieve)
            status = rec.json()['status']
            if status == "succeeded":
                print(f"Image {job_id} generated!")
                image_url = rec.json()['imageUrl']
                stt = False
                return image_url
            elif status == "queued":
                print("Still working...")
                time.sleep(5)
            elif status == "generating":
                print("Still working...")
                time.sleep(5)
            else:
                print(f"Something went wrong! Please try later, error: {status}")
                stt = False
                return status



