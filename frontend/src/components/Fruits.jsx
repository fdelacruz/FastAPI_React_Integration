import React, { useEffect, useState } from 'react';
import AddFruitForm from './AddFruitForm';
import api from '../api';

const FruitList = () => {
  const [fruits, setFruits] = useState([]);

  // api.interceptors.request.use((config) => {
  //   console.log('Making request to:', config.url);
  //   return config;
  // });

  const fetchFruits = async () => {
    try {
      const response = await api.get('/fruits');
      setFruits(response.data || []);
    } catch (error) {
      console.error("Error fetching fruits", error);
    }
  };

  const addFruit = async (fruitName) => {
    try {
      await api.post('/fruits', { name: fruitName });
      fetchFruits();  // Refresh the list after adding a fruit
    } catch (error) {
      console.error("Error adding fruit", error);
    }
  };

  useEffect(() => {
    fetchFruits(); // Fetch fruits from the backend
  }, []);

  return (
    <div>
      <h2>Fruits List</h2>
      <p>Fruits count: {fruits.length}</p>
      <ul>
        {fruits && fruits.length > 0 ? (
          fruits.map((fruit, index) => (
            <li key={fruit.id || index}>{fruit.name}</li>
          ))
        ) : (
          <p>No fruits available</p>
        )}
      </ul>
      <AddFruitForm addFruit={addFruit} />
    </div>
  );
};

export default FruitList;
