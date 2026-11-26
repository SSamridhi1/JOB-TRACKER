import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Why this file exists:
// Vite needs to know we're a React project (via the plugin) and, for
// testing, where to find the test environment config. Keeping test config
// inside vite.config.js (instead of a separate jest.config.js) avoids
// maintaining two build pipelines.
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
  },
  test: {
    environment: 'jsdom',
    setupFiles: './src/tests/setup.js',
    globals: true,
  },
})
