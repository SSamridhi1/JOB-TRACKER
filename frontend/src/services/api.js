import axios from 'axios'

// Why this file exists:
// A single configured Axios instance (base URL, headers) means every
// service file (authService, applicationService, etc.) shares the same
// config instead of repeating it, and gives one place to later add
// request/response interceptors (e.g. attaching the auth token).

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api',
  headers: {
    'Content-Type': 'application/json',
  },
})

export default apiClient
