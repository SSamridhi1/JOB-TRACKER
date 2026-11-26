import '@testing-library/jest-dom'

// Why this file exists:
// Vitest's jsdom environment doesn't include jest-dom's extra matchers
// (toBeInTheDocument, etc.) by default. This setup file (referenced from
// vite.config.js's test.setupFiles) runs before every test file and
// registers them globally, so individual test files don't need to import it.
