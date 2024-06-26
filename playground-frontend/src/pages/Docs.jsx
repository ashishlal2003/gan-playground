import React from 'react';
import Sidebar from '../components/docs/Sidebar';
import { Home, Bookmark} from 'lucide-react';

function Docs() {
  return (
    <div className="bg-black text-white w-full h-screen flex">
      <Sidebar />
    </div>
  );
}

export default Docs;
