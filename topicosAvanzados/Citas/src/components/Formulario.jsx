import React from 'react'

const Formulario = () => {
    return (
        <div className='bg-slate-300 m-10 rounded-md p-4  md:w-1/2 lg:w-2/5'>
            <h1 className=' text-center'>Formulario</h1>
            <form className='container mx-2'>
                <div>
                    <label htmlFor="nombrePaciente">Nombre Paciente </label>
                    <input type="text" placeholder=' nombre' className=' block rounded-md w-full mb-1' />
                </div>
                <div>
                    <label htmlFor="email">Correo </label>
                    <input type="email" className='block rounded-md w-full mb-1' />
                </div>
                <div>
                    <label htmlFor="sintomas">Sintomas </label>
                    <input type="text" className='block rounded-md w-full mb-1' />
                </div>
                <div>
                    <label htmlFor="date">Fecha </label>
                    <input type="date" name="date" id="date" className='block rounded-md w-full mb-1' />
                </div>
                <div className='m-3'>
                    <button type="submit" className='bg-purple-300 m-2 p-2 hover:bg-slate-400 block w-full'>Enviar</button>
                </div>


            </form>
        </div>
    )
}

export default Formulario