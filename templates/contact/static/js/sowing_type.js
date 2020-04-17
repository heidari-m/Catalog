$(document).ready(function () {
    $('#id_sow_type').change(function (e) {
        var tmp = $(this).val();
        if (tmp == 't') {
            $('#id_direct_sowing_type').parent().hide("slow");
            $('label[for="id_direct_sowing_type"]').parent().hide("slow");
            $('#id_hand_type').parent().hide("slow");
            $('label[for="id_hand_type"]').parent().hide("slow");
        } else if (tmp == 'd') {
            $('#id_direct_sowing_type').parent().show("slow");
            $('label[for="id_direct_sowing_type"]').parent().show("slow");
            $('#id_hand_type').parent().show("slow");
            $('label[for="id_hand_type"]').parent().show("slow");
        }
    });
});