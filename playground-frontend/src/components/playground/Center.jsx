import React,{useState, useEffect} from 'react';
import Rightside from './Rightside';
import oops from '../../assets/oops.jpeg';
import axios from 'axios';

export default function Center() {
  const[data, setData] = useState('');

  useEffect(()=>{
    const fetchData = async() =>{
      try{
        const res = await axios.get('http://localhost:5000/');
        setData(res.data);
      }
      catch(err){
        console.log(err);
      }
    };

    fetchData();

  },[]);

  return (
    <div className="w-full sm:w-[84%] bg-[#111113] h-screen flex flex-col sm:flex-row justify-center items-center sm:items-start">
      <img src={oops} alt="View on desktop" className='block sm:hidden h-[20rem]' />
      <h1 className='block sm:hidden text-white text-center my-16 font-bold text-4xl'>
        ACCESS THROUGH A DESKTOP BROWSER
      </h1>
      <div className='hidden sm:block w-[80%]'></div>
      <p className='text-white'>{data}</p>
      <Rightside className="hidden sm:block self-end"/>
    </div>
  )
}
