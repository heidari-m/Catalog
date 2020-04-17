$(document).ready(function () {
    $('#category1').hide();
    $('#group').change(function (e) {
        var group = $(this).val();
        if (group == 'Premium') {
            $('#category1').show();
        } else {
            $('#category1').hide();
        }
    });
});
