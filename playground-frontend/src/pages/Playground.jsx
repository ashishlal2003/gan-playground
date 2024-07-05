import React, { useState } from 'react';
import Leftside from '../components/playground/Leftside';
import Center from '../components/playground/Center';

const Playground = () => {
    const [dataset, setDataset] = useState('');

    const handleDatasetSelection = (dataset) => {
        setDataset(dataset);
    }

    return (
        <div className='flex pt-[7.5rem] bg-black text-white h-[43.45rem]'>
            <Leftside onDatasetSelect={handleDatasetSelection} selectedDataset={dataset}/>
            <Center selectedDataset={dataset}/>
        </div>
    );
}

export default Playground;
