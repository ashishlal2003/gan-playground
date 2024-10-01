import React from 'react';

export default function Leftside({ onDatasetSelect, selectedDataset }) {
    
    const handleDatasetClick = (dataset) => {
        onDatasetSelect(dataset);
        console.log(`Clicked on ${dataset} dataset!`);
    };

    return (
        <div className="hidden sm:flex h-full w-[18%] border-gray-100 border-r-[1px] border-solid p-3  flex-col items-center bg-[#111111]">
            <h5 className='text-2xl mt-8'>GAN Playground</h5>
            <ul className='w-[70%] mt-10 flex flex-col'>
                <li className='text-gray-500 mb-4 font-bold'>Standard Dataset</li>
                <li className={`items-center p-2 text-gray-500 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600 hover:text-white cursor-pointer ${selectedDataset === 'Celeb' ? 'bg-gray-700 text-white' : ''}`} onClick={() => handleDatasetClick('Celeb')}>Celeb dataset</li>
                {/* <li className={`items-center p-2 mt-2 text-gray-500 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600 hover:text-white cursor-pointer ${selectedDataset === 'Flower' ? 'bg-gray-700 text-white' : ''}`} onClick={() => handleDatasetClick('Flower')}>Flower dataset</li>
                <li className={`items-center p-2 mt-2 text-gray-500 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600 hover:text-white cursor-pointer ${selectedDataset === 'House' ? 'bg-gray-700 text-white' : ''}`} onClick={() => handleDatasetClick('House')}>House dataset</li> */}
            </ul>

            <div className="flex flex-col items-start space-y-4 w-[70%] mt-11">
                <div className="flex flex-col space-x-4">
                    <label className="m-2 relative cursor-pointer bg-gray-700 text-white py-2 px-4 rounded-lg font-medium">
                        Upload Dataset
                        <input
                            type="file"
                            className="hidden"
                        />
                    </label>
                    <div className="text-sm text-gray-500">
                        {'No file chosen'}
                    </div>
                </div>
            </div>
        </div>
    );
}
