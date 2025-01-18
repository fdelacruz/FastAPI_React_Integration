import { useState, useEffect } from 'react';
import { Box, Button, Heading, List, ListItem, Spacer, Text, Stack } from '@chakra-ui/react';
import AddFruitForm from './AddFruitForm';
import api from '../api';

const FruitList = () => {
  const [fruits, setFruits] = useState([]);

  const fetchFruits = async () => {
    try {
      const response = await api.get('/fruits');
      setFruits(response.data || []);
    } catch (error) {
      console.error('Error fetching fruits', error);
    }
  };

  const addFruit = async (fruitName) => {
    try {
      await api.post('/fruits', { name: fruitName });
      fetchFruits(); // Refresh the list after adding a fruit
    } catch (error) {
      console.error('Error adding fruit', error);
    }
  };

  const deleteFruit = async (id) => {
    try {
      await api.delete(`/fruits/${id}`);
      fetchFruits(); // Refresh the list after deleting a fruit
    } catch (error) {
      console.error('Error deleting fruit:', error);
    }
  };

  const editFruit = (id) => {
    // Placeholder for future edit functionality
    console.log(`Edit fruit with ID: ${id}`);
  };

  useEffect(() => {
    fetchFruits(); // Fetch fruits from the backend
  }, []);

  return (
    <Box p="4" maxWidth="600px" mx="auto" mt="6">
      <Heading as="h2" size="lg" mb="4" textAlign="center">
        Fruits List
      </Heading>
      <List spacing={3}>
        {fruits.map((fruit, index) => (
          <ListItem
            key={index}
            display="flex"
            alignItems="center"
            justifyContent="space-between"
            borderWidth="1px"
            borderRadius="md"
            p="2"
          >
            <Text>{fruit.name}</Text>
            <Stack direction="row" spacing={2}>
              {/* Edit Button */}
              <Button
                size="sm"
                colorScheme="green"
                onClick={() => editFruit(fruit.id)}
              >
                Edit
              </Button>

              {/* Delete Button */}
              <Button
                size="sm"
                colorScheme="red"
                onClick={() => deleteFruit(fruit.id)}
              >
                Delete
              </Button>
            </Stack>
          </ListItem>
        ))}
      </List>
      <Spacer mt="4" />
      <Box mt="6">
        <AddFruitForm addFruit={addFruit} />
      </Box>
    </Box>
  );
};

export default FruitList;

