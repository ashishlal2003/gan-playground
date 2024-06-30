import React from 'react'
import { NavLink } from 'react-router-dom';

export default function ResNavBar() {
  return (
    <div className="sm:hidden flex sm:items-center sm:justify-center flex-grow relative z-50">
      <div className="flex flex-col gap-4 space-x-4 items-start absolute h-auto right-[-10px] top-[-35px] w-[250px] pt-20 p-10 bg-slate-900 rounded-lg">
        <NavLink
          exact
          to="/"
          className="rounded-md text-lg font-medium text-gray-300 px-3 py-2 hover:bg-gray-700 hover:text-white translate-x-4"
          activeClassName="bg-gray-900 text-white"
        >
          Home
        </NavLink>
        <NavLink
          to="/playground"
          className="rounded-md text-lg font-medium text-gray-300 px-3 py-2 hover:bg-gray-700 hover:text-white"
          activeClassName="bg-gray-900 text-white"
        >
          Playground
        </NavLink>
        <NavLink
          to="/docs"
          className="rounded-md text-lg font-medium text-gray-300 px-3 py-2 hover:bg-gray-700 hover:text-white"
          activeClassName="bg-gray-900 text-white"
        >
          Docs
        </NavLink>
        <NavLink
          to="/gallery"
          className="rounded-md text-lg font-medium text-gray-300 px-3 py-2 hover:bg-gray-700 hover:text-white"
          activeClassName="bg-gray-900 text-white"
        >
          Gallery
        </NavLink>
        <NavLink
          to="/community"
          className="rounded-md text-lg font-medium text-gray-300 px-3 py-2 hover:bg-gray-700 hover:text-white"
          activeClassName="bg-gray-900 text-white"
        >
          Community
        </NavLink>
      </div>
    </div>
  )
}
