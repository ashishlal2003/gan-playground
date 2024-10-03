from flask import Flask, jsonify, request, send_file, send_from_directory
import os
from dotenv import load_dotenv
from train.train_dcgan import train_dcgan, generate_images
from train.train_wgan_gp import train_wgan_gp, generate_images_wgan
from train.train_wgan import train_wgan
from train.train_cgan import train_cgan
from train.train_vgan import train_vanilla_gan
from train.train_cycleGan import train_cyclegan
from torchvision.utils import save_image

app = Flask(__name__)
load_dotenv()
@app.route("/")
def hello():
    return "Hello, World!"

dataset_path = os.getenv("DATASET_PATH")


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
    # clip_value = data.get("clip_value", 0.01)
    # critic_iters = data.get("critic_iters", 5)
    dataroot = dataset_path

    print("WGAN training starting...")
    train_wgan(dataroot, num_epochs, lr, nz)
    return jsonify({"message": "WGAN training started"}), 200


@app.route("/train_cgan", methods=["POST"])
def train_cgan_api():
    data = request.json
    num_epochs = data.get("num_epochs", 5)
    lr = data.get("lr", 0.0002)
    nz = data.get("nz", 100)
    dataroot = dataset_path
    print("CGAN Training starting...")
    train_cgan(dataroot, num_epochs, lr, nz)
    return jsonify({"message": "CGAN training started"}), 200

@app.route("/train_vgan", methods=["POST"])
def train_vanilla_gan_api():
    data = request.json
    num_epochs = data.get("num_epochs", 5)
    lr = data.get("lr", 0.0002)
    nz = data.get("nz", 100)
    dataroot = dataset_path
    print("Vanilla GAN Training starting...")
    train_vanilla_gan(dataroot, num_epochs, lr, nz)
    return jsonify({"message": "Vanilla GAN training started"}), 200

@app.route("/train_cyclegan", methods=["POST"])
def train_cyclegan_api():
    data = request.json
    num_epochs = data.get("num_epochs", 5)
    lr = data.get("lr", 0.0002)
    lambda_cycle = 10.0
    lambda_identity =  0.5
    dataroot = dataset_path
    print("CycleGAN Training starting...")
    dataroot = dataset_path
    # Check if dataset paths exist
    if not os.path.exists(dataroot) or not os.path.exists(dataroot):
        return jsonify({"error": "Dataset paths are invalid."}), 400

    # Start training CycleGAN
    train_cyclegan(dataroot, dataroot, num_epochs, lr, lambda_cycle, lambda_identity)

    return jsonify({"message": "CycleGAN training started"}), 200


@app.route("/generate", methods=["GET"])
def generate():
    num_images = int(request.json.get("num_images", 1))
    fake_images = generate_images(num_images)
    output_dir = "output/generated_images"
    os.makedirs(output_dir, exist_ok=True)
    file_paths = []
    for i, image in enumerate(fake_images):
        file_path = os.path.join(output_dir, f"generated_image_{i}.png")
        save_image(image, file_path, normalize=True)
        file_paths.append(file_path)
    return jsonify({"images": file_paths}), 200


@app.route("/image/<filename>", methods=["GET"])
def get_image(filename):
    return send_file(os.path.join("output", filename), mimetype="image/png")


# @app.route("/image/<filename>", methods=["GET"])
# def get_image(filename):
#     return send_file(
#         os.path.join("output/generated_images", filename), mimetype="image/png"
#     )


# @app.route("/generated_images", methods=["GET"])
# def list_generated_images():
#     image_dir = "output/generated_images"
#     images = [img for img in os.listdir(image_dir) if img.endswith(".png")]
#     return jsonify({"images": images})


@app.route("/generated_images", methods=["GET"])
def list_generated_images():
    image_dir = "output"
    images = [img for img in os.listdir(image_dir) if img.endswith(".png")]
    return jsonify({"images": images})
