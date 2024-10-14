import React, { useState } from 'react';

function Gallery() {
  const [selectedModel, setSelectedModel] = useState('');

  const handleChange = (e) => {
    setSelectedModel(e.target.value);
  };

  return (
    <div className="bg-gray-900 text-white w-full h-screen flex flex-col items-center px-4">
      <div className='h-[60%] w-full max-w-5xl mt-52 flex flex-col md:flex-row shadow-lg rounded-lg overflow-hidden bg-gray-800'>
        {/* Left Section: Model Selection */}
        <div className='h-full flex-1 flex flex-col items-center justify-center p-8'>
          <h1 className='text-2xl font-bold mb-4'>Generate Images</h1>
          <select
            id="model"
            value={selectedModel}
            onChange={handleChange}
            className="block w-full md:w-2/3 p-3 border border-gray-300 rounded-md bg-white text-gray-700 focus:ring-blue-500 focus:border-blue-500"
          >
            <option value="" disabled>Select a model</option>
            <option value="DCGAN">DCGAN</option>
            <option value="WGAN">WGAN</option>
            <option value="WGAN_GP">WGAN_GP</option>
            <option value="GAN">GAN</option>
          </select>
          {selectedModel && (
            <p className="mt-4 text-lg">You selected: <span className="font-semibold">{selectedModel}</span></p>
          )}
        </div>

        {/* Right Section: Image Display */}
        <div className='h-full flex-1 flex items-center justify-center p-8'>
          <div className="flex flex-col items-center justify-center">
            <p className="text-lg mb-4">Generated Image Appears Here</p>
            <div className="bg-gray-700 h-48 w-48 md:h-64 md:w-64 rounded-md flex items-center justify-center">
              <span className="text-gray-400">[Image Placeholder]</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Gallery;
