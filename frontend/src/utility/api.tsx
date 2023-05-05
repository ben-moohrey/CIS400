import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:4444/api', // Replace with the backend API URL
});

export default api;
