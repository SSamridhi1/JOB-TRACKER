// Why this file exists:
// The 7 application statuses are used in multiple places (status badges,
// filter dropdowns, forms). Defining them once here - matching the
// backend's exact string values - prevents typos and drift between the
// frontend and the API contract.

export const APPLICATION_STATUSES = [
  'WISHLIST',
  'APPLIED',
  'SCREENING',
  'INTERVIEW',
  'OFFER',
  'REJECTED',
  'WITHDRAWN',
]
