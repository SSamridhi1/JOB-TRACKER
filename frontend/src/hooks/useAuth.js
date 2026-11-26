// Why this file exists:
// Re-exports the context hook so pages import from `hooks/useAuth` -
// a consistent "hooks live in hooks/" convention - without needing to know
// the auth state actually lives in Context under the hood.

export { useAuth } from '../context/AuthContext.jsx'
