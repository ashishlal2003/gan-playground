import React from 'react';
import Media1 from '../components/home-components/Media1';
import Content1 from '../components/home-components/Content1';

function Home() {
  return (
    <div className="bg-black text-white w-full h-screen px-4 items-center py-4">
      <div className='flex flex-row ml-[15rem] mt-[5rem] mr-[15rem]'>
        <Media1 />
        <Content1 />
      </div>
    </div>
  );
}

export default Home;
