// src/components/Footer.jsx

import React from 'react';

function Footer() {
  return (
    <footer className="bg-gray-800 text-white text-center py-4 z-50 relative">
      <div className="container mx-auto">
        <p>&copy; {new Date().getFullYear()} GAN Playground. All rights reserved.</p>
      </div>
    </footer>
  );
}

export default Footer;
