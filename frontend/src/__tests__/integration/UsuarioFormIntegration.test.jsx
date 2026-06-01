import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import UsuarioForm from '../../components/UsuarioForm'

describe('UsuarioForm Integration', () => {
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

  it('deve carregar usuários e cadastrar um novo usuário', async () => {
    const usuariosIniciais = [
      { id: 1, nome: 'João Silva', email: 'joao@email.com', tipo: 'CLIENTE', status: 'ATIVO' }
    ]
    const usuariosAtualizados = [
      ...usuariosIniciais,
      { id: 2, nome: 'Novo Usuário', email: 'novo@email.com', tipo: 'CLIENTE', status: 'ATIVO' }
    ]

    let fetchCount = 0
    global.fetch.mockImplementation((url, options = {}) => {
      if (url.endsWith('/usuarios') && (!options.method || options.method === 'GET')) {
        fetchCount += 1
        return Promise.resolve({ ok: true, json: async () => (fetchCount === 1 ? usuariosIniciais : usuariosAtualizados) })
      }

      if (url.endsWith('/usuarios') && options.method === 'POST') {
        return Promise.resolve({ ok: true, json: async () => usuariosAtualizados[1] })
      }

      return Promise.resolve({ ok: false, json: async () => ({ detail: 'Erro' }) })
    })

    const { container } = render(<UsuarioForm />)

    await waitFor(() => {
      expect(screen.getByText('João Silva')).toBeInTheDocument()
    })

    const nomeInput = container.querySelector("input[name='nome']")
    const emailInput = container.querySelector("input[name='email']")
    const senhaInput = container.querySelector("input[name='senha']")

    await userEvent.type(nomeInput, 'Novo Usuário')
    await userEvent.type(emailInput, 'novo@email.com')
    await userEvent.type(senhaInput, 'senha123')
    fireEvent.click(screen.getByRole('button', { name: /cadastrar/i }))

    await waitFor(() => {
      expect(global.fetch).toHaveBeenCalledWith(
        'http://localhost:8000/usuarios',
        expect.objectContaining({ method: 'POST' })
      )
      expect(screen.getByText('Novo Usuário')).toBeInTheDocument()
    })
  })
})
