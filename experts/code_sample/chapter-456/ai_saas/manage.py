from flask_cors import CORS
from flask import Flask, request, jsonify
from io import BytesIO
from PIL import Image

import os
import sys
import wget

from ai_pipeline import run

app = Flask(__name__)
CORS(app)

def download_image(img_url, image_path="test.jpg"):
    wget.download(img_url, image_path)
    return image_path

@app.route('/tf2/ai_saas', methods=["POST"])
def ai_saas():
    data = request.get_json()
    # 下载图像文件
    image_path = download_image(data["image_url"])
    # 商品检测和识别
    sku_list = run(image_path)
    
    return jsonify(sku_list)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=9000, threaded=False)

# curl -H "Content-Type: application/json" --data @body.json http://localhost:9000/tf2/ai_saas