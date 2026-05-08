const API_URL = 'http://localhost:8000';

const getToken = () => localStorage.getItem('token');

const request = async (endpoint, options = {}) => {
    const response = await fetch(`${API_URL}${endpoint}`, {
        ...options,
        headers: {
            'Content-Type': 'application/json',
            ...(getToken() && { 'Authorization': `Bearer ${getToken()}` }),
            ...options.headers,
        },
    });

    if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || 'Erro na requisição');
    }

    return response.json();
};

export const login = async (email, senha) => {
    return request('/auth/login', {
        method: 'POST',
        body: JSON.stringify({ email, senha }),
    });
};

export const listarUsuarios = async () => {
    return request('/usuarios');
};

export const criarUsuario = async (data) => {
    return request('/usuarios', {
        method: 'POST',
        body: JSON.stringify(data),
    });
};

export const atualizarUsuario = async (id, data) => {
    return request(`/usuarios/${id}`, {
        method: 'PUT',
        body: JSON.stringify(data),
    });
};

export const desativarUsuario = async (id) => {
    return request(`/usuarios/${id}`, {
        method: 'DELETE',
    });
};

export const listarFuncionarios = async () => {
    return request('/funcionarios');
};

export const criarFuncionario = async (data) => {
    return request('/funcionarios', {
        method: 'POST',
        body: JSON.stringify(data),
    });
};
