import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Home from './pages/Home';
import Playground from './pages/Playground';
import Gallery from './pages/Gallery';
import Community from './pages/Community';
import Docs from './pages/Docs';

const App = () => {
    return (
        <Router>
            <Navbar />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/playground" element={<Playground />} />
                <Route path="/gallery" element={<Gallery />} />
                <Route path="/community" element={<Community />} />
                <Route path="/docs" element={<Docs />} />
            </Routes>
        </Router>
    );
}

export default App;
