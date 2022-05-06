
import Pacientes from './Pacientes'

const Listado = ({ pacientes }) => {
    return (
        <div className='bg-slate-300 text-center m-10 rounded-md p-10 overflow-y-scroll md:w-1/2 lg:w-3/5 md:h-screen'>
            <h2 className=' font-bold text-3xl text-center bg-blue-500 rounded-md'>Listado de Pacientes</h2>
            <p className='text-xl text-center mt-5'>Administra tus <span className='font-bold text-cyan-500'>pacientes y citas</span></p>
            {
                pacientes.map(pacientes => (
                    <Pacientes
                        pacientes={pacientes}
                    />
                ))
            }


        </div>
    )
}

export default Listado