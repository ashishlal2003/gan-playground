import React from 'react'

function Sidebar() {
  return (
    <aside className='text-white h-screen'>
      <nav className='h-full flex flex-col bg-red border-r shadow-sm'>
        <div className="p-4 pb-2 flex justify-between items-center">
          <img src="https://img.logoipsum.com/243.svg" alt="" />
          <button>
            
          </button>
        </div>

        <ul className='flex-1 px-3'>
        YO
        </ul>
        <ul className='flex-1 px-3'>
        YO2
        </ul>
        <ul className='flex-1 px-3'>
        YO3
        </ul>


      </nav>
    </aside>
  )
}

export default Sidebar
