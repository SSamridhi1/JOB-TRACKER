import apiClient from './api.js'

// Skeleton only - not yet called from any page.

export function listApplications(params) {
  return apiClient.get('/applications', { params })
}

export function getApplication(id) {
  return apiClient.get(`/applications/${id}`)
}

export function createApplication(payload) {
  return apiClient.post('/applications', payload)
}

export function updateApplication(id, payload) {
  return apiClient.put(`/applications/${id}`, payload)
}

export function deleteApplication(id) {
  return apiClient.delete(`/applications/${id}`)
}
