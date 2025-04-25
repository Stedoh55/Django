import { useState, useEffect } from "react"
import axiosInstance from "../api/axios"

function Home() {
    const [data, setData] = useState([]);

    useEffect(() => {
        axiosInstance.get('/')
            .then((response) => {
                setData(response.data);
            })
            .catch((error) => {
                console.error('Error Fetching data:', error);
            });
    }, [])

    return (
        <div>
            <div>
                <h1 className="font-bold">Hello World !</h1>
                <div>
                    {data.map(item => (
                        <div key={item.id}>
                            <h3>{item.title} by {item.author}</h3>
                            <p>{item.body}</p>
                            <p>Created date: {item.created_at }</p>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}

export default Home