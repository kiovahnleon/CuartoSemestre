import Cabecera from "./components/Cabecera"
import Formulario from "./components/Formulario"
import Listado from "./components/Listado"

function App() {

  return (
    <div>
      <Cabecera />
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
        <Formulario />
        <Listado />
      </div>

    </div>
  )
}

export default App
