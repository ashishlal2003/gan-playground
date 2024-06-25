import React from 'react'
import { NavLink } from 'react-router-dom'

function Content1() {
  return (
    <div className="md:ml-[5rem] place-content-center mx-[20px]">
      <h1 className="font-ibm-plex-sans font-bold xl:text-7xl lg:text-5xl md:text-6xl text-5xl">Explore the</h1>
      <h1 className="font-ibm-plex-sans xl:text-7xl lg:text-5xl md:text-6xl text-5xl font-bold">Power of GANs</h1>
      <p className="py-4 font-ibm-plex-sansmt-4 xl:text-lg lg:text-md text-gray-500">Experiment with cutting-edge GAN models in a user-friendly playground.</p>

      <div className='mt-[3rem]'>
        <NavLink to="/playground" className="rounded-[10px] px-4 py-4 text-lg lg:text-md font-medium text-gray-300 hover:bg-gray-700 hover:text-white bg-purple-600">
          Try it now
        </NavLink>
      </div>

    </div>
  )
}

export default Content1
