from flask import Flask, jsonify, request, send_file
import os
from train.train_dcgan import train_dcgan, generate_images
from torchvision.utils import save_image

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/train', methods=['POST'])
def train():
    num_epochs = request.json.get('num_epochs', 5)
    dataroot = r"C:\Users\ashis\Mirror\Important_files\IIIT\Machine Learning - Personal\Generative Adveserial Networks\DCGAN\celeb_dataset"
    print("Training starting...")
    train_dcgan(dataroot, num_epochs)
    return jsonify({"message": "Training started"}), 200


@app.route('/generate', methods=['GET'])
def generate():
    num_images = int(request.args.get('num_images', 1))
    fake_images = generate_images(num_images)
    output_dir = 'output/generated_images'
    os.makedirs(output_dir, exist_ok=True)
    file_paths = []
    for i, image in enumerate(fake_images):
        file_path = os.path.join(output_dir, f'generated_image_{i}.png')
        save_image(image, file_path, normalize=True)
        file_paths.append(file_path)
    return jsonify({"images": file_paths}), 200

@app.route('/image/<filename>', methods=['GET'])
def get_image(filename):
    return send_file(os.path.join('output/generated_images', filename), mimetype='image/png')

@app.route('/generated_images', methods=['GET'])
def list_generated_images():
    image_dir = 'output/generated_images'
    images = [img for img in os.listdir(image_dir) if img.endswith('.png')]
    return jsonify({"images": images})
