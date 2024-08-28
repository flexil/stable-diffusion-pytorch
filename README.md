# stable-diffusion-pytorch
A Python implementation of the Stable Diffusion model for generating images using PyTorch.
This repository contains a Python script that utilizes the Stable Diffusion model to generate images based on provided prompts.

Prerequisites

Python 3.x
PyTorch
Transformers
Diffusers
Clip
Accelerate
Matplotlib
Installation

To install the required libraries, run the following command:

pip install pytorch-fid torch diffusers clip transformers accelerate matplotlib
Usage

Replace the model_id variable in the script with your desired model ID.
Add your desired prompts to the prompts list.
Run the script using the command: python stable_diff.py
Example

Model ID: CompVis/stable-diffusion-v1-4
Prompts: ["A photo of a cat", "A painting of a sunset"]
Script Overview

The script consists of two main functions:

load_model: Loads the Stable Diffusion model with the provided model ID and device.
generate_images: Generates images based on the provided prompts using the loaded model.
The script also includes a main section that demonstrates how to use these functions to generate images.


Device Support

The script supports the following devices:

CPU
CUDA (GPU)
MPS (M1 Macs)
Note that the autocast feature is not supported on MPS devices.

Output

The generated images will be saved in the ./img directory with the prefix pil_image. The images will also be rendered using the render_images function.

Utilities

The script uses the following utility functions:

render_images: Renders the generated images.
save_pil_images: Saves the generated images as PIL images.

Here are the steps to run the code:

Prerequisites

Make sure you have Python 3.x installed on your system.
Install the required libraries by running the following command in your terminal:
pip install pytorch-fid torch diffusers clip transformers accelerate matplotlib
Step 1: Clone the repository (if you haven't already)

If you haven't already, clone the repository to your local machine using the following command:

git clone https://github.com/your-username/your-repo-name.git
Step 2: Navigate to the repository directory

Navigate to the directory where the repository is cloned:

cd your-repo-name
Step 3: Edit the script (optional)

If you want to change the model ID or prompts, open the stable_diff.py file in a text editor and modify the model_id and prompts variables as needed.

Step 4: Run the script

Run the script using the following command:

python stable_diff.py
Step 5: Wait for the images to be generated

The script will take some time to generate the images. You can monitor the progress by looking at the output in the terminal.

Step 6: View the generated images

Once the script has finished running, you can view the generated images in the ./img directory. The images will be saved with the prefix pil_image.

That's it! If you encounter any issues or errors, feel free to ask.
