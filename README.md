# Stable Diffusion Image Generation Repository
=====================================================

This repository contains a Python script for generating images using the Stable Diffusion model. It leverages the diffusers library to interact with the Stable Diffusion pipeline and create images based on textual prompts.

## Prerequisites

Before running the script, make sure you have the necessary Python packages installed. You can install them using the following command:

```bash
pip install pytorch-fid torch diffusers clip transformers accelerate matplotlib

```
## Code Overview

* Dependencies

torch: PyTorch framework.
diffusers: Library for using diffusion models.
clip: Contrastive Language-Image Pretraining.
transformers: Hugging Face transformers library.
accelerate: Library for managing distributed computing.
matplotlib: Plotting library for visualizations.

## Functions

load_model(model_id: str, device="cpu") -> StableDiffusionPipeline

Loads the Stable Diffusion model pipeline from the specified model_id and places it on the specified device (CPU, CUDA, or MPS).

generate_images(pipe: StableDiffusionPipeline, prompts: List[str], device="cuda") -> List[PIL.Image.Image]

Generates images from a list of prompts using the provided Stable Diffusion pipeline. Supports automatic casting for performance optimization.

## Main Script Execution

Model Initialization: The script initializes the Stable Diffusion model using the specified model_id.

Prompt Definition: Prompts for image generation are defined.

Device Selection: The device is selected (e.g., "cpu", "cuda", "mps" for M1 Macs).

Image Generation: The script generates images from the prompts.

Saving and Rendering: Generated images are saved to a specified directory and rendered.

## Running the Script

To run the script, execute the following command in your terminal:

python3  stable_diff.py


## Configuration

Model ID: Default is "CompVis/stable-diffusion-v1-4". You can change this to use a different model version.

Device: Set the device variable to "cuda" for NVIDIA GPUs, "cpu" for CPU, or "mps" for Apple Silicon Macs.

Output
The generated images are saved in the `./img
