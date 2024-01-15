$("#id_factory_area").change(function () {
    let url = $("#reviewForm").attr("data-equipments-url");  // get the url of the `load_equipments` view
    let factoryareaId = $(this).val();  // get the selected factory area ID from the HTML input

    $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= /ajax/load-equipments/)
        data: {
            'factory_area': factoryareaId       // add the factory area id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_equipments` view function
            $("#id_equipment").html(data);  // replace the contents of the city input with the data that came from the server
        }
    });

});