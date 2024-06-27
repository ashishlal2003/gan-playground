import React from 'react'
import img1 from '../../assets/interactive_learning/img1.png';
import img2 from '../../assets/interactive_learning/img2.png';
import img3 from '../../assets/interactive_learning/img3.png';

export default function InteractiveLearning() {
    const data = [
        {
            title : "User-Freindly Interface",
            desc : "Navigate and test GAN models effortlessly",
            img : img1
        },
        {
            title : "Real-Time Results",
            desc : "See immediate outputs from your GAN models.",
            img : img2
        },
        {
            title : "Comprehensive Tutorials",
            desc : "Step-by-step guides to mastering GANs.",
            img : img3
        },

    ]
    return (
        <div className='md:ml-[5rem] place-content-center mx-[20px] my-[60px] mt-52 flex flex-col items-center gap-6'>
            <h3 className="font-ibm-plex-sans font-bold xl:text-5xl lg:text-5xl md:text-6xl text-5xl">Interactive Learning</h3>
            <p>Hands on GAN experiment</p>
            <div className='flex gap-10 xl:gap-16 flex-wrap items-center justify-center'>
                {data.map((info, index) =>(
                    <div key = {index} className='flex flex-col items-center gap-2'>
                        <img src={info.img} alt = {info.title}/>
                        <h4 className='font-bold'>{info.title}</h4>
                        <p className='font-light'>{info.desc}</p>
                    </div>
                    
                ))}
            </div>
        </div>
    )
}
