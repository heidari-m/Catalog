  Dropzone.autoDiscover = false;
  $(document).ready(() => {
    $('[id^="custom-dropzone-widget"]').each((index, element) => {
      options = JSON.parse($(element).text())
        className = 'div.' + options.class
      console.log(options)
      new Dropzone(className, options)
    })
  })