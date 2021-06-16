import '@testing-library/jest-dom'

import * as React from 'react'
import { render, fireEvent, screen } from '@testing-library/react'
import Input from '../components/Input'

test('shows the children when the checkbox is checked', () => {
  render(<HiddenMessage>{testMessage}</HiddenMessage>)

  expect(screen.queryByText(testMessage)).toBeNull()

  fireEvent.click(screen.getByLabelText(/show/i))

  expect(screen.getByText(testMessage)).toBeInTheDocument()
})