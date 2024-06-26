// Sidebar.jsx
import { useContext, createContext, useState } from 'react';
import { MoreVertical, ChevronLast, ChevronFirst } from 'lucide-react';

export const SidebarContext = createContext();

export default function Sidebar({ children }) {
  const [expanded, setExpanded] = useState(true);
  const [subMenuOpen, setSubMenuOpen] = useState(false);

  const toggleSubMenu = () => {
    setSubMenuOpen(!subMenuOpen);
  };

  return (
    <SidebarContext.Provider value={{ expanded }}>
      <aside className="h-screen">
        <nav className="h-full flex flex-col bg-gray-700 border-r shadow-sm">
          <div className="p-4 pb-2 flex justify-between items-center">
            <button
              onClick={() => setExpanded((curr) => !curr)}
              className="p-1.5 rounded-lg bg-gray-700 hover:bg-gray-800"
            >
              {expanded ? <ChevronFirst /> : <ChevronLast />}
            </button>
          </div>

          <ul className="flex-1 px-3">{children}</ul>

          <div className="p-2.5 mt-2 flex items-center rounded-md px-4 duration-300 cursor-pointer hover:bg-blue-600" onClick={toggleSubMenu}>
            <i className="bi bi-chat-left-text-fill"></i>
            <div className="flex justify-between w-full items-center">
              <span className="text-[15px] ml-4 text-gray-200">Chatbox</span>
              <span className={`text-sm ${subMenuOpen ? 'rotate-180' : ''}`} id="arrow">
                <i className="bi bi-chevron-down"></i>
              </span>
            </div>
          </div>

          {subMenuOpen && (
            <div className="leading-7 text-left text-sm font-thin mt-2 w-4/5 mx-auto" id="submenu">
              <h1 className="cursor-pointer p-2 hover:bg-gray-700 rounded-md mt-1">Social</h1>
              <h1 className="cursor-pointer p-2 hover:bg-gray-700 rounded-md mt-1">Personal</h1>
              <h1 className="cursor-pointer p-2 hover:bg-gray-700 rounded-md mt-1">Friends</h1>
            </div>
          )}

          <div className="border-t flex p-3">
            <img
              src="https://ui-avatars.com/api/?background=c7d2fe&color=3730a3&bold=true"
              alt=""
              className="w-10 h-10 rounded-md"
            />
            <div
              className={`
                flex justify-between items-center
                overflow-hidden transition-all ${expanded ? 'w-52 ml-3' : 'w-0'}
            `}
            >
              <div className="leading-4">
                <h4 className="font-semibold">John Doe</h4>
                <span className="text-xs text-gray-600">johndoe@gmail.com</span>
              </div>
              <MoreVertical size={20} />
            </div>
          </div>
        </nav>
      </aside>
    </SidebarContext.Provider>
  );
}
