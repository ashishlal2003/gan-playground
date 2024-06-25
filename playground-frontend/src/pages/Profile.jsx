// src/pages/Playground.jsx

import React, { useState } from 'react';

const Playground = () => {
    const [learningRate, setLearningRate] = useState(0.0002);
    const [epochs, setEpochs] = useState(50);
    const [noiseDim, setNoiseDim] = useState(100);

    const handleGenerate = () => {
        // Placeholder for generating images
        console.log('Generating images with settings:', { learningRate, epochs, noiseDim });
    };

    return (
        <div className="container mx-auto px-4 py-8">
            <h1 className="text-4xl font-bold mb-4">GAN Playground</h1>
            <div className="grid grid-cols-1 gap-4 sm:grid-cols-3">
                <div>
                    <label className="block mb-2">Learning Rate</label>
                    <input
                        type="range"
                        min={0.0001}
                        max={0.001}
                        step={0.0001}
                        value={learningRate}
                        onChange={(e) => setLearningRate(parseFloat(e.target.value))}
                        className="w-full"
                    />
                    <p className="text-sm">{learningRate}</p>
                </div>
                <div>
                    <label className="block mb-2">Epochs</label>
                    <input
                        type="range"
                        min={10}
                        max={100}
                        step={10}
                        value={epochs}
                        onChange={(e) => setEpochs(parseInt(e.target.value))}
                        className="w-full"
                    />
                    <p className="text-sm">{epochs}</p>
                </div>
                <div>
                    <label className="block mb-2">Noise Dimension</label>
                    <input
                        type="range"
                        min={50}
                        max={200}
                        step={10}
                        value={noiseDim}
                        onChange={(e) => setNoiseDim(parseInt(e.target.value))}
                        className="w-full"
                    />
                    <p className="text-sm">{noiseDim}</p>
                </div>
            </div>
            <button
                className="mt-4 bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
                onClick={handleGenerate}
            >
                Generate
            </button>
            {/* Add a section to display generated images here */}
        </div>
    );
}

export default Playground;
