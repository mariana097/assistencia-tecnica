import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import UsuarioForm from '../components/UsuarioForm'

const mockListarUsuarios = vi.fn()
const mockCriarUsuario = vi.fn()
const mockAtualizarUsuario = vi.fn()
const mockDesativarUsuario = vi.fn()

vi.mock('../services/api', () => ({
  listarUsuarios: () => mockListarUsuarios(),
  criarUsuario: (data) => mockCriarUsuario(data),
  atualizarUsuario: (id, data) => mockAtualizarUsuario(id, data),
  desativarUsuario: (id) => mockDesativarUsuario(id)
}))

describe('UsuarioForm Component', () => {
  const mockUsuarios = [
    { id: 1, nome: 'João Silva', email: 'joao@email.com', tipo: 'CLIENTE', status: 'ATIVO' },
    { id: 2, nome: 'Maria Souza', email: 'maria@email.com', tipo: 'TECNICO', status: 'ATIVO' }
  ]

  beforeEach(() => {
    vi.clearAllMocks()
    mockListarUsuarios.mockResolvedValue(mockUsuarios)
  })

  it('deve renderizar lista de usuários', async () => {
    render(<UsuarioForm />)
    
    await waitFor(() => {
      expect(screen.getByText('João Silva')).toBeInTheDocument()
      expect(screen.getByText('Maria Souza')).toBeInTheDocument()
    })
  })

  it('deve cadastrar novo usuário', async () => {
    const novoUsuario = { nome: 'Novo User', email: 'novo@email.com', tipo: 'CLIENTE' }
    mockCriarUsuario.mockResolvedValue({ id: 3, ...novoUsuario })
    mockListarUsuarios.mockResolvedValue([...mockUsuarios, { ...novoUsuario, id: 3 }])

    render(<UsuarioForm />)
    
    await waitFor(() => {
      expect(screen.getByText('Gerenciar Usuários')).toBeInTheDocument()
    })
    
    const nomeInput = screen.getByLabelText(/nome/i)
    const emailInput = screen.getByLabelText(/e-mail/i)
    const senhaInput = screen.getByLabelText(/senha/i)
    const submitButton = screen.getByRole('button', { name: /cadastrar/i })
    
    await userEvent.type(nomeInput, 'Novo User')
    await userEvent.type(emailInput, 'novo@email.com')
    await userEvent.type(senhaInput, 'senha123')
    fireEvent.click(submitButton)
    
    await waitFor(() => {
      expect(mockCriarUsuario).toHaveBeenCalled()
    })
  })
})
