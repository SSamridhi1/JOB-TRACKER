import { Route, Routes } from 'react-router-dom'
import MainLayout from '../components/layout/MainLayout.jsx'
import LoginPage from '../pages/auth/LoginPage.jsx'
import RegisterPage from '../pages/auth/RegisterPage.jsx'
import DashboardPage from '../pages/dashboard/DashboardPage.jsx'
import ApplicationListPage from '../pages/applications/ApplicationListPage.jsx'
import ApplicationDetailPage from '../pages/applications/ApplicationDetailPage.jsx'
import NotFoundPage from '../pages/NotFoundPage.jsx'

// Why this file exists:
// Centralising the URL -> page mapping in one file makes the whole app's
// navigation structure visible at a glance, instead of routes being
// scattered or implicitly defined. MainLayout wraps every page so the
// navbar/sidebar don't need to be repeated in each page component.
//
// NOTE: There is no route-protection (redirect-if-not-logged-in) logic
// yet - that depends on the auth feature, which isn't implemented.
function AppRoutes() {
  return (
    <Routes>
      <Route element={<MainLayout />}>
        <Route path="/" element={<DashboardPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/applications" element={<ApplicationListPage />} />
        <Route path="/applications/:id" element={<ApplicationDetailPage />} />
        <Route path="*" element={<NotFoundPage />} />
      </Route>
    </Routes>
  )
}

export default AppRoutes
