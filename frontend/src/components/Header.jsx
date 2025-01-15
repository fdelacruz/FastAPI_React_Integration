import { Heading, Flex } from '@chakra-ui/react';

const Header = () => {
  return (
    <Flex
      as="nav"
      align="center"
      justify="space-between"
      wrap="wrap"
      padding="0.5rem"
      bg="gray.400"
      width="100%" // Ensures the navbar spans the full width
      position="fixed" // Keeps the navbar at the top of the viewport
      top="0" // Positions it at the very top
      left="0" // Align it to the left
      zIndex="1000" // Ensure it stays above other elements
      boxSizing="border-box" // Include padding and border in width calculations
    >
      <Flex align="center" mr={5}>
        <Heading as="h1" size="sm">Fruit Management</Heading>
      </Flex>
    </Flex>
  );
};

export default Header;

