import { useState } from 'react';

const Formulario = (setPersona) => {
    const [edad, setEdad] = useState(0)
    const [peso, setPeso] = useState(0)
    const [sexo, setSexo] = useState('')
    const [fa, setFa] = useState(0)
    const [error, setError] = useState(false)

    const validaFormulario = (e => {
        e.preventDefault();
        if ([edad, peso, sexo, fa].includes('' || 0)) {
            setError(true);
            return
        }
        setError(false)

        const gastoBasal = () => {
            if (sexo === 'masculino') {
                if (edad >= 18 && edad <= 29) {
                    return ((13.37 * peso) + 747)
                } if (edad >= 30 && edad <= 59) {
                    return ((13.08 * peso) + 693)
                } if (edad > 60) {
                    return ((14.21 * peso) + 429)
                }
            } else {
                if (edad >= 18 && edad <= 29) {
                    return ((11.02 * peso) + 679)
                } if (edad >= 30 && edad <= 59) {
                    return ((10.92 * peso) + 677)
                } if (edad > 60) {
                    return ((10.92 * peso) + 520)
                }

            }
        }
        const caloriasFinal = () => {
            return (gastoBasal() * fa)
        }

        // const objetoPersona = {

        // }
        // setPersona(objetoPersona)

        console.log(gastoBasal());
        console.log(caloriasFinal());
    })



    return (
        <div className='bg-[#8EBED2] mx-3 rounded-md p-3 mb-2 md:w-1/2 lg:w-2/5 h-fit'>
            <h1 className='bg-[#2E86AB] p-2 text-center font-bold text-3xl mb-3 rounded-md text-white'>Datos</h1>
            <form className='' onSubmit={validaFormulario}>
                {error && <p className='p-2 m-2 rounded-md text-center font-bold bg-[#03045E] text-white'>Debes llenar todos los campos!</p>}
                <div className='mb-3 mt-5'>
                    <label htmlFor="edad">Edad </label>
                    <input type="number" id='edad' placeholder=' edad' className='p-2 block rounded-md w-full mb-1' value={edad} onChange={(e) => setEdad(e.target.value)} />
                </div>
                <div className='mb-3'>
                    <label htmlFor="peso">Peso </label>
                    <input type="number" id='peso' placeholder=' Peso' className='p-2 block rounded-md w-full mb-1' value={peso} onChange={(e) => setPeso(e.target.value)} />
                </div>
                <div>
                    <label htmlFor="genero">Genero</label><br />
                    <input type="radio" id="masculino" value={sexo} onChange={(e) => setSexo(e.target.value)} />
                    <label for="html"> Masculino</label>
                    <input type="radio" id="femenino" value={sexo} onChange={(e) => setSexo(e.target.value)} />
                    <label for="css"> Femenino</label><br />

                </div>
                <div>
                    <label for="fa">Factores de actividad: </label>

                    <select name="" id="fa" value={fa} onChange={(e) => setFa(e.target.value)}>
                        <option value="1.2">Sedentario</option>
                        <option value="1.3">Ligero</option>
                        <option value="1.5">Moderado</option>
                        <option value="1.7">Activo</option>
                        <option value="1.9">Vigoroso</option>
                    </select>

                </div>
                <div className='my-3 '>
                    <input type="submit" id='submit' className='bg-[#00B4DB] hover:bg-[#009cbf] p-2 rounded-md font-extrabold text-white block w-full'></input>
                </div>


            </form>
        </div>
    )
}

export default Formulario