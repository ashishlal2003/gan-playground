from flask import Flask, jsonify, request, send_file, send_from_directory
import os
from dotenv import load_dotenv
from train.train_dcgan import train_dcgan, generate_images
from train.train_wgan_gp import train_wgan_gp
from train.train_wgan import train_wgan
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


@app.route("/generate", methods=["GET"])
def generate():
    num_images = int(request.json.get("num_images", 1))
    model_path = os.path.join("model_files_dir_dcgan", "netG.pth")
    fake_images = generate_images(num_images, model_path)
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
