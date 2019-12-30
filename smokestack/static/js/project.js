/* Project specific Javascript goes here. */
Vue.options.delimiters = ['[[', ']]'];
// Vue.config.devtools = true;


// What buttons should show on the summernote text editor, for the admin page you need to
// edit the summernote configuration in settings/base.py
const summernote_toolbar = [
  ['style', ['style']],
  ['font', ['bold', 'underline', 'clear', 'fontsize']],
  ['fontname', ['fontname']],
  ['color', ['color']],
  ['para', ['ul', 'ol', 'paragraph']],
  ['table', ['table']],
  ['insert', ['link', 'picture']],
  ['view', ['fullscreen', 'codeview']],
];

// Javascript implementation of String.format.
// From https://stackoverflow.com/questions/1038746/equivalent-of-string-format-in-jquery/41052964#41052964
// First, checks if it isn't implemented yet
// Can be used with "".format() or short "".f()
if (!String.prototype.format) {
  String.prototype.format = String.prototype.f = function() {
    var args = arguments;
    return this.replace(/{(\d+)}/g, function (match, number) {
      return typeof args[number] != 'undefined' ? args[number] : match;
    });
  };
}


// Detects the worlds worst browser that people still use for some reason.
function detectIE() {
  var ua = window.navigator.userAgent;
  if (ua.indexOf('MSIE ') > 0 || ua.indexOf('Trident/') > 0) {
    return true;
  }
  return false;
}


$(document).ready(function () {

  // Makes site unusable with IE since it will only cause problems.
  if (detectIE()) {
    document.getElementById('page-container').innerHTML =
      '<div class="row justify-content-center mt-5"><div class="mt-5 col"><center>' +
      '<h2>This app will not work in IE 11 or older browsers!</h2><br>' +
      '<strong>Try one of the modern browsers below and repent for your sins.</strong><br><br>' +
      '<a class="btn btn-link" href="https://www.mozilla.org/en-US/firefox/">Firefox</a>' +
      '<a class="btn btn-link" href="https://www.google.com/chrome/">Chrome</a>' +
      '<a class="btn btn-link" href="https://www.opera.com/">Opera</a>' +
      '<a class="btn btn-link" href="https://www.microsoft.com/en-gb/windows/microsoft-edge">Edge</a>' +
      '<a class="btn btn-link" href="https://vivaldi.com/">Vivaldi</a>' +
      '</center></div></div>';
  }


});
