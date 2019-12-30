
var inventoryApp = new Vue({
  el: '#inventory-app',
  data: {
    items: [],
    vendors: [],
    categories: [],
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
      { key: 'price', label: 'Price', sortable: true },
      { key: 'category_name', label: 'Category', sortable: true },
      { key: 'vendor_name', label: 'Vendor', sortable: true },
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
    itemEditModal: {
      id: 'info-modal',
      item_id: 0,
      item: {},
      title: '',
      content: ''
    },
    item: [],
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
  mounted: function () {
    // Set the initial number of items
    this.totalRows = this.items.length;
  },
  created: function() {

  },
  computed: {
    // Data to use as the vendor options in a select widgety thingy
    vendor_options: function () {
      let options = [];
      _.forEach(this.vendors, function(v) {
        options.push({value: v.id, text: v.name})
      });
      return options;
    },
    // Data to use as the category options in a select widgety thingy
    category_options: function () {
      let options = [];
      _.forEach(this.categories, function(c) {
        options.push({value: c.id, text: c.name})
      });
      return options;
    },
  },
  methods: {
    rowHovered(item, index, button) {
      // console.log("DIOGS");
      // console.log(item, index, button);

    },
    // Gets mods available for the current item and puts them into categories.
    load: function() {
      let vue = this;
      let ajax_items = $.get('/inventory/api/items').done(function(data) {
        vue.items = data;
      });
      let ajax_categories = $.get('/inventory/api/categories').done(function(data) {
        vue.categories = data;
      });
      let ajax_vendors = $.get('/inventory/api/vendors').done(function(data) {
        vue.vendors = data;
      });

      $.when(ajax_items, ajax_categories, ajax_vendors).done(function() {
        vue.loaded = true;
      })
    },
    fieldType(val) {
      if (isNaN(val)) {
        return "text";
      } else {
        return "number";
      }
    },
    itemUpdate(bvm) {
      this.item.notes = $("#id_notes").summernote('code');
      let send_data = $.ajax({
          url: "/inventory/api/items/" + this.item.id + "/",
          method: 'put',
          data: this.item})
        .done(function (data) {
          console.log(data);
        });
    },

    info: function(item, index, button) {
      vue = this;
      vue.itemEditModal.item = _.find(vue.items, {id: item.id});
      vue.itemEditModal.title = 'Edit Item: ' + vue.itemEditModal.item.name;
      vue.itemEditModal.item_id = item.id;
      vue.itemEditModal.content = JSON.stringify(item, null, 2);
      vue.$root.$emit('bv::show::modal', vue.itemEditModal.id, button);
      vue.item = vue.itemEditModal.item;

      // Initialize summernote editor. Have to do it here because everywhere else fails.
      // $("#id_notes").summernote('destroy');
      $("#id_notes").summernote({
        toolbar: summernote_toolbar,
        height: 150});
      $("#id_notes").summernote("code", vue.item.notes);

    },
    resetitemEditModal: function() {
      this.itemEditModal.title = '';
      this.itemEditModal.content = '';
    },
    onFiltered: function(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    }
  }
});


$(document).ready(function () {
  inventoryApp.load();
});
