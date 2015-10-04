/* Javascript for polyxXBlock. */
function polyxXBlockInitStudio(runtime, element) {

    $(element).find('.action-cancel').bind('click', function() {
        runtime.notify('cancel', {});
    });

    $(element).find('.save-button').bind('click', function() {
    var handlerUrl = runtime.handlerUrl(element, 'studio_submit');
    var data = {
        display_name: $(element).find('input[name=display_name]').val(),
        video_id: $(element).find('input[name=video_id]').val(),
        width: $(element).find('input[name=width]').val(),
        height: $(element).find('input[name=height]').val()
    };
    $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
      window.location.reload(false);
    });

}
