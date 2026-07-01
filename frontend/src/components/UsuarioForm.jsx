import React, { useState, useEffect } from 'react';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const UsuarioForm = () => {
    const [usuarios, setUsuarios] = useState([]);
    const [formData, setFormData] = useState({
        email: '',
        senha: '',
        nome: '',
        tipo: 'CLIENTE'
    });
    const [editingId, setEditingId] = useState(null);
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    const getToken = () => localStorage.getItem('token');

    const carregarUsuarios = async () => {
        try {
            const response = await fetch(`${API_URL}/usuarios`, {
                headers: { 'Authorization': `Bearer ${getToken()}` }
            });
            if (response.ok) {
                const data = await response.json();
                setUsuarios(data);
            }
        } catch (err) {
            setError('Erro ao carregar usuários');
        }
    };

    useEffect(() => {
        carregarUsuarios();
    }, []);

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setLoading(true);

        try {
            const url = editingId 
                ? `${API_URL}/usuarios/${editingId}`
                : `${API_URL}/usuarios`;
            const method = editingId ? 'PUT' : 'POST';

            const response = await fetch(url, {
                method,
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${getToken()}`
                },
                body: JSON.stringify(formData)
            });

            if (!response.ok) throw new Error('Erro ao salvar usuário');

            setFormData({ email: '', senha: '', nome: '', tipo: 'CLIENTE' });
            setEditingId(null);
            carregarUsuarios();
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    const handleEdit = (usuario) => {
        setFormData({
            email: usuario.email,
            senha: '',
            nome: usuario.nome,
            tipo: usuario.tipo || 'CLIENTE'
        });
        setEditingId(usuario.id);
    };

    const handleDelete = async (id) => {
        if (window.confirm('Tem certeza que deseja desativar este usuário?')) {
            try {
                await fetch(`${API_URL}/usuarios/${id}`, {
                    method: 'DELETE',
                    headers: { 'Authorization': `Bearer ${getToken()}` }
                });
                carregarUsuarios();
            } catch (err) {
                setError('Erro ao desativar usuário');
            }
        }
    };

    const handleCancel = () => {
        setFormData({ email: '', senha: '', nome: '', tipo: 'CLIENTE' });
        setEditingId(null);
        setError('');
    };

    return (
        <div className="usuario-container">
            <h2>Gerenciar Usuários</h2>
            
            {error && <div className="error-message">{error}</div>}
            
            <form onSubmit={handleSubmit} className="usuario-form">
                <h3>{editingId ? 'Editar Usuário' : 'Novo Usuário'}</h3>
                
                <div className="form-group">
                    <label>Nome:</label>
                    <input
                        type="text"
                        name="nome"
                        value={formData.nome}
                        onChange={handleChange}
                        required
                    />
                </div>

                <div className="form-group">
                    <label>E-mail:</label>
                    <input
                        type="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        required
                    />
                </div>

                <div className="form-group">
                    <label>Senha:</label>
                    <input
                        type="password"
                        name="senha"
                        value={formData.senha}
                        onChange={handleChange}
                        required={!editingId}
                    />
                </div>

                <div className="form-group">
                    <label>Tipo:</label>
                    <select name="tipo" value={formData.tipo} onChange={handleChange}>
                        <option value="CLIENTE">Cliente</option>
                        <option value="TECNICO">Técnico</option>
                        <option value="ADMIN">Administrador</option>
                    </select>
                </div>

                <div className="form-actions">
                    <button type="submit" disabled={loading}>
                        {editingId ? 'Atualizar' : 'Cadastrar'}
                    </button>
                    {editingId && (
                        <button type="button" onClick={handleCancel}>
                            Cancelar
                        </button>
                    )}
                </div>
            </form>

            <div className="usuarios-list">
                <h3>Usuários Cadastrados</h3>
                <table className="table">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Nome</th>
                            <th>E-mail</th>
                            <th>Tipo</th>
                            <th>Status</th>
                            <th>Ações</th>
                        </tr>
                    </thead>
                    <tbody>
                        {usuarios.map((usuario) => (
                            <tr key={usuario.id}>
                                <td>{usuario.id}</td>
                                <td>{usuario.nome}</td>
                                <td>{usuario.email}</td>
                                <td>{usuario.tipo}</td>
                                <td>{usuario.status}</td>
                                <td>
                                    <button onClick={() => handleEdit(usuario)}>Editar</button>
                                    <button onClick={() => handleDelete(usuario.id)}>Desativar</button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default UsuarioForm;
