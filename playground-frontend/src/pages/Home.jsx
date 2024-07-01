import React from 'react';
import Media1 from '../components/home/Media1';
import Content1 from '../components/home/Content1';
import HIW from '../components/home/HIW';
import InteractiveLearning from '../components/home/InteractiveLearning';
import Footer from '../components/Footer';

function Home() {
  return (
    <div className="bg-black text-white w-full px-4 items-center pt-4 h-auto ">
      <div className='flex flex-col lg:flex-row xl:mx-[10rem] my-[5rem] lg:mx-[7rem] md:mx-[5rem] translate-y-[8rem]'>
        <Media1 />
        <Content1 />
      </div>

      <div className=''>
        <InteractiveLearning />
        <HIW />
      </div>
      <Footer className="w-[115%]"/>
    </div>
  );
}

export default Home;
