import { useState, useEffect } from "react";
import axiosInstance from "../api/axios";

function Home() {
    const [data, setData] = useState([]);

    useEffect(() => {
        axiosInstance.get('/')    // Path to data from the base url root of api
            .then((response) => {
                setData(response.data);
            })
            .catch((error) => {
                console.error('Error fetching data:', error);
            });
    }, []);

    return (
        <div id="Home" className="mx-[12px]">
            <div>
                <h1 className="text-3xl">Hello World!, This is Vite with React</h1>
                <h2 className="text-2xl mt-2 text-[#008000]">Here We are utilizing our Django API</h2>
            </div>
            <div className="ConnectingAPI">
                <h3 className="mx-[8px] mt-[12px] font-[700]">To Do API data</h3>
                <div className="mx-[8px] mt-[10px] grid grid-cols-4 gap-y-[12px] gap-x-[10px]">
                    {data.map(item => (
                        <div className="p-4 bg-amber-500 rounded-md border-amber-100 border-solid border-2" key={item.id}>
                            <h4 className="font-[700] text-[18px]"> {item.title}</h4>
                            <p>{item.body}</p>
                            <p className="mt-[20px]">{item.formatted_datetime}</p>
                        </div>   
                    ))}
               </div>
            </div>
        </div>
       
   )
}

export default Home