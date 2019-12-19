/* Project specific Javascript goes here. */


var inventoryApp = new Vue({
  el: '#inventory-app',
  data: {
    items: [],
    fields: [
      { key: 'name', label: 'Item Name', sortable: true, sortDirection: 'desc' },
      { key: 'current_quantity', label: 'Quantity', sortable: true, class: 'text-center' },
      {
        key: 'isActive',
        label: 'is Active',
        formatter: function(value, key, item) {
          return value ? 'Yes' : 'No'
        },
        sortable: true,
        sortByFormatted: true,
        filterByFormatted: true
      },
      { key: 'vendor.name', label: 'Vendor', sortable: true },
      { key: 'price', label: 'Price', sortable: true },
      { key: 'actions', label: 'Actions' }
    ],
    totalRows: 1,
    currentPage: 1,
    perPage: 25,
    pageOptions: [25, 60, 100],
    sortBy: '',
    sortDesc: false,
    sortDirection: 'asc',
    filter: null,
    filterOn: [],
    loaded: false,
    infoModal: {
      id: 'info-modal',
      title: '',
      content: ''
    }
  },
  computed: {
    sortOptions: function() {
      // Create an options list from our fields
      // return this.fields
      //   .filter(f => f.sortable)
      //   .map(f => {
      //     return { text: f.label, value: f.key }
      //   })
    }
  },
  mounted: function() {
    // Set the initial number of items
    this.totalRows = this.items.length
  },
  methods: {
    rowHovered(item, index, button) {
      console.log("DIOGS");
      console.log(item, index, button);

    },
    // Gets mods available for the current item and puts them into categories.
    load: function() {
      var vue = this;
      return $.get('/inventory/api/items').done(function(data) {
        console.log(data);

        vue.items = data;
      });
    },
    info: function(item, index, button) {
      this.infoModal.title = 'Row index: ' + index;
      this.infoModal.content = JSON.stringify(item, null, 2)
      this.$root.$emit('bv::show::modal', this.infoModal.id, button)
    },
    resetInfoModal: function() {
      this.infoModal.title = ''
      this.infoModal.content = ''
    },
    onFiltered: function(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length
      this.currentPage = 1
    }
  }
});


$(document).ready(function () {
  inventoryApp.load();
});
