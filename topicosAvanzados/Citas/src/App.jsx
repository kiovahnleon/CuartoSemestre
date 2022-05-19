import Cabecera from "./components/Cabecera"
import Formulario from "./components/Formulario"
import Listado from "./components/Listado"
import Pacientes from "./components/Pacientes"
import { useEffect, useState } from "react"

function App() {

  const [pacientes, setPacientes] = useState([]);
  const [paciente, setPaciente] = useState({});

  useEffect(() => {
    localStorage.setItem('pacientes', JSON.stringify(pacientes));
  }, [pacientes]);

  useEffect(() => {
    const pacientesLocalStorage = localStorage.getItem('pacientes');
  }, []);

  const eliminarPaciente = (id) => {
    console.log('Eliminando paciente: ', id);
    const pacientesActualizados = pacientes.filter(reemplazo => reemplazo.id !== id);
    setPacientes(pacientesActualizados);
  };


  return (
    <div className="text-slate-800">
      <Cabecera />
      <div className=" mt-3 md:flex p-5 w-full ">
        <Formulario
          setPacientes={setPacientes}
          pacientes={pacientes}
          paciente={paciente}
          setPaciente={setPaciente}
        />
        <Listado
          pacientes={pacientes}
          setPaciente={setPaciente}
          eliminarPaciente={eliminarPaciente}
        />
      </div>

    </div>
  )
}

export default App
