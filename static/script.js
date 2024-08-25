// script.js
// Funciones para redirigir a las rutas correspondientes
function editarReparacion(id) {
    window.location.href = `/editar_reparacion/${id}`;
}

function eliminarReparacion(id) {
    if (confirm("¿Estás seguro de que deseas eliminar esta reparación?")) {
        window.location.href = `/eliminar_reparacion/${id}`;
    }
}

function visualizarReparacion(id) {
    window.location.href = `/ver_reparacion/${id}`;
}

function cerrarVentana() {
    window.close();
}

function nuevaReparacion() {
    window.location.href = "/nueva_reparacion";
}

// script.js
function filtrarReparaciones(estado) {
    $.ajax({
        type: "GET",
        url: "/reparaciones/estado",
        data: { estado: estado },
        success: function(data) {
            $("tbody").html("");
            $.each(data, function(index, reparacion) {
                $("tbody").append(`
                    <tr>
                        <td>${reparacion.id}</td>
                        <td>${reparacion.patente}</td>
                        <td>${reparacion.nombre_apellido}</td>
                        <td>${reparacion.fecha_ingreso}</td>
                        <td>${reparacion.fecha_egreso}</td>
                        <td>${reparacion.descripcion}</td>
                        <td> $ ${reparacion.presupuesto}</td>
                        <td>
                            {% if reparacion.estado == 'sin empezar' %}
                            <span class="badge badge-danger">${reparacion.estado}</span>
                            {% elif reparacion.estado == 'en proceso' %}
                            <span class="badge badge-warning">${reparacion.estado}</span>
                            {% else %}
                            <span class="badge badge-success">${reparacion.estado}</span>
                            {% endif %}
                        </td>
                        <td>
                            <button class="btn btn-info" onclick="visualizarReparacion(${reparacion.id})">
                                <i class="fas fa-eye"></i> Visualizar
                            </button>
                            <button class="btn btn-primary" onclick="editarReparacion(${reparacion.id})">Editar</button>
                            <button class="btn btn-danger" onclick="eliminarReparacion(${reparacion.id})">Eliminar</button>
                        </td>
                    </tr>
                `);
            });
        }
    });
}

// Evento de escucha para el formulario de editar reparación
document.addEventListener("DOMContentLoaded", function () {
    const editarReparacionForm = document.getElementById("editar-reparacion-form");
    if (editarReparacionForm) {
        editarReparacionForm.addEventListener("submit", function (e) {
            e.preventDefault(); // Evita que se envíe el formulario de manera tradicional
            const formData = new FormData(editarReparacionForm); // Crea un objeto FormData con los datos del formulario
            fetch("/editar_reparacion", {
                method: "POST", // Envía una solicitud POST
                body: formData, // Envía los datos del formulario
            })
                .then((response) => response.json()) // Espera la respuesta del servidor y la convierte a JSON
                .then((data) => {
                    if (data.success) { // Si la solicitud es exitosa
                        window.location.href = "/"; // Redirige a la página principal
                    } else {
                        alert("Error al editar la reparación"); // Muestra un mensaje de error
                    }
                })
                .catch((error) => console.error(error)); // Captura cualquier error que ocurra
        });
    }
});

// Evento para cambiar el estado seleccionado
$("#estado-dropdown ul li a").on("click", function() {
    var estado = $(this).data("estado");
    $("#estado-selected").text(estado.charAt(0).toUpperCase() + estado.slice(1));
    filtrarReparaciones(estado);
});

// Filtrar reparaciones por defecto (Todo)
filtrarReparaciones("todo");