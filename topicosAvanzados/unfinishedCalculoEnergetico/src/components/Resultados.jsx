

const Resultados = (persona, setPersona) => {
    return (
        <div className='bg-[#8EBED2] text-center mx-3 mb-2 rounded-md p-3 overflow-y-scroll md:w-1/2 lg:w-3/5 h-fit'>
            <h2 className=' font-bold p-2 text-3xl text-center bg-[#2E86AB]  rounded-md text-white'>Listado de Pacientes</h2>
            <div>
                <p className='text-gray-600 font-bold'>Nombre del paciente <span className='font-normal normal-case'></span></p>
                <p className='text-gray-600 font-bold'>Correo <span className='font-normal normal-case'></span></p>
                <p className='text-gray-600 font-bold'>Sintomas <span className='font-normal normal-case'></span></p>
                <p className='text-gray-600 font-bold'>Fecha <span className='font-normal normal-case'></span></p>
            </div>
        </div>

    )
}

export default Resultados