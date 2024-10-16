from flask import Flask
import multiprocessing
import routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Register routes from routes module
app.add_url_rule("/", view_func=routes.hello)
app.add_url_rule("/train", view_func=routes.train, methods=["POST"])
app.add_url_rule("/train_wgan_gp", view_func=routes.train_wgan_gp_api, methods=["POST"])
app.add_url_rule("/train_wgan", view_func=routes.train_wgan_api, methods=["POST"])
app.add_url_rule("/generate_dcgan", view_func=routes.generate_dcgan, methods=["GET"])
app.add_url_rule("/generate_wgan_gp", view_func=routes.generate_wgangp, methods=["GET"])
app.add_url_rule("/generate_wgan", view_func=routes.generate_wgan, methods=["GET"])
app.add_url_rule("/image/<filename>", view_func=routes.get_image, methods=["GET"])
app.add_url_rule("/generated_images", view_func=routes.list_generated_images, methods=["GET"])
app.add_url_rule("/output/generated_images_dcgan/<filename>", view_func=routes.send_generated_image_dcgan, methods=["GET"])
app.add_url_rule("/output/generated_images_wgan/<filename>", view_func=routes.send_generated_image_wgan, methods=["GET"])
app.add_url_rule("/output/generated_images_wgangp/<filename>", view_func=routes.send_generated_image_wgangp, methods=["GET"])

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    app.run(debug=True)
