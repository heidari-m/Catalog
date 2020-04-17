$(document).ready(function () {
    function showEditPopup(url) {
        console.log("from edit");
        var win = window.open(url, "Edit",
            'height=500,width=800,resizable=yes,scrollbars=yes');
        return false;
    };

    function showAddPopup(triggeringLink) {
        var name = triggeringLink.id.replace(/^instance_/, '');
        console.log(name);
        {
            // var
            n2 = triggeringLink.id.replace(/^type/, 'create');
            //
        }
        href = triggeringLink.href;
        var win = window.open(href, name, 'height=500,width=500,resizable=yes,scrollbars=yes');

        win.focus();
        return false;
    };

    function closePopup(win, newID, newRepr, id) {
        alert("form close");
        console.log(id);
        console.log(win);
        console.log(newID);
        console.log(newRepr);
        $(id).append('<option value=' + newID + ' selected >' + newRepr + '</option>');

        win.close();
    };
});