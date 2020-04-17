$(document).ready(function () {
    // $("#id_species").change(function () {
    //     var form = $(this).closest("form");
    //     console.log(tes);
    //     $.ajax({
    //         url: $(this).url,
    //         data: {
    //             'species_id': $(this).val(),
    //             'crop_family': $("#id_crop_family").val()
    //         },
    //         dataType: 'json',
    //         success: function (data) {
    //             $("#id_serial_no").val(data.serial_no);
    //         }
    //     });
    // });

    $("#id_variety_supplier_name").change(function () {
        var form = $(this).closest("form");
        console.log("working");
        $.ajax({
            url: form.attr("data-validate-variety-supplier-name-url"),
            data: form.serialize(),
            dataType: 'json',
            success: function (data) {
                if (data.similar_exists) {
                    console.log("from success");
                    // {
                    //     console.log(data.status);
                    // }
                    // $("#id_variety_form").add_error('Variety_supplier_name', 'sup name error');
                    alert(data.error_message);
                }
            }
        });

    });
});