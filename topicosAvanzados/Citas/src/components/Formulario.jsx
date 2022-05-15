import { useState, useEffect } from 'react';
import Pacientes from './Pacientes';

const Formulario = ({ pacientes, setPacientes, paciente }) => {

    //TIP Definir el estado para el nombre
    const [nombre, setNombre] = useState('');
    const [email, setCorreo] = useState('');
    const [sintomas, setSintomas] = useState('');
    const [date, setDate] = useState('');

    const [error, setError] = useState(false)



    useEffect(() => {
        if (Object.keys(paciente).length > 0) {
            setNombre(paciente.nombre)
            setCorreo(paciente.email)
            setSintomas(paciente.sintomas)
            setDate(paciente.date)
        }
    }, [paciente]);

    const generarID = () => {
        const random = Math.random().toString(16).substring(2);
        const fecha = Date.now().toString(36);
        return random + fecha;
    }

    const validaFormulario = (e => {
        e.preventDefault();
        if ([nombre, email, sintomas, date].includes('')) {
            setError(true);
            return
        }

        //TIP se coloca el error en falso para indicar que todos los campos estan llenos
        setError(false)

        const objetoPacientes = {
            nombre,
            email,
            sintomas,
            date,
            id: generarID()
        }

        setPacientes([...pacientes, objetoPacientes]);
        limpiarDatos();
    })

    const limpiarDatos = () => {
        setNombre('')
        setCorreo('')
        setSintomas('')
        setDate('')
    }

    return (
        <div className='bg-[#84CEEB] m-10 rounded-md p-10 mb-auto md:w-1/2 lg:w-2/5'>
            <h1 className='bg-gradient-to-r from-purple-500 to-blue-500 p-2 text-center font-bold text-3xl mb-3 rounded-md text-white'>Formulario</h1>
            <form className='' onSubmit={validaFormulario}>
                {error && <p className='p-2 m-2 rounded-md text-center font-bold bg-red-500 text-white'>debes llenar todos los campos</p>}
                <div className='mb-3'>
                    <label htmlFor="nombre">Nombre Paciente </label>
                    <input type="text" id='nombre' placeholder=' nombre' className='p-2 block rounded-md w-full mb-1'
                        value={nombre} onChange={(e) => setNombre(e.target.value)} />
                </div>
                <div className='mb-3'>
                    <label htmlFor="email">Correo </label>
                    <input type="email" id='email' placeholder=' Correo' className='p-2 block rounded-md w-full mb-1'
                        value={email} onChange={(e) => setCorreo(e.target.value)} />
                </div>
                <div className='mb-3'>
                    <label htmlFor="sintomas">Sintomas </label>
                    <textarea className=' p-2 w-full block rounded-lg mt-2' name="sintomas" id="sintomas" cols="30" rows="5"
                        value={sintomas} onChange={(e) => setSintomas(e.target.value)}></textarea>
                </div>
                <div className='mb-3'>
                    <label htmlFor="date">Fecha </label>
                    <input type="date" name="date" id="date" className='p-2 block rounded-md w-full mb-1'
                        value={date} onChange={(e) => setDate(e.target.value)} />
                </div>
                <div className='mb-3'>
                    <button type="submit" id='submit' className='bg-gradient-to-r from-purple-500 to-blue-500 hover:from-blue-500 hover:to-purple-500 p-2 rounded-md font-extrabold text-white block w-full'>Enviar</button>
                </div>


            </form>
        </div>
    )
}

export default Formulario