import { useState, useEffect } from 'react';

const Formulario = () => {

    //TIP Definir el estado para el nombre
    const [nombre, setNombre] = useState('');
    const [email, setCorreo] = useState('');
    const [sintomas, setSintomas] = useState('');
    const [date, setDate] = useState('');

    const validaFormulario = (e => {
        e.preventDefault();
        console.log('validando formulario');
        console.log(nombre);
        console.log(email);
        console.log(sintomas);
        console.log(date);
    })

    return (
        <div className='bg-slate-300 m-10 rounded-md p-4  md:w-1/2 lg:w-2/5'>
            <h1 className='bg-blue-500 text-center'>Formulario</h1>
            <form className='container mx-2' onSubmit={validaFormulario}>
                <div>
                    <label htmlFor="nombre">Nombre Paciente </label>
                    <input type="text" id='nombre' placeholder=' nombre' className=' block rounded-md w-full mb-1'
                        value={nombre} onChange={(e) => setNombre(e.target.value)} />
                </div>
                <div>
                    <label htmlFor="email">Correo </label>
                    <input type="email" id='email' placeholder=' Correo' className='block rounded-md w-full mb-1'
                        value={email} onChange={(e) => setCorreo(e.target.value)} />
                </div>
                <div>
                    <label htmlFor="sintomas">Sintomas </label>
                    <textarea className='w-full block rounded-lg p-1 mt-2' name="sintomas" id="sintomas" cols="30" rows="5"
                        value={sintomas} onChange={(e) => setSintomas(e.target.value)}></textarea>
                </div>
                <div>
                    <label htmlFor="date">Fecha </label>
                    <input type="date" name="date" id="date" className='block rounded-md w-full mb-1'
                        value={date} onChange={(e) => setDate(e.target.value)} />
                </div>
                <div className='m-3'>
                    <button type="submit" id='submit' className='bg-purple-300 m-2 pr-4 p-2 hover:bg-slate-400 block w-full'>Enviar</button>
                </div>


            </form>
        </div>
    )
}

export default Formulario