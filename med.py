import os
os.environ["TORCH_COMPILE_DISABLE"] = "1"  # Disable TorchDynamo to avoid tracing errors

import torch
from transformers import pipeline
import gradio as gr
from PIL import Image

# Set device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Device set to use {device}")

# Load MedGemma-4B image-text model
pipe = pipeline(
    "image-text-to-text",
    model="google/medgemma-4b-it",
    torch_dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32,
    device=device,
)

# Inference function
def analyze_image(image, prompt):
    messages = [
        {
            "role": "system",
            "content": [{"type": "text", "text": "You are an expert radiologist."}]
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image", "image": image}
            ]
        }
    ]

    with torch.no_grad():
        output = pipe(text=messages, max_new_tokens=200)

    return output[0]["generated_text"][-1]["content"]

# Gradio UI
gr.Interface(
    fn=analyze_image,
    inputs=[
        gr.Image(type="pil", label="Medical Image"),
        gr.Textbox(lines=2, label="Prompt")
    ],
    outputs=gr.Textbox(label="AI Radiology Response"),
    title="MedGemma Radiology Assistant",
    description="Upload a medical image and enter a prompt for AI analysis.",
    allow_flagging="never"
).launch()
