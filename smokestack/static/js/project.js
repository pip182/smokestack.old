/* Project specific Javascript goes here. */
Vue.options.delimiters = ['[[', ']]'];
// Vue.config.devtools = true;


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
