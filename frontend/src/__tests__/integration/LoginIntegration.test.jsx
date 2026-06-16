import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import Login from '../../components/Login'

describe('Login Integration', () => {
  beforeEach(() => {
    vi.clearAllMocks()

    const store = {}
    const localStorageMock = {
      getItem: (key) => (key in store ? store[key] : null),
      setItem: (key, value) => { store[key] = String(value) },
      removeItem: (key) => { delete store[key] },
      clear: () => { Object.keys(store).forEach((key) => delete store[key]) }
    }

    Object.defineProperty(window, 'localStorage', {
      value: localStorageMock,
      writable: true,
    })

    global.fetch = vi.fn()
  })

  it('deve armazenar token e usuário no localStorage ao efetuar login', async () => {
    const mockResponse = {
      token: 'fake-token',
      user: { id: 1, nome: 'Teste', email: 'teste@email.com' }
    }

    global.fetch.mockResolvedValue({
      ok: true,
      json: async () => mockResponse
    })

    const onLoginSuccess = vi.fn()
    render(<Login onLoginSuccess={onLoginSuccess} />)

    await userEvent.type(screen.getByLabelText(/e-mail/i), 'teste@email.com')
    await userEvent.type(screen.getByLabelText(/senha/i), 'senha123')
    fireEvent.click(screen.getByRole('button', { name: /entrar/i }))

    await waitFor(() => {
      expect(global.fetch).toHaveBeenCalled()
      expect(window.localStorage.getItem('token')).toBe('fake-token')
      expect(JSON.parse(window.localStorage.getItem('user'))).toEqual(mockResponse.user)
      expect(onLoginSuccess).toHaveBeenCalledWith(mockResponse.user)
    })
  })

  it('deve exibir mensagem de erro quando o login falhar', async () => {
    global.fetch.mockResolvedValue({ ok: false })

    render(<Login onLoginSuccess={vi.fn()} />)

    await userEvent.type(screen.getByLabelText(/e-mail/i), 'teste@email.com')
    await userEvent.type(screen.getByLabelText(/senha/i), 'senha_errada')
    fireEvent.click(screen.getByRole('button', { name: /entrar/i }))

    await waitFor(() => {
      expect(screen.getByText(/credenciais inválidas/i)).toBeInTheDocument()
      expect(window.localStorage.getItem('token')).toBeNull()
    })
  })
})
