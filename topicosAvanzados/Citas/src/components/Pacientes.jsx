

const Pacientes = ({ pacientes }) => {
    return (
        <div className=' mt-5 shadow-md bg-white p-10 rounded-md uppercase mb-3'>
            <p className='text-gray-600 font-bold'>Nombre del paciente: <span className='font-normal normal-case'>{pacientes.nombre}</span></p>
            <p className='text-gray-600 font-bold'>Correo <span className='font-normal normal-case'>{pacientes.email}</span></p>
            <p className='text-gray-600 font-bold'>Sintomas <span className='font-normal normal-case'>{pacientes.sintomas}</span></p>
            <p className='text-gray-600 font-bold'>Fecha <span className='font-normal normal-case'>{pacientes.date}</span></p>
        </div>
    )
}

export default Pacientes