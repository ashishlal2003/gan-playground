import React from 'react';
import Sidebar from '../components/docs/Sidebar';
import SidebarItem from '../components/docs/SidebarItem';
import { Home, Bookmark} from 'lucide-react';

function Docs() {
  return (
    <div className="bg-black text-white w-full h-screen flex">
      <Sidebar>
        <SidebarItem icon={<Home />} text="Home" />
        <SidebarItem icon={<Bookmark />} text="Bookmark" />
      </Sidebar>
    </div>
  );
}

export default Docs;
