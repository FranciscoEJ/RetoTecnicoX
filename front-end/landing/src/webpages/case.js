import React, { useState, useEffect } from 'react';
const Case = props => {
    var number_case = props.match.params.number_case
    const [error, setError] = useState(null);
    const [isLoaded, setIsLoaded] = useState(false);
    const [user, setUser] = useState([]);

    useEffect(() => {
        fetch("http://localhost:5000/" + number_case)
            .then(res => res.json())
            .then(
                (data) => {
                    console.log(data);
                    setUser(data);
                    setIsLoaded(true);
                },
                (error) => {
                    setIsLoaded(true);
                    setError(error);
                }
            )
    }, [])
    if (error) {
        return <div>Error: {error.message}</div>;
    }
    if (!isLoaded) {
        return <div>Loading...</div>;
    }

    if (user) {
        return (
            <div>
                <h1>{user}</h1>
            </div>
        );
    }
}
export default Case;