import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';
import Logo from '../assets/logo.png';
import ResNavBar from './ResNavBar';
import { IoMenu } from "react-icons/io5";
import { RxCross2 } from "react-icons/rx";

function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <>
      <nav className={`fixed w-full z-20 transition-shadow duration-300 border-b-[0.5px] border-white bg-black`}>
        <div className="flex justify-between items-center py-3 max-w-7xl mx-auto px-4">
          <div className="flex-shrink-0">
            <NavLink to="/">
              <img className="sm:h-[6rem] h-[4rem] w-auto" src={Logo} alt="Your Company" />
            </NavLink>
          </div>

          <div className="hidden sm:flex sm:items-center sm:justify-center flex-grow">
            <div className="flex space-x-4">
              <NavLink
                exact
                to="/"
                className="rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white"
                activeClassName="bg-gray-900 text-white"
              >
                Home
              </NavLink>
              <NavLink
                to="/playground"
                className="rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white"
                activeClassName="bg-gray-900 text-white"
              >
                Playground
              </NavLink>
              <NavLink
                to="/docs"
                className="rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white"
                activeClassName="bg-gray-900 text-white"
              >
                Docs
              </NavLink>
              <NavLink
                to="/gallery"
                className="rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white"
                activeClassName="bg-gray-900 text-white"
              >
                Gallery
              </NavLink>
              <NavLink
                to="/community"
                className="rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white"
                activeClassName="bg-gray-900 text-white"
              >
                Community
              </NavLink>
            </div>
          </div>

          <div>
            <NavLink to="/playground" className="hidden sm:block rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white border border-white">
              Get Started
            </NavLink>
          </div>
          <IoMenu className='text-white text-4xl absolute right-4 block sm:hidden' onClick={() => setIsOpen(!isOpen)} />

          {isOpen && (
            <div className='relative'>
              <RxCross2 className='text-white text-4xl absolute z-[100] right-0 top-[-10px] block sm:hidden' onClick={() => setIsOpen(!isOpen)} />
              <ResNavBar />
            </div>
          )}
        </div>
      </nav>

      {isOpen && (
        <div
          className="fixed inset-0 bg-black bg-opacity-50 backdrop-blur-md z-10"
          onClick={() => setIsOpen(false)}
        />
      )}
    </>
  );
}

export default Navbar;
