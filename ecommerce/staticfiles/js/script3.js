$(document).ready(function() {


    //Función que obtendrá el listado de las bicicletas através 
    function obtenerBicicletas() {
        //através de fetch nos dirigimos a la dirección url que nos devolverá el listado de las bicicletas disponibles.
        fetch('https://api-bicicletas-705c23e6eeff.herokuapp.com/bicicletas')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Error al obtener los datos');
                }
                return response.json();
            })
            .then(data => {
                // Recorrer e imprimir los resultados en las tarjetas de bicicletas en una constante que tendrá una card con los datos especificados.
                const tarjetasBicicletas = document.getElementById('tarjetasBicicletas');
                data.forEach(bicicleta => {

                  
                    const card = `
                        <div class="col-md-3">
                            <div class="card" onclick="window.location.href='bici_altitude.html';">
                                <img src="${bicicleta.img}" class="card-img-top mx-auto d-block" alt="Foto de una bicicleta">
                                <div class="card-body text-center">
                                    <h4 class="card-precio">${bicicleta.valor}</h4>
                                    <h5 class="card-title">${bicicleta.modelo}</h5>
                                    <p class="card-text">${bicicleta.descripcion}</p>
                                </div>
                            </div>
                        </div>
                    `;
                    tarjetasBicicletas.innerHTML += card;
                });
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }

    obtenerBicicletas();
});