// Why this file exists:
// Date formatting (e.g. for application_date, status changed_at) will be
// needed on multiple pages. One shared function keeps the display format
// consistent across the whole app instead of each component rolling its own.

export function formatDate(isoDateString) {
  if (!isoDateString) return ''
  const date = new Date(isoDateString)
  return date.toLocaleDateString(undefined, {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  })
}
