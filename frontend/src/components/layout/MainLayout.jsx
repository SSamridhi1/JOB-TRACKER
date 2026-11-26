import { Outlet } from 'react-router-dom'
import Navbar from './Navbar.jsx'

// Why this file exists:
// Shared page chrome (navbar today, maybe a sidebar or footer later) lives
// in one layout component. <Outlet /> is React Router's placeholder for
// "whichever page matched the current route" - this is the standard
// nested-routing pattern instead of repeating <Navbar /> in every page.
function MainLayout() {
  return (
    <div className="app-shell">
      <Navbar />
      <main className="app-content">
        <Outlet />
      </main>
    </div>
  )
}

export default MainLayout
