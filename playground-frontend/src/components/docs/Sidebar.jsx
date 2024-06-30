import React, { useState } from 'react';

function Sidebar() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const [isSimpleGANDropdownOpen, setIsSimpleGANDropdownOpen] = useState(false);
  const [isDCGANDropdownOpen, setIsDCGANDropdownOpen] = useState(false);
  const [isWGANDropdownOpen, setIsWGANDropdownOpen] = useState(false);

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  const toggleSimpleGANDropdown = () => {
    setIsSimpleGANDropdownOpen(!isSimpleGANDropdownOpen);
  };

  const toggleDCGANDropdown = () => {
    setIsDCGANDropdownOpen(!isDCGANDropdownOpen);
  };

  const toggleWGANDropdown = () => {
    setIsWGANDropdownOpen(!isWGANDropdownOpen);
  };

  return (
    <div className=''>
      <div className='translate-y-24 w-[94%] fixed ml-3 border-b-[0.1px] border-white'>
        <button
          aria-controls="sidebar-multi-level-sidebar"
          type="button"
          className="inline-flex items-center p-2 mt-2 ms-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
          onClick={toggleSidebar}
        >
          <span className="sr-only">Open sidebar</span>
          <svg
            className="w-6 h-6"
            aria-hidden="true"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              clipRule="evenodd"
              fillRule="evenodd"
              d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z"
            />
          </svg>
        </button>
      </div>
      <aside
        id="sidebar-multi-level-sidebar"
        className={`fixed top-0 left-0 z-40 w-64 h-screen transition-transform ${isSidebarOpen ? 'translate-x-0' : '-translate-x-full'} sm:translate-x-0`}
        aria-label="Sidebar"
      >
        <div className="h-[80%] px-3 py-4 overflow-y-scroll border-r bg-black mt-[7.6rem] z-0">
          <ul className="space-y-2 font-medium">
            <p className='ml-2 font-bold'>DOCUMENTATION</p>
            <li>
              <button
                type="button"
                className="flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700"
              >
                <span className="flex-1 text-left rtl:text-right whitespace-nowrap">Overview</span>
              </button>
            </li>
            <li>
              <button
                type="button"
                className="flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700"
                aria-controls="dropdown-example"
                onClick={toggleSimpleGANDropdown}
              >
                <span className="flex-1 text-left rtl:text-right whitespace-nowrap">Simple GAN</span>
                <svg
                  className="w-3 h-3"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 10 6"
                >
                  <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="m1 1 4 4 4-4" />
                </svg>
              </button>
              <ul id="dropdown-example" className={`py-2 space-y-2 ${isSimpleGANDropdownOpen ? '' : 'hidden'}`}>
                <li>
                  <a
                    href="/docs/simple-gan/theory"
                    className="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700"
                  >
                    Theory
                  </a>
                </li>
                <li>
                  <a
                    href="/docs/simple-gan/usage"
                    className="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700"
                  >
                    Usage
                  </a>
                </li>
                <li>
                  <a
                    href="/docs/simple-gan/code"
                    className="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700"
                  >
                    Code Snippet
                  </a>
                </li>
              </ul>
            </li>


            <li>
              <button
                type="button"
                className="flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700"
                aria-controls="dropdown-example"
                onClick={toggleDCGANDropdown}
              >
                <span className="flex-1 text-left rtl:text-right whitespace-nowrap">DC-GAN</span>
                <svg
                  className="w-3 h-3"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 10 6"
                >
                  <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="m1 1 4 4 4-4" />
                </svg>
              </button>
              <ul id="dropdown-example" className={`py-2 space-y-2 ${isDCGANDropdownOpen ? '' : 'hidden'}`}>
                <li>
                  <a
                    href="/docs/dcgan/theory"
                    className="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700"
                  >
                    Theory
                  </a>
                </li>
                <li>
                  <a
                    href="/docs/dcgan/usage"
                    className="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700"
                  >
                    Usage
                  </a>
                </li>
                <li>
                  <a
                    href="/docs/dcgan/code"
                    className="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700"
                  >
                    Code Snippet
                  </a>
                </li>
              </ul>
            </li>


            <li>
              <button
                type="button"
                className="flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700"
                aria-controls="dropdown-example"
                onClick={toggleWGANDropdown}
              >
                <span className="flex-1 text-left rtl:text-right whitespace-nowrap">W-GAN</span>
                <svg
                  className="w-3 h-3"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 10 6"
                >
                  <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="m1 1 4 4 4-4" />
                </svg>
              </button>
              <ul id="dropdown-example" className={`py-2 space-y-2 ${isWGANDropdownOpen ? '' : 'hidden'}`}>
                <li>
                  <a
                    href="/docs/wgan/theory"
                    className="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700"
                  >
                    Theory
                  </a>
                </li>
                <li>
                  <a
                    href="/docs/wgan/usage"
                    className="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700"
                  >
                    Usage
                  </a>
                </li>
                <li>
                  <a
                    href="/docs/wgan/code"
                    className="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700"
                  >
                    Code Snippet
                  </a>
                </li>
              </ul>
            </li>
          </ul>
        </div>
      </aside>

      {/* Overlay to close the sidebar when clicking outside on small screens */}
      {isSidebarOpen && (
        <div
          className="fixed inset-0 z-30 bg-black opacity-50 sm:hidden"
          onClick={toggleSidebar}
        ></div>
      )}
    </div>
  );
}

export default Sidebar;
