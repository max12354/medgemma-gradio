# medgemma-gradio
MedGemma Radiology Assistant with Gradio
## ⚠️ Requirements

- A CUDA-compatible GPU (recommended 16GB VRAM or more)
- [Hugging Face](https://huggingface.co/) account access to the gated model: [google/medgemma-4b-it](https://huggingface.co/google/medgemma-4b-it)

> 💡 Request access to the model [here](https://huggingface.co/google/medgemma-4b-it) before running the app.


# 🧠 MedGemma Gradio App

[![GPU Required](https://img.shields.io/badge/GPU-required-blue?logo=nvidia)](#requirements)
[![Hugging Face Access](https://img.shields.io/badge/HuggingFace-model--access-yellow?logo=huggingface)](https://huggingface.co/google/medgemma-4b-it)
[![Built with Gradio](https://img.shields.io/badge/Built%20with-Gradio-orange?logo=gradio)](https://gradio.app/)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python)](https://www.python.org/)

> A Gradio-powered AI assistant using Google's MedGemma-4B multimodal model for medical image analysis.

## 🖼️ Demo

Here’s how the MedGemma Gradio app works:

![MedGemma AI Demo](./Screenshot.png)



A Gradio-powered app using Google's MedGemma-4B model for medical image analysis.

## 🌟 Features
- Upload medical radiology images
- Enter a prompt
- Get an AI-generated diagnostic response

## 🚀 How to Run

```bash
git clone https://github.com/max12354/medgemma-gradio.git
cd medgemma-gradio
pip install -r requirements.txt
python med.py

---

### ⚠️ Requirements

To run this app, you'll need:

- A GPU with at least 16GB of memory
- Access to the gated Hugging Face model: [google/medgemma-4b-it]
(https://huggingface.co/google/medgemma-4b-it)

You must request access from Hugging Face before using the model.
