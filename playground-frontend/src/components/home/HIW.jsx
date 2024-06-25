import React from 'react'
import { NavLink } from 'react-router-dom'

function HIW() {
  return (
    <div className="md:ml-[5rem] place-content-center mx-[20px]">
      <h1 className="font-ibm-plex-sans font-bold xl:text-7xl lg:text-5xl md:text-6xl text-5xl">How it Works</h1>
      <p className="flex justify-center py-4 font-ibm-plex-sansmt-4 xl:text-lg lg:text-md text-gray-500">A quick guide to understand the inner workings.</p>

      <div className='mt-[1rem] flex justify-center'>
        <NavLink to="/docs" className="rounded-[10px] px-3 py-3 text-lg lg:text-md font-medium text-gray-300 hover:bg-gray-700 hover:text-white bg-purple-600">
          Read the docs
        </NavLink>
      </div>

    </div>
  )
}

export default HIW
