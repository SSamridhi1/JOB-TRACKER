// Why this file exists:
// A single reusable error display component, matching LoadingSpinner's
// pattern, for consistent error UI across the app.
function ErrorMessage({ message }) {
  return <p role="alert">{message || 'Something went wrong.'}</p>
}

export default ErrorMessage
