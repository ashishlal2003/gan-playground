import React, { useState, useEffect, useRef } from 'react';
import Rightside from './Rightside';
import oops from '../../assets/oops.jpeg';
import axios from 'axios';

export default function Center({ selectedDataset }) {
    const [images, setImages] = useState([]);
    const [currentIndex, setCurrentIndex] = useState(0);
    const intervalRef = useRef(null);

    // Fetch images from the server
    const fetchImages = async () => {
        try {
            const response = await axios.get('http://15.206.94.196:5000/generated_images');
            if (response.data.images && response.data.images.length > 0) {
                setImages(response.data.images);
                setCurrentIndex(response.data.images.length - 1); // Set to the latest image
            }
        } catch (error) {
            console.error('Error fetching images:', error);
        }
    };

    // Set up image fetching and cycling
    useEffect(() => {
        fetchImages();

        // Fetch images every 5 seconds
        intervalRef.current = setInterval(fetchImages, 5000);

        return () => clearInterval(intervalRef.current); // Cleanup on unmount
    }, []);

    // Handle image cycling every 5 seconds
    useEffect(() => {
        if (images.length > 0) {
            const cycleInterval = setInterval(() => {
                setCurrentIndex((prevIndex) => (prevIndex + 1) % images.length);
            }, 5000); // Change image every 5 seconds

            return () => clearInterval(cycleInterval); // Cleanup on unmount
        }
    }, [images]);

    // Handle progress bar change
    const handleProgressChange = (event) => {
        setCurrentIndex(parseInt(event.target.value, 10));
    };

    return (
        <div className="w-full sm:w-[84%] bg-[#111113] h-full flex flex-col sm:flex-row justify-center items-center sm:items-start">
            <img src={oops} alt="View on desktop" className="block sm:hidden h-[20rem]" />
            <h1 className="block sm:hidden text-white text-center my-16 font-bold text-4xl">
                ACCESS THROUGH A DESKTOP BROWSER
            </h1>
            <div className="hidden sm:block w-[80%] p-4">
                <h5>Fake images</h5>
                <div className="w-[30%]">
                    <input
                        type="range"
                        min="0"
                        max={images.length - 1}
                        value={currentIndex}
                        onChange={handleProgressChange}
                        className="w-full mt-4"
                    />
                    <p>Step: {currentIndex}</p>
                </div>
                <div className="h-[400px] w-[400px] overflow-auto">
                    {images.length > 0 ? (
                        <img
                            src={`http://15.206.94.196:5000/image/${images[currentIndex]}`}
                            alt={`Fake ${currentIndex}`}
                            className="w-full h-auto my-2"
                        />
                    ) : (
                        <p>No images to display</p>
                    )}
                </div>
            </div>
            <Rightside className="hidden sm:block self-end" selectedDataset={selectedDataset} />
        </div>
    );
}
