/* Project specific Javascript goes here. */
Vue.options.delimiters = ['[[', ']]'];



$(document).ready(function () {

  $('#sidebarCollapse').on('click', function () {
      $('#sidebar').toggleClass('condensed');
  });

});
