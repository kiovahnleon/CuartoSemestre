

const Pacientes = ({ paciente, setPaciente, eliminarPaciente }) => {

    const handleEliminar = () => {
        const respuesta = confirm('seguro krnal?')
        if (respuesta) {
            eliminarPaciente(paciente.id);
        }
    }

    return (
        <div className=' mt-5 shadow-md bg-white p-10 rounded-md uppercase mb-3'>
            <p className='text-gray-600 font-bold'>Nombre del paciente <span className='font-normal normal-case'>{paciente.nombre}</span></p>
            <p className='text-gray-600 font-bold'>Correo <span className='font-normal normal-case'>{paciente.email}</span></p>
            <p className='text-gray-600 font-bold'>Sintomas <span className='font-normal normal-case'>{paciente.sintomas}</span></p>
            <p className='text-gray-600 font-bold'>Fecha <span className='font-normal normal-case'>{paciente.date}</span></p>
            <div className="flex justify-evenly gap-4 mt-4 text-white">
                <input type="button" value="Eliminar" className="p-2 w-full rounded-lg bg-[#023E8A] font-black hover:bg-[#023372]" onClick={handleEliminar} />
                <input type="button" value="Editar" className="p-2 w-full rounded-lg bg-[#0077B6] font-black hover:bg-[#016ba3] hover: cursor-pointer" onClick={() => setPaciente(paciente)} />
            </div>
        </div>
    )
}

export default Pacientes