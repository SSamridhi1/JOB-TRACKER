import { Link } from 'react-router-dom'

// Skeleton navbar - static links only, no active-state highlighting or
// auth-aware rendering (e.g. hiding "Login" once logged in) yet.
function Navbar() {
  return (
    <nav>
      <Link to="/">Dashboard</Link>
      <Link to="/applications">Applications</Link>
      <Link to="/login">Login</Link>
    </nav>
  )
}

export default Navbar
