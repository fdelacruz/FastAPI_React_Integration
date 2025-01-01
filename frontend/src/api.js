import axios from "axios";

// Create an instance of axios with the base URL
const api = axios.create({
  baseURL: "http://192.168.1.6:8001"
});

// Export the axios instance
export default api;
