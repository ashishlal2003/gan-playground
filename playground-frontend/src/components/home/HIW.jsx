import React from 'react'
import { NavLink } from 'react-router-dom'
import HIWimg from "../../assets/HIW.png";
import Vector1 from "../../assets/HIW/Vector1.png"
import Vector2 from "../../assets/HIW/Vector2.png"
import Vector3 from "../../assets/HIW/Vector3.png"

function HIW() {
  const data = [
    {
      name: "Upload Your Data",
      desc: "Easily upload your datasets for model training.",
      icon: Vector1
    },
    {
      name: "Train GAN Models",
      desc: "Utilize our robust training environment.",
      icon: Vector2
    },
    {
      name: "Analyze Outputs",
      desc: "Examine generated results for insights.",
      icon: Vector3
    },

  ]
  return (
    <div className="md:ml-[5rem] my-52 place-content-center mx-[20px] flex flex-col items-center gap-20">
      <div className='flex items-center justify-center gap-[8rem]'>
        <img src={HIWimg} />
        <div className='flex flex-col items-start'>
          <h1 className="font-ibm-plex-sans font-bold xl:text-6xl lg:text-5xl md:text-6xl text-5xl">How it Works</h1>
          <p className="flex justify-center py-4 font-ibm-plex-sansmt-4 xl:text-lg lg:text-md text-gray-500">A quick guide to understand the inner workings.</p>

          <div className='mt-[1rem] flex justify-center'>
            <NavLink to="/docs" className="rounded-[10px] px-3 py-3 text-lg lg:text-md font-medium text-gray-300 hover:bg-gray-700 hover:text-white bg-purple-600">
              Read the docs
            </NavLink>
          </div>
        </div>
      </div>

      <div className='flex gap-28'>
        {data.map((info, index) => (
          <div className=''>
            <img src={info.icon} alt='icon' />
            <h4 className='font-semibold my-2'>{info.name}</h4>
            <p className='font-light'>{info.desc}</p>
          </div>
        ))}
      </div>

    </div>
  )
}

export default HIW
