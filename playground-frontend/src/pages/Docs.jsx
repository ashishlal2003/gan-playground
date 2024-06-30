import React from 'react';
import Sidebar from '../components/docs/Sidebar';
import { Home, Bookmark } from 'lucide-react';
import Navbar from '../components/Navbar';

function Docs() {
  return (
    <div className="bg-black text-white w-full h-screen flex">
      <Navbar className="shadow-sm shadow-slate-400 bg-black" />
      <div>
        <Sidebar />
      </div>

    </div>
  );
}

export default Docs;
