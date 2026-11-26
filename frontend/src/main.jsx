import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import App from './App.jsx'
import './index.css'

// Why this file exists:
// This is the one place that mounts React onto the actual DOM node
// (#root in index.html). BrowserRouter lives here (not in App.jsx) so
// that App.jsx stays testable without needing a router wrapper in tests.
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
)
