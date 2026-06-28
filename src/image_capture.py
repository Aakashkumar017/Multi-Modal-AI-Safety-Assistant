import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image


@st.cache_resource(show_spinner=False)
def _load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model


def generate_caption(image: Image.Image) -> str:
    processor, model = _load_model()

    inputs = processor(image, return_tensors="pt")
    output = model.generate(**inputs, max_new_tokens=80)
    caption = processor.decode(output[0], skip_special_tokens=True)

    return caption