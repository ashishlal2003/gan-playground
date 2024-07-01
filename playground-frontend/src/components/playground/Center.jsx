import React from 'react'
import Rightside from './Rightside'
export default function Center() {
  return (
    <div className="w-[84%] bg-[#111113] h-full flex ">
      <div className='w-[80%]'></div>
      <Rightside className="self-end"/>
    </div>
  )
}
