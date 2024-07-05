import React from 'react';
import Rightside from './Rightside';
import oops from '../../assets/oops.jpeg';

export default function Center() {
  return (
    <div className="w-full sm:w-[84%] bg-[#111113] h-screen flex flex-col sm:flex-row justify-center items-center sm:items-start">
      <img src={oops} alt="View on desktop" className='block sm:hidden h-[20rem]' />
      <h1 className='block sm:hidden text-white text-center my-16 font-bold text-4xl'>
        ACCESS THROUGH A DESKTOP BROWSER
      </h1>
      <div className='hidden sm:block w-[80%]'></div>
      <Rightside className="hidden sm:block self-end"/>
    </div>
  )
}
