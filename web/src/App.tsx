import { useState, ChangeEvent } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [dados, setDados] = useState({
    nome: '',
    cpf: '',
    endereco: '',
    valor: '',
  });

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setDados({ ...dados, [e.target.name]: e.target.value });
  };

  const handleSubmit = async () => {
    try {
      await axios.post('http://localhost:8000/api/v1/propostas/', dados);
    } catch (error: any) {
      console.log(error);
    }
  };

  return (
    <form onSubmit={ handleSubmit }>
      <h2>Envie sua proposta</h2>
      <div className="formulario">
        <label htmlFor="nome">Nome:</label>
        <input
          type="text"
          id="nome"
          name="nome"
          value={ dados.nome }
          onChange={ handleChange }
        />
      </div>
      <div className="formulario">
        <label htmlFor="cpf">Cpf:</label>
        <input
          type="text"
          id="cpf"
          name="cpf"
          value={ dados.cpf }
          onChange={ handleChange }
        />
      </div>
      <div className="formulario">
        <label htmlFor="endereco">Endereço:</label>
        <input
          type="text"
          id="endereco"
          name="endereco"
          value={ dados.endereco }
          onChange={ handleChange }
        />
      </div>
      <div className="formulario">
        <label htmlFor="valor">Valor:</label>
        <input
          type="text"
          id="valor"
          name="valor"
          value={ dados.valor }
          onChange={ handleChange }
        />
      </div>
      <button className="form-button" type="submit">Enviar</button>
    </form>
  );
}

export default App;
