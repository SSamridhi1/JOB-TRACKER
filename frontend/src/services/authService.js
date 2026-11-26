import apiClient from './api.js'

// Why this file exists:
// Route/page components should not call axios directly - they should call
// a "service" function. This keeps API call shapes in one place per
// resource, and means the API layer can change without touching any page.
// Skeleton only: functions are declared with the correct signature but not
// yet called from any page.

export function register(payload) {
  return apiClient.post('/auth/register', payload)
}

export function login(payload) {
  return apiClient.post('/auth/login', payload)
}

export function getCurrentUser() {
  return apiClient.get('/auth/me')
}
