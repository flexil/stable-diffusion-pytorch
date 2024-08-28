# !pip install pytorch-fid torch diffusers clip transformers accelerate matplotlib

from typing import List
import torch
from diffusers import StableDiffusionPipeline
from util import render_images, save_pil_images, DEMO_PROMPTS
import PIL


def load_model(model_id: str, device="cpu") -> StableDiffusionPipeline:
    
    return StableDiffusionPipeline.from_pretrained(
        model_id, torch_dtype=torch.float16, revision="fp16", use_auth_token=False
    ).to(device)


def generate_images(
    pipe: StableDiffusionPipeline, prompts: List[str], device="cuda"
) -> List[PIL.Image.Image]:
    """Generate images based on provided prompts."""
    with torch.autocast(device):
        images = pipe(prompts).images
    return images


if __name__ == "__main__":


    model_id = "CompVis/stable-diffusion-v1-4"
    prompts = DEMO_PROMPTS

    device = "mps"  # "cuda", "cpu", "mps" is for M1 Macs
    pipe = load_model(model_id, device="mps")
    images = generate_images(
        pipe, prompts, device="cpu"
    )  # autocast does not support mps

    # Save the images
    save_pil_images(images, "./img", prefix="pil_image")

    # render the images
    render_images(images)
