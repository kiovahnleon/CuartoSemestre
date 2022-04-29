import Cabecera from "./components/Cabecera"
import Formulario from "./components/Formulario"
import Listado from "./components/Listado"

function App() {

  return (
    <div className="text-slate-800">
      <Cabecera />
      <div className=" mt-12 md:flex">
        <Formulario />
        <Listado />
      </div>

    </div>
  )
}

export default App
