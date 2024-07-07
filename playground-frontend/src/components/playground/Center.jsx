import React, { useState, useEffect } from 'react';
import Rightside from './Rightside';
import oops from '../../assets/oops.jpeg';
import Fakeimg from "../../assets/fake_samples_step_000.png"
import axios from 'axios';

export default function Center({ selectedDataset }) {
    return (
        <div className="w-full sm:w-[84%] bg-[#111113] h-full flex flex-col sm:flex-row justify-center items-center sm:items-start">
            <img src={oops} alt="View on desktop" className='block sm:hidden h-[20rem]' />
            <h1 className='block sm:hidden text-white text-center my-16 font-bold text-4xl'>
                ACCESS THROUGH A DESKTOP BROWSER
            </h1>
            <div className='hidden sm:block w-[80%]'>
                <h5>Fake images</h5>
                <div className='h-[400px] w-[400px] bg-white m-4'>
                    <img src={Fakeimg} alt='' />
                </div>
            </div>
            <Rightside className="hidden sm:block self-end" selectedDataset={selectedDataset}/>
        </div>
    )
}
