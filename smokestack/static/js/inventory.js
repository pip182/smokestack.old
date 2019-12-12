/* Project specific Javascript goes here. */


var app = new Vue({
  el: '#test-app',
  data: {
    name: 'BootstrapVue',
    show: true
  },
  watch: {
    show(newVal) {
      console.log('Alert is now ' + (newVal ? 'visible' : 'hidden'))
    }
  },
  methods: {
    toggle() {
      console.log('Toggle button clicked')
      this.show = !this.show
    },
    dismissed() {
      console.log('Alert dismissed')
    }
  }
});
