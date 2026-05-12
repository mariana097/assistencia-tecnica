import { describe, it, expect, vi, beforeEach } from 'vitest'
import { login, listarUsuarios, criarUsuario } from '../services/api'

describe('API Service', () => {
  beforeEach(() => {
    vi.clearAllMocks()
    global.fetch = vi.fn()
  })

  it('deve fazer login com sucesso', async () => {
    const mockResponse = { token: 'fake-token', user: { id: 1 } }
    global.fetch.mockResolvedValue({
      ok: true,
      json: async () => mockResponse
    })

    const result = await login('teste@email.com', 'senha123')
    expect(result).toEqual(mockResponse)
    expect(global.fetch).toHaveBeenCalledWith(
      'http://localhost:8000/auth/login',
      expect.objectContaining({
        method: 'POST',
        body: JSON.stringify({ email: 'teste@email.com', senha: 'senha123' })
      })
    )
  })

  it('deve lançar erro quando login falha', async () => {
    global.fetch.mockResolvedValue({
      ok: false,
      json: async () => ({ detail: 'Credenciais inválidas' })
    })

    await expect(login('teste@email.com', 'senha_errada')).rejects.toThrow()
  })
})
