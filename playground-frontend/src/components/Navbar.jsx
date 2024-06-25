import React from 'react';
import { NavLink } from 'react-router-dom';

function Navbar() {
  return (
    <nav className="bg-black">
      
      <div className="bg-red-500 flex justify-center items-center py-3 max-w-7xl mx-auto px-4">
      <div className="flex-shrink-0">
            <img className="h-8 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500" alt="Your Company" />
          </div>
        <div className=" h-16">
          <div className="hidden sm:flex sm:items-center sm:justify-center">
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
          
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
