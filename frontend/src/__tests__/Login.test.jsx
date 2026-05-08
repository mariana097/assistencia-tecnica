import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import Login from '../components/Login'

// Mock da API
const mockLogin = vi.fn()
vi.mock('../services/api', () => ({
  login: (...args) => mockLogin(...args)
}))

describe('Login Component', () => {
  const mockOnLoginSuccess = vi.fn()

  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('deve renderizar o formulário de login', () => {
    render(<Login onLoginSuccess={mockOnLoginSuccess} />)
    
    expect(screen.getByLabelText(/e-mail/i)).toBeInTheDocument()
    expect(screen.getByLabelText(/senha/i)).toBeInTheDocument()
    expect(screen.getByRole('button', { name: /entrar/i })).toBeInTheDocument()
  })

  it('deve fazer login com sucesso', async () => {
    const mockResponse = {
      token: 'fake-token',
      user: { id: 1, nome: 'Teste', email: 'teste@email.com' }
    }
    mockLogin.mockResolvedValue(mockResponse)

    render(<Login onLoginSuccess={mockOnLoginSuccess} />)
    
    const emailInput = screen.getByLabelText(/e-mail/i)
    const passwordInput = screen.getByLabelText(/senha/i)
    const submitButton = screen.getByRole('button', { name: /entrar/i })
    
    await userEvent.type(emailInput, 'teste@email.com')
    await userEvent.type(passwordInput, 'senha123')
    fireEvent.click(submitButton)
    
    await waitFor(() => {
      expect(mockLogin).toHaveBeenCalledWith('teste@email.com', 'senha123')
      expect(mockOnLoginSuccess).toHaveBeenCalledWith(mockResponse.user)
    })
  })

  it('deve exibir erro quando credenciais são inválidas', async () => {
    mockLogin.mockRejectedValue(new Error('Credenciais inválidas'))

    render(<Login onLoginSuccess={mockOnLoginSuccess} />)
    
    const emailInput = screen.getByLabelText(/e-mail/i)
    const passwordInput = screen.getByLabelText(/senha/i)
    const submitButton = screen.getByRole('button', { name: /entrar/i })
    
    await userEvent.type(emailInput, 'teste@email.com')
    await userEvent.type(passwordInput, 'senha_errada')
    fireEvent.click(submitButton)
    
    await waitFor(() => {
      expect(screen.getByText(/credenciais inválidas/i)).toBeInTheDocument()
    })
    expect(mockOnLoginSuccess).not.toHaveBeenCalled()
  })
})
