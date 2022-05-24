
import Pacientes from './Pacientes'

const Listado = ({ pacientes, setPaciente, eliminarPaciente }) => {
    return (
        <div className='bg-[#8EBED2] text-center mx-3 mb-2 rounded-md p-3 overflow-y-scroll md:w-1/2 lg:w-3/5 h-fit'>
            <h2 className=' font-bold p-2 text-3xl text-center bg-[#2E86AB]  rounded-md text-white'>Listado de Pacientes</h2>
            <p className='text-xl text-center mt-5'>Administra tus <span className='font-bold text-[#2E86AB]'>pacientes y citas</span></p>
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