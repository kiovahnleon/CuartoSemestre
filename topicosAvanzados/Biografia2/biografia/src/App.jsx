function App() {

  return (
    <div className="text-slate-700 mx-14 ">
      <h1 className="text-2xl md:text-6xl text-center font-black rounded-lg uppercase p-10 text-slate-100">Biografia</h1>
      <div className=" bg-white rounded-lg p-[10%] ">
        <div className="pb-10 grid grid-cols-2 gap-4">
          <img src="https://pbs.twimg.com/media/FRVHj_VVIAAFCFa?format=png&name=240x240" alt="profilepic" className="rounded-full" />
          <h1 className="text-transparent bg-clip-text bg-gradient-to-br from-yellow-400 to-orange-600"><span className="md:text-6xl text-2xl font-bold">Kiovahn Leon</span><br /> <span className="font-thin text-lg">Instituto Tecnologico de Ensenada</span></h1>
        </div>
        <div className="grid grid-cols-2 gap-4">
          <div className="..."><h1 className=" font-black">Experiencia</h1>Experiencia muy limitada</div>
          <div className="..."><h1 className="font-black">Habilidades Personales</h1>
            <ul>
              <li>Moverle un poco a la guitarra</li>
              <li>Jugar medianamente futbol</li>
            </ul>
          </div>
          <div className="..."><h1 className='font-black'>Educacion</h1>
            <ul>
              <li>EST Num.19 - Tecnico en Electronica</li>
              <li>CBTis Num. 41 - Tecnico en Electronica</li>
            </ul>
          </div>
          <div className="..."><h1 className='font-black'>Referencias</h1>
            <ul>
              <li>Pablo Palmeras <span className='font-light'>(465 929 89 12)</span></li>
              <li>Kevin Salaas <span className='font-light'>(475 858 90 14)</span></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  )
}

export default App
