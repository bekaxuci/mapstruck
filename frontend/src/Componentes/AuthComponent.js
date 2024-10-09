import React, { useState } from 'react';
import '../Css/AuthComponent.css'; // Asegúrate de importar el archivo CSS

const ComponenteAutenticacion = () => {
  const [registrando, setRegistrando] = useState(false);
  const [datosFormulario, setDatosFormulario] = useState({
    email: '',
    contraseña: '',
    nombre: '',
    apellido: '',
  });

  const manejarCambio = (e) => {
    const { name, value } = e.target;
    setDatosFormulario({
      ...datosFormulario,
      [name]: value,
    });
  };

  const manejarEnvio = (e) => {
    e.preventDefault();
    if (registrando) {
      // Lógica para registrar el usuario
      console.log('Registro:', datosFormulario);
      // Aquí puedes hacer una llamada a tu API para registrar al usuario
    } else {
      // Lógica para acceder
      console.log('Acceso:', datosFormulario);
      // Aquí puedes hacer una llamada a tu API para acceder
    }
  };

  return (
    <div className="auth-container">
      <h2>{registrando ? 'Registro' : 'Acceso'}</h2>
      <form onSubmit={manejarEnvio}>
        <div className="input-group">
          <label>Email:</label>
          <input
            type="email"
            name="email"
            value={datosFormulario.email}
            onChange={manejarCambio}
            required
          />
        </div>
        <div className="input-group">
          <label>Contraseña:</label>
          <input
            type="password"
            name="contraseña"
            value={datosFormulario.contraseña}
            onChange={manejarCambio}
            required
          />
        </div>
        {registrando && (
          <>
            <div className="input-group">
              <label>Nombre:</label>
              <input
                type="text"
                name="nombre"
                value={datosFormulario.nombre}
                onChange={manejarCambio}
                required
              />
            </div>
            <div className="input-group">
              <label>Apellido:</label>
              <input
                type="text"
                name="apellido"
                value={datosFormulario.apellido}
                onChange={manejarCambio}
                required
              />
            </div>
          </>
        )}
        <button type="submit">{registrando ? 'Registrar' : 'Acceder'}</button>
      </form>
      <button onClick={() => setRegistrando(!registrando)}>
        {registrando ? 'Ya tengo una cuenta' : 'Crear cuenta'}
      </button>
    </div>
  );
};

export default ComponenteAutenticacion;
