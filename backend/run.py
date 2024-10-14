from waitress import serve
from main import app  # Ensure this points to your Flask app

serve(app, host='0.0.0.0', port=5000)
