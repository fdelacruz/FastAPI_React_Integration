import axios from "axios";

// Create an instance of axios with the base URL
const api = axios.create({
  baseURL: "/api"
});

// Export the axios instance
export default api;
