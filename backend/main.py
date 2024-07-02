from flask import Flask
import multiprocessing
import routes

app = Flask(__name__)

# Register routes from routes module
app.add_url_rule('/', view_func=routes.hello)
app.add_url_rule('/train', view_func=routes.train, methods=['POST'])
app.add_url_rule('/generate', view_func=routes.generate, methods=['GET'])
app.add_url_rule('/image/<filename>', view_func=routes.get_image, methods=['GET'])
app.add_url_rule('/generated_images', view_func=routes.list_generated_images, methods=['GET'])

if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    app.run(debug=True)
