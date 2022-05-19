
import Pacientes from './Pacientes'

const Listado = ({ pacientes, setPaciente, eliminarPaciente }) => {
    return (
        <div className='bg-[#84CEEB] text-center mx-10 mb-auto rounded-md p-10 overflow-y-scroll md:w-1/2 lg:w-3/5 md:h-screen'>
            <h2 className=' font-bold p-2 text-3xl text-center bg-purple-500  rounded-md text-white'>Listado de Pacientes</h2>
            <p className='text-xl text-center mt-5'>Administra tus <span className='font-bold text-cyan-500'>pacientes y citas</span></p>
            {
                pacientes.map(paciente => (
                    <Pacientes
                        key={paciente.id}
                        paciente={paciente}
                        setPaciente={setPaciente}
                        eliminarPaciente={eliminarPaciente}
                    />
                ))
            }


        </div>
    )
}

export default Listado