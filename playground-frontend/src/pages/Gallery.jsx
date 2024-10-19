import React, { useState } from 'react';
import axios from 'axios';

function Gallery() {
  const [selectedModel, setSelectedModel] = useState('');
  const [generatedImages, setGeneratedImages] = useState([]);

  const handleChange = (e) => {
    setSelectedModel(e.target.value);
  };

  const handleGeneratedImages = async () => {
      if (!selectedModel) {
        alert('Please select a model first');
        return;
      }

      try {
          const response = await axios.get(`https://gan-playground-flask-app.onrender.com/generate_${selectedModel}`, {
              params: {
                  num_images: 1
              }
          });
          const newImageName = response.data.images[0]; // Assuming this is the name of the new image
          const timestamp = new Date().getTime(); // Create a unique timestamp
          setGeneratedImages([`${newImageName}?t=${timestamp}`]); // Append timestamp to the image URL
      } catch (error) {
          console.log("Error generating images:", error);
      }
  };

  return (
    <div className="bg-gray-900 text-white w-full h-screen flex flex-col items-center px-4">
      <div className='h-[70%] w-full max-w-5xl mt-24 md:mt-44 flex flex-col md:flex-row shadow-lg rounded-lg overflow-hidden bg-gray-800'>
        
        {/* Left Section: Model Selection */}
        <div className='h-auto w-full md:w-1/2 p-6 md:p-8 flex flex-col items-center justify-center'>
          <h1 className='text-lg md:text-2xl font-bold mb-4'>Generate Images</h1>
          <select
            id="model"
            value={selectedModel}
            onChange={handleChange}
            className="block w-full md:w-2/3 p-2 md:p-3 border border-gray-300 rounded-md bg-white text-gray-700 focus:ring-blue-500 focus:border-blue-500"
          >
            <option value="" disabled>Select a model</option>
            <option value="dcgan">DCGAN</option>
            <option value="wgan">WGAN</option>
            <option value="wgangp">WGAN_GP</option>
            <option value="GAN">GAN</option>
          </select>
          {selectedModel && (
            <p className="mt-4 text-sm md:text-lg">You selected: <span className="font-semibold">{selectedModel}</span></p>
          )}
           <button
            onClick={handleGeneratedImages}
            className="mt-4 p-2 w-full md:w-auto bg-blue-600 text-white rounded-md hover:bg-blue-700"
          >
            Generate Image
          </button>
        </div>

        {/* Right Section: Image Display */}
        <div className='h-auto w-full md:w-1/2 p-6 md:p-8 flex flex-col items-center justify-center'>
          <p className="text-sm md:text-lg mb-4">Generated Images</p>
          <div className="flex flex-wrap justify-center">
              {generatedImages.length === 0 ? (
                <p className="text-gray-400">No images yet.</p>
              ) : (
                generatedImages.map((image, index) => (
                    <img
                        key={index}
                        src={`https://gan-playground-flask-app.onrender.com/output/generated_images_${selectedModel}/${image}`}
                        className="h-32 w-32 md:h-48 md:w-48 lg:h-64 lg:w-64 rounded-md m-2"
                        alt={`Generated ${index + 1}`}
                    />
                ))
              )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Gallery;
