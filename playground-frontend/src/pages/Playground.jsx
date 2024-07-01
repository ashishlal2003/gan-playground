import React, { useState } from 'react';
import Leftside from '../components/playground/Leftside';
import Center from '../components/playground/Center';

const Playground = () => {
    return (
        <div className='flex pt-[7.5rem] bg-black text-white h-[43.45rem]'>
            <Leftside />
            <Center />
        </div>
    );
}

export default Playground;
