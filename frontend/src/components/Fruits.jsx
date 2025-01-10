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
    <div className='fruit-list-container'>
      <h2 className='fruit-header'>Fruits List</h2>
      <ul className='fruit-list'>
        {
          fruits.map((fruit, index) => (
            <li key={index}>{fruit.name}</li>
          ))
        }
      </ul>
      <div className='add-fruit-form'><AddFruitForm addFruit={addFruit} /></div>
    </div>
  );
};

export default FruitList;
