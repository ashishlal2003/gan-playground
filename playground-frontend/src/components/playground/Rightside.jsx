import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function Rightside({ selectedDataset }) {
    const [learningRate, setLearningRate] = useState(0.0002);
    const [num_epochs, setnum_epochs] = useState(50);
    const [noiseDim, setNoiseDim] = useState(100);
    const [selectedModel, setSelectedModel] = useState('');

    const handleTrain = async () => {
        if (selectedModel === 'DCGAN') {
            console.log('Generating images with settings:', { learningRate, num_epochs, noiseDim, selectedDataset });
    
            try {
                const res = await axios.post('http://localhost:5000/train', {
                    num_epochs,
                    lr: learningRate,
                    nz: noiseDim,
                    dataroot: selectedDataset
                });
                console.log(res.data);
            } catch (err) {
                console.log(err);
            }
        }
    };
    

    const handleChange = (event) => {
        setSelectedModel(event.target.value);
    };

    return (
        <div className='w-[20%] hidden sm:block'>
            <div className="bg-[#111113] w-[100%] h-screen text-white flex flex-col items-center border-gray-100 border-l-[1px] border-solid">
                <div className="m-8">
                    <select
                        id="model"
                        value={selectedModel}
                        onChange={handleChange}
                        className="block w-full p-2.5 px-3 border border-gray-300 rounded-md bg-white text-gray-700 focus:ring-blue-500 focus:border-blue-500"
                    >
                        <option value="" disabled>Select a model</option>
                        <option value="DCGAN">DCGAN</option>
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
                        <label className="block mb-2">Number of Epochs</label>
                        <input
                            type="range"
                            min={10}
                            max={100}
                            step={10}
                            value={num_epochs}
                            onChange={(e) => setnum_epochs(parseInt(e.target.value))}
                            className="w-full"
                        />
                        <p className="text-sm">{num_epochs}</p>
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
                    onClick={handleTrain}
                >
                    Train on Dataset
                </button>
            </div>
        </div>
    );
}
