import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import UsuarioForm from '../components/UsuarioForm'

describe('UsuarioForm Component', () => {
  const mockUsuarios = [
    { id: 1, nome: 'João Silva', email: 'joao@email.com', tipo: 'CLIENTE', status: 'ATIVO' },
    { id: 2, nome: 'Maria Souza', email: 'maria@email.com', tipo: 'TECNICO', status: 'ATIVO' }
  ]

  beforeEach(() => {
    vi.clearAllMocks()
    const store = { token: 'fake-token' }
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

  it('deve renderizar lista de usuários', async () => {
    global.fetch.mockResolvedValueOnce({ ok: true, json: async () => mockUsuarios })

    render(<UsuarioForm />)

    await waitFor(() => {
      expect(screen.getByText('João Silva')).toBeInTheDocument()
      expect(screen.getByText('Maria Souza')).toBeInTheDocument()
    })
  })

  it('deve cadastrar novo usuário', async () => {
    const novoUsuario = { nome: 'Novo User', email: 'novo@email.com', tipo: 'CLIENTE' }

    global.fetch
      .mockResolvedValueOnce({ ok: true, json: async () => mockUsuarios })
      .mockResolvedValueOnce({ ok: true, json: async () => ({ id: 3, ...novoUsuario, status: 'ATIVO' }) })
      .mockResolvedValueOnce({ ok: true, json: async () => [...mockUsuarios, { ...novoUsuario, id: 3 }] })

    render(<UsuarioForm />)

    await waitFor(() => {
      expect(screen.getByText('Gerenciar Usuários')).toBeInTheDocument()
    })

    const nomeInput = document.querySelector("input[name='nome']")
    const emailInput = document.querySelector("input[name='email']")
    const senhaInput = document.querySelector("input[name='senha']")
    const submitButton = screen.getByRole('button', { name: /cadastrar/i })

    await userEvent.type(nomeInput, 'Novo User')
    await userEvent.type(emailInput, 'novo@email.com')
    await userEvent.type(senhaInput, 'senha123')
    fireEvent.click(submitButton)

    await waitFor(() => {
      expect(global.fetch).toHaveBeenCalledWith(
        'http://localhost:8000/usuarios',
        expect.objectContaining({
          method: 'POST',
          headers: expect.objectContaining({ 'Content-Type': 'application/json' }),
        })
      )
      expect(screen.getByText('Novo User')).toBeInTheDocument()
    })
  })
})
