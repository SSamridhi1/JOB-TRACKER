import AppRoutes from './routes/AppRoutes.jsx'

// Why this file exists:
// App.jsx is intentionally thin. It doesn't define pages, routes, or
// layout itself - it just renders <AppRoutes />. This keeps App.jsx stable
// even as the route list grows, and makes it easy to wrap AppRoutes with
// future providers (e.g. <AuthProvider>) in one obvious place.
function App() {
  return <AppRoutes />
}

export default App
