import { useState, useEffect } from 'react';
import Pacientes from './Pacientes';

const Formulario = ({ pacientes, setPacientes }) => {

    //TIP Definir el estado para el nombre
    const [nombre, setNombre] = useState('');
    const [email, setCorreo] = useState('');
    const [sintomas, setSintomas] = useState('');
    const [date, setDate] = useState('');

    const [error, setError] = useState(false)

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
            date
        }

        setPacientes([...pacientes, objetoPacientes]);
    })

    return (
        <div className='bg-slate-300 m-10 rounded-md p-10  md:w-1/2 lg:w-2/5'>
            <h1 className='bg-blue-500 text-center font-bold text-3xl mb-3 rounded-md'>Formulario</h1>
            <form className='' onSubmit={validaFormulario}>
                {error && <p className='p-2 m-2 rounded-md text-center font-bold bg-red-500 text-white'>debes llenar todos los campos</p>}
                <div className='mb-3'>
                    <label htmlFor="nombre">Nombre Paciente </label>
                    <input type="text" id='nombre' placeholder=' nombre' className=' block rounded-md w-full mb-1'
                        value={nombre} onChange={(e) => setNombre(e.target.value)} />
                </div>
                <div className='mb-3'>
                    <label htmlFor="email">Correo </label>
                    <input type="email" id='email' placeholder=' Correo' className='block rounded-md w-full mb-1'
                        value={email} onChange={(e) => setCorreo(e.target.value)} />
                </div>
                <div className='mb-3'>
                    <label htmlFor="sintomas">Sintomas </label>
                    <textarea className='w-full block rounded-lg p-1 mt-2' name="sintomas" id="sintomas" cols="30" rows="5"
                        value={sintomas} onChange={(e) => setSintomas(e.target.value)}></textarea>
                </div>
                <div className='mb-3'>
                    <label htmlFor="date">Fecha </label>
                    <input type="date" name="date" id="date" className='block rounded-md w-full mb-1'
                        value={date} onChange={(e) => setDate(e.target.value)} />
                </div>
                <div className='mb-3'>
                    <button type="submit" id='submit' className='bg-purple-300 p-2 hover:bg-slate-400 block w-full'>Enviar</button>
                </div>


            </form>
        </div>
    )
}

export default Formulario