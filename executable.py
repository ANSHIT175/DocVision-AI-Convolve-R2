import os
import json
import argparse
from PIL import Image
import pytesseract
import re

def preprocess_image(img_path):
    img = Image.open(img_path)
    img = img.convert("L")
    return img

def extract_fields(text):
    result = {
        "dealer_name": None,
        "model_name": None,
        "horse_power": None,
        "asset_cost": None,
        "signature": {"present": False, "bbox": None},
        "stamp": {"present": False, "bbox": None}
    }

    lines = text.split("\n")

    for line in lines:
        l = line.lower()

        if "dealer" in l and result["dealer_name"] is None:
            result["dealer_name"] = line.strip()

        if "model" in l and result["model_name"] is None:
            result["model_name"] = line.strip()

        hp = re.search(r'(\d+)\s*hp', l)
        if hp and result["horse_power"] is None:
            result["horse_power"] = int(hp.group(1))

        cost = re.search(r'(\d{4,})', l)
        if cost and result["asset_cost"] is None:
            result["asset_cost"] = int(cost.group(1
