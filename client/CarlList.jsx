import React, {use, useEffect, useState} from "react";
import axios from "axios";

const CarList = () => {
    const [cars, setCars] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        axios.get("http://localhost:8000/api/cars")
        .then(res => setCars(res.data))
        .catch(err => console.log(err))
        .finally(() => setLoading(false))
    })

    if (loading) return <p>Loading...</p>;
    
    return (
        <div>
            {cars.map(car => (
                <div key={car.id}>
                    <h2>{car.model}</h2>
                    <p>{car.year}</p>
                </div>
            ))}
        </div>
    )
}
export default CarList