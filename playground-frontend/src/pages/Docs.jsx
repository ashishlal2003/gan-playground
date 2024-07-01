import React from 'react';
import Sidebar from '../components/docs/Sidebar';
import { Home, Bookmark } from 'lucide-react';
import Overview from '../components/docs/Overview';

function Docs() {
  return (
    <div className="bg-black text-white w-full h-screen flex pt-36">

      <div className='flex-2 w-[20%]'>
        <Sidebar />
      </div>
      <div className='flex-1 w-[69%]'>
        <Overview />
      </div>
    </div>
  );
}

export default Docs;
