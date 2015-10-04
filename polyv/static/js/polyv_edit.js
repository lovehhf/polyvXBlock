/* Javascript for polyxXBlock. */
function polyxXBlockInitStudio(runtime, element) {

    $(element).find('.action-cancel').bind('click', function() {
        runtime.notify('cancel', {});
    });

    $(element).find('.action-save').bind('click', function() {
        var data = {
            'display_name': $('#polyv_edit_display_name').val(),
            'file_id': $('#polyv_edit_file_id').val(),
            'app_id': $('#polyv_edit_app_id').val(),
            'width': $('#polyv_edit_width').val(),
            'height': $('#polyv_edit_height').val(),
        };

        runtime.notify('save', {state: 'start'});

        var handlerUrl = runtime.handlerUrl(element, 'save_polyv');
        $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
            if (response.result === 'success') {
                runtime.notify('save', {state: 'end'});
                // Reload the whole page :
                // window.location.reload(false);
            } else {
                runtime.notify('error', {msg: response.message})
            }
        });
    });

}
