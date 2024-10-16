from flask import Flask, jsonify, request, send_file, send_from_directory
import os
from dotenv import load_dotenv
from train.train_dcgan import train_dcgan, generate_images as generate_images_dcgan
from train.train_wgan_gp import train_wgan_gp, generate_images as generate_images_wgan_gp
from train.train_wgan import train_wgan, generate_images as generate_images_wgan
from torchvision.utils import save_image

app = Flask(__name__)

load_dotenv()

@app.route("/")
def hello():
    return "Hello, World!"

dataset_path = os.getenv("DATASET_PATH")

## TRAINING ROUTES

@app.route("/train", methods=["POST"])
def train():
    data = request.json
    num_epochs = data.get("num_epochs", 5)
    lr = data.get("lr", 0.0005)
    nz = data.get("nz", 100)
    dataroot = dataset_path
    print("Training starting...")
    train_dcgan(dataroot, num_epochs, lr, nz)
    return jsonify({"message": "Training started"}), 200

@app.route("/train_wgan_gp", methods=["POST"])
def train_wgan_gp_api():
    data = request.json
    num_epochs = data.get("num_epochs", 5)
    lr = data.get("lr", 0.00005)
    nz = data.get("nz", 100)
    clip_value = data.get("clip_value", 0.01)
    critic_iters = data.get("critic_iters", 5)
    dataroot = dataset_path

    print("WGAN GP training starting...")
    train_wgan_gp(dataroot, num_epochs, lr, nz, clip_value, critic_iters)
    return jsonify({"message": "WGAN GP training started"}), 200

@app.route("/train_wgan", methods=["POST"])
def train_wgan_api():
    data = request.json
    num_epochs = data.get("num_epochs", 5)
    lr = data.get("lr", 0.00005)
    nz = data.get("nz", 100)
    dataroot = dataset_path

    print("WGAN training starting...")
    train_wgan(dataroot, num_epochs, lr, nz)
    return jsonify({"message": "WGAN training started"}), 200

## GENERATION ROUTES

@app.route("/generate_dcgan", methods=["GET"])
def generate_dcgan():
    # Get the number of images from query parameters
    num_images = int(request.args.get("num_images", 1))  # Changed to request.args
    model_path = os.path.join("model_files_dir_dcgan", "netG.pth")
    fake_images = generate_images_dcgan(num_images, model_path)
    output_dir = "output/generated_images_dcgan"
    os.makedirs(output_dir, exist_ok=True)
    file_paths = []
    for i, image in enumerate(fake_images):
        file_path = os.path.join(output_dir, f"generated_image_{i}.png")
        save_image(image, file_path, normalize=True)
        print(f"Saved image: {file_path}")
        file_paths.append(f"generated_image_{i}.png")  # Just keep the filename
    return jsonify({"images": file_paths}), 200

@app.route("/generate_wgan", methods=["GET"])
def generate_wgan():
    # Get the number of images from query parameters
    num_images = int(request.args.get("num_images", 1))  # Changed to request.args
    model_path = os.path.join("model_files_dir_wgan", "netG.pth")
    fake_images = generate_images_wgan(num_images, model_path)
    output_dir = "output/generated_images_wgan"
    os.makedirs(output_dir, exist_ok=True)
    file_paths = []
    for i, image in enumerate(fake_images):
        file_path = os.path.join(output_dir, f"generated_image_{i}.png")
        save_image(image, file_path, normalize=True)
        print(f"Saved image: {file_path}")
        file_paths.append(f"generated_image_{i}.png")  # Just keep the filename
    return jsonify({"images": file_paths}), 200

@app.route("/generate_wgangp", methods=["GET"])
def generate_wgangp():
    # Get the number of images from query parameters
    num_images = int(request.args.get("num_images", 1))  # Changed to request.args
    model_path = os.path.join("model_files_dir_wgangp", "netG.pth")
    fake_images = generate_images_wgan_gp(num_images, model_path)
    output_dir = "output/generated_images_wgangp"
    os.makedirs(output_dir, exist_ok=True)
    file_paths = []
    for i, image in enumerate(fake_images):
        file_path = os.path.join(output_dir, f"generated_image_{i}.png")
        save_image(image, file_path, normalize=True)
        print(f"Saved image: {file_path}")
        file_paths.append(f"generated_image_{i}.png")  # Just keep the filename
    return jsonify({"images": file_paths}), 200

## IMAGE ROUTES

@app.route("/output/generated_images_dcgan/<path:filename>", methods=["GET"])
def send_generated_image_dcgan(filename):
    return send_from_directory("output/generated_images_dcgan", filename)

@app.route("/output/generated_images_wgan/<path:filename>", methods=["GET"])
def send_generated_image_wgan(filename):
    return send_from_directory("output/generated_images_wgan", filename)

@app.route("/output/generated_images_wgangp/<path:filename>", methods=["GET"])
def send_generated_image_wgangp(filename):
    return send_from_directory("output/generated_images_wgangp", filename)

## FETCHING IMAGES FOR PLAYGROUND ROUTES

@app.route("/generated_images", methods=["GET"])
def list_generated_images():
    os.makedirs("output/generated_images_dcgan", exist_ok=True)
    os.makedirs("output/generated_images_wgan", exist_ok=True)
    os.makedirs("output/generated_images_wgangp", exist_ok=True)

    image_dir = "output"
    images = [img for img in os.listdir(image_dir) if img.endswith(".png")]
    return jsonify({"images": images})

@app.route("/image/<filename>", methods=["GET"])
def get_image(filename):
    return send_file(os.path.join("output", filename), mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)
