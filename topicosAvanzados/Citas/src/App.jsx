import Cabecera from "./components/Cabecera"
import Formulario from "./components/Formulario"
import Listado from "./components/Listado"
import Pacientes from "./components/Pacientes"
import { useState } from "react"

function App() {

  const [pacientes, setPacientes] = useState([]);
  const [paciente, setPaciente] = useState({});


  return (
    <div className="text-slate-800">
      <Cabecera />
      <div className=" mt-3 md:flex p-5 w-full ">
        <Formulario
          setPacientes={setPacientes}
          pacientes={pacientes}
          paciente={paciente}
        />
        <Listado
          pacientes={pacientes}
          setPaciente={setPaciente}
        />
      </div>

    </div>
  )
}

export default App
