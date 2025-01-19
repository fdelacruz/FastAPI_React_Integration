import React, { useState } from "react";
import {
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalBody,
  ModalFooter,
  FormControl,
  Input,
  Button,
} from "@chakra-ui/react";

const UpdateFruitForm = ({ isOpen, onClose, fruit, onUpdate }) => {
  const [fruitName, setFruitName] = useState(fruit?.name || "");

  const handleSubmit = () => {
    onUpdate(fruit.id, fruitName); // Call the update handler from FruitList
  };

  return (
    <Modal isOpen={isOpen} onClose={onClose}>
      <ModalOverlay />
      <ModalContent>
        <ModalHeader>Edit Fruit</ModalHeader>
        <ModalBody>
          <FormControl>
            <Input
              type="text"
              value={fruitName}
              onChange={(e) => setFruitName(e.target.value)}
              placeholder="Enter new fruit name"
              size="md"
              bg="white"
              borderColor="gray.300"
              _hover={{ borderColor: "gray.400" }}
              _focus={{ borderColor: "blue.500", boxShadow: "0 0 0 1px blue.500" }}
            />
          </FormControl>
        </ModalBody>
        <ModalFooter>
          <Button colorScheme="blue" onClick={handleSubmit} mr={3}>
            Save
          </Button>
          <Button variant="ghost" onClick={onClose}>
            Cancel
          </Button>
        </ModalFooter>
      </ModalContent>
    </Modal>
  );
};

export default UpdateFruitForm;
