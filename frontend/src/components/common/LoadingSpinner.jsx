// Why this file exists:
// A single reusable loading indicator so every page/component that
// fetches data shows a consistent spinner instead of each one inventing
// its own "Loading..." text.
function LoadingSpinner() {
  return <p>Loading...</p>
}

export default LoadingSpinner
