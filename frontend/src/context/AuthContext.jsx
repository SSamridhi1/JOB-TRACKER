import { createContext, useContext, useState } from 'react'

// Why this file exists:
// Auth state (current user, is-logged-in) is needed across many unrelated
// components (navbar, protected routes, login page). React Context avoids
// prop-drilling that state through every layer. Skeleton only - state is
// declared but never set by real login logic yet.

const AuthContext = createContext(undefined)

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null)

  const value = { user, setUser }

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
}

export function useAuth() {
  const context = useContext(AuthContext)
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider')
  }
  return context
}
