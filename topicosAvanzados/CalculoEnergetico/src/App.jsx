import { useState } from "react"
import Cabecera from "./components/Cabecera"
import Formulario from "./components/Formulario"
import Resultados from "./components/Resultados"

function App() {
  const [persona, setPersona] = useState({})
  return (
    <div className="text-slate-800 font-semibold">
      <Cabecera />
      <div className=" mt-3 md:flex p-2 w-full">
        <Formulario
          setPersona={setPersona}
        />
        <Resultados
          persona={persona}
        />
      </div>

    </div>
  )
}

export default App
