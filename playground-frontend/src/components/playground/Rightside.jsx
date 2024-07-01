import React, { useState } from 'react';

export default function Rightside() {
    const [learningRate, setLearningRate] = useState(0.0002);
    const [epochs, setEpochs] = useState(50);
    const [noiseDim, setNoiseDim] = useState(100);

    const handleGenerate = () => {
        // Placeholder for generating images
        console.log('Generating images with settings:', { learningRate, epochs, noiseDim });
    };

    const [selectedModel, setSelectedModel] = useState('');

    const handleChange = (event) => {
        setSelectedModel(event.target.value);
    };
    return (
        <div className='w-[20%]'>
            <div className="bg-[#111113] w-[100%] h-full text-white flex flex-col items-center border-gray-100 border-l-[1px] border-solid">
                <div className="m-8">
                    <select
                        id="model"
                        value={selectedModel}
                        onChange={handleChange}
                        className="block w-full p-2.5 px-3 border border-gray-300 rounded-md bg-white text-gray-700 focus:ring-blue-500 focus:border-blue-500"
                    >
                        <option value="" disabled>Select a model</option>
                        <option value="WGAN">WGAN</option>
                        <option value="GAN">GAN</option>
                    </select>
                    {selectedModel && (
                        <p className="mt-3 text-sm text-gray-700">
                            Selected Model: <span className="font-medium text-blue-500">{selectedModel}</span>
                        </p>
                    )}
                </div>

                <div className="grid grid-cols-1 gap-4 sm:grid-rows-3 p-5">
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
            </div>
        </div>
    )
}
