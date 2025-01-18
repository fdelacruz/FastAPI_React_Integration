import React, { useState } from 'react';
import { FormControl, Input, Button, Box } from '@chakra-ui/react';

const AddFruitForm = ({ addFruit }) => {
  const [fruitName, setFruitName] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    if (fruitName) {
      addFruit(fruitName);
      setFruitName('');
    }
  };

  return (
    <Box as="form" onSubmit={handleSubmit} display="flex" gap="4" alignItems="center">
      <FormControl>
        <Input
          type="text"
          value={fruitName}
          onChange={(e) => setFruitName(e.target.value)}
          placeholder="Enter fruit name"
          size="md"
          bg="white"
          borderColor="gray.300"
          _hover={{ borderColor: "gray.400" }}
          _focus={{ borderColor: "blue.500", boxShadow: "0 0 0 1px blue.500" }}
        />
      </FormControl>
      <Button type="submit" colorScheme="gray" size="md">
        Add Fruit
      </Button>
    </Box>
  );
};

export default AddFruitForm;

