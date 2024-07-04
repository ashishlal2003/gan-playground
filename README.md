# GAN Playground

Welcome to the GAN Playground! This project allows users to explore and experiment with Generative Adversarial Networks (GANs) through an interactive web interface. Users can choose different GAN models, set training parameters, and visualize the results.

## Website
Visit the GAN Playground at [gan-playground.vercel.app](https://gan-playground.vercel.app)

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Frontend](#frontend)
  - [Backend](#backend)
- [API Endpoints](#api-endpoints)
  - [DCGAN](#dcgan)
  - [WGAN-GP](#wgan-gp)
  - [Future Models](#future-models)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features
- Choose from multiple GAN models (DCGAN, WGAN-GP, and more coming soon).
- Set training parameters such as number of epochs, learning rate, etc.
- Visualize training progress and results at each step of every epoch.
- API access to integrate GAN functionalities into other projects.

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm 6+

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/gan-playground.git
    cd gan-playground
    ```

2. **Backend setup:**
    ```bash
    cd backend
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Frontend setup:**
    ```bash
    cd ../frontend
    npm install
    ```

## Usage

### Frontend
To start the frontend:
```bash
cd playground-frontend
npm start
```

This will start the React app on `localhost:3000`.

### Backend
To start the backend on a new terminal:
```bash
cd backend
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
python main.py
```

This will start the React app on `localhost:5000`.

## API Endpoints

### DCGAN
- **Endpoint:** `/api/dcgan/train`
  - **Method:** `POST`
  - **Description:** Train the DCGAN model with the provided parameters.
  - **Parameters:**
    - `epochs` (int): Number of epochs to train.
    - `batch_size` (int): Batch size for training.
    - `learning_rate` (float): Learning rate for the optimizer.
  - **Example Request:**
    ```json
    {
      "epochs": 100,
      "batch_size": 64,
      "learning_rate": 0.0002
    }
    ```

### WGAN-GP
- **Endpoint:** `/api/wgan_gp/train`
  - **Method:** `POST`
  - **Description:** Train the WGAN-GP model with the provided parameters.
  - **Parameters:**
    - `epochs` (int): Number of epochs to train.
    - `batch_size` (int): Batch size for training.
    - `learning_rate` (float): Learning rate for the optimizer.
  - **Example Request:**
    ```json
    {
      "epochs": 100,
      "batch_size": 64,
      "learning_rate": 0.0001
    }
    ```

### Future Models
Additional models will be added soon. Stay tuned for updates!

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements
- [TensorFlow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)
- [React](https://reactjs.org/)
- [Flask](https://flask.palletsprojects.com/)
