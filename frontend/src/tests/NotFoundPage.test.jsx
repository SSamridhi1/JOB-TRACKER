import { render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { describe, expect, it } from 'vitest'
import NotFoundPage from '../pages/NotFoundPage.jsx'

// Example frontend test.
// Why this file exists: demonstrates the testing pattern (Vitest +
// React Testing Library) for the project, using the one page that has
// zero dependencies (no routing params, no API calls) to keep the example
// simple. Future page tests should follow this same shape.
describe('NotFoundPage', () => {
  it('renders a 404 message', () => {
    render(
      <MemoryRouter>
        <NotFoundPage />
      </MemoryRouter>,
    )

    expect(screen.getByText('404')).toBeInTheDocument()
    expect(screen.getByText('Page not found.')).toBeInTheDocument()
  })
})
