$(document).ready(function () {
    $('#id_sow_type').change(function (e) {
        var tmp = $(this).val();
        if (tmp == 't') {
            $('#id_direct_sowing_type').parent().hide("slow");
            $('label[for="id_direct_sowing_type"]').parent().hide("slow");
            $('#id_hand_type').parent().hide("slow");
            $('label[for="id_hand_type"]').parent().hide("slow");
            $('#id_sow_KG_HA_direct_min_interval').parent().hide("slow");
            $('#id_sow_KG_HA_direct_max_interval').parent().hide("slow");
            $('#id_sow_KG_HA_transplant_min_interval').parent().show("slow");
            $('#id_sow_KG_HA_transplant_max_interval').parent().show("slow");
        } else if (tmp == 'd') {
            $('#id_direct_sowing_type').parent().show("slow");
            $('label[for="id_direct_sowing_type"]').parent().show("slow");
            $('#id_hand_type').parent().show("slow");
            $('label[for="id_hand_type"]').parent().show("slow");
            $('#id_sow_KG_HA_direct_min_interval').parent().show("slow");
            $('#id_sow_KG_HA_direct_max_interval').parent().show("slow");
            $('#id_sow_KG_HA_transplant_min_interval').parent().hide("slow");
            $('#id_sow_KG_HA_transplant_max_interval').parent().hide("slow");
        } else if (tmp == 'b') {
            $('#id_direct_sowing_type').parent().show("slow");
            $('label[for="id_direct_sowing_type"]').parent().show("slow");
            $('#id_hand_type').parent().show("slow");
            $('label[for="id_hand_type"]').parent().show("slow");
            $('#id_sow_KG_HA_direct_min_interval').parent().show("slow");
            $('#id_sow_KG_HA_direct_max_interval').parent().show("slow");
            $('#id_sow_KG_HA_transplant_min_interval').parent().show("slow");
            $('#id_sow_KG_HA_transplant_max_interval').parent().show("slow");

        }
    });

    $('#id_direct_sowing_type').change(function (e) {
        var tmp = $(this).val();
        if (tmp == 'm') {
            $('#id_hand_type').parent().hide('slow');
            $('label[for="id_hand_type"]').parent().hide('slow');


        } else if (tmp == 'h') {
            $('#id_hand_type').parent().show('slow');
            $('label[for="id_hand_type"]').parent().show('slow');
        }
    });

});