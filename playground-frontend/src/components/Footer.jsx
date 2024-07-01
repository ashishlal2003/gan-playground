// src/components/Footer.jsx

import React from 'react';

function Footer() {
  return (
    <footer className="bg-gray-800 text-white text-center py-4 z-50 relative w-[102%] translate-x-[-14px]">
      <div className="container w-full">
        <p>&copy; {new Date().getFullYear()} GAN Playground. All rights reserved.</p>
      </div>
    </footer>
  );
}

export default Footer;
