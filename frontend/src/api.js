import axios from "axios";

// Create an instance of axios with the base URL
const api = axios.create({
  baseURL: "http://192.168.1.6:8000"
  // baseURL: "http://localhost:8000"
});

// Export the axios instance
export default api;
