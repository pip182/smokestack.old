// Vue.use(vuedraggable);

// const createSortable = (el, options, vnode) => {
//   // console.log(el, options, vnode);

//   return Sortable.create(el, {...options,
//     onChange(evt) {
//       // let items = inventoryApp.items;
//       // let high = _.nth(items, evt.oldIndex + 1),
//       //     low = _.nth(items. evt.oldIndex - 1)

//       // console.log(evt.oldIndex, evt.newIndex);
//       // console.log("Old:", _.nth(inventoryApp.items, evt.oldIndex).name);
//       // console.log("New:", _.nth(inventoryApp.items, evt.newIndex).name);

//     }
//   });
// };


const sortable = {
  name: 'sortable',
  bind(el, binding, vnode) {
    const table = el;
    table._sortable = Sortable.create(table.querySelector("tbody"), binding.value, vnode);
  }
};

// Custom date validator (Not actually used right now just an example of how to get one mostly working)
VeeValidate.extend('date', {
  validate(value, args) {
    var date = dayjs(value);
    var min = args.min ? dayjs(args.min) : dayjs();
    var max = args.max ? dayjs(args.max) : dayjs().add(5, 'year');

    if (date >= min && date <= max) {
      return true;
    }
    return 'The {_field_} field must be between ' + min.format('MM/DD/YYYY') + ' and ' + max.format('MM/DD/YYYY');
  },
  params: ['min', 'max']
});


var inventoryApp = new Vue({
  el: '#inventory-app',
  data: {
    items: [],
    vendors: [],
    categories: [],
    fields: [
      {key: 'position', label: "#", sortable: true},
      {key: 'name', label: 'Item Name', sortable: true, sortDirection: 'desc'},
      {key: 'current_quantity', label: 'Quantity', sortable: true, class: 'text-center'},
      {key: 'active', label: 'is Active', sortable: true, sortByFormatted: true, filterByFormatted: true},
      {key: 'price', label: 'Price', sortable: true},
      {key: 'category_name', label: 'Category', sortable: true},
      {key: 'vendor_name', label: 'Vendor', sortable: true},
      {key: 'actions', label: 'Actions'}
    ],
    totalRows: 1,
    sortBy: 'position',
    sortDesc: false,
    sortDirection: 'asc',
    filter: '',
    filterOn: ['active'],
    loaded: false,
    itemEditModal: {
      id: 'edit-modal', method: "", url: "",
      item_id: 0, item: {}, title: '', content: ''
    },
    transProps: {
      // Transition name
      name: 'item'
    },
    // The current item being edited.
    item: {
      id: 0, name: '', code: '', notes: ''
    },
    hovered_row: -1,
  },
  directives: { sortable },
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
    max_position: function() {
      return _.maxBy(this.items, function(i) {
        return i.position;
      }).position;
    },
    min_position: function () {
      return _.minBy(this.items, function(i) {
        return i.position;
      }).position;
    }
  },
  methods: {
    onUpdate(event) {
      console.log(event);
      if (event.newIndex < event.oldIndex) {
        let shifted = _.nth(this.items, event.oldIndex);
        shifted.position--;
        console.log(shifted.name, event.oldIndex, shifted.position);

      } else if (event.newIndex > event.oldIndex) {

      }
      console.log(_.nth(this.items, event.oldIndex).position);
    },
    rowHovered(item, index, event) {
      this.hovered_item = item;
      // console.log("Hovered:", this.hovered_item);
    },
    rowUnHovered(item, index, event) {
      this.hovered_item = null;
      // console.log("Leave:", this.hovered_item);
    },
    // Gets mods available for the current item and puts them into categories.
    load: function() {
      var vue = this,
      ajax_items = $.get('/inventory/api/items/').done(function(data) {
        vue.items = data;
      }),
      ajax_categories = $.get('/inventory/api/categories').done(function(data) {
        vue.categories = data;
      }),
      ajax_vendors = $.get('/inventory/api/vendors').done(function(data) {
        vue.vendors = data;
      });

      $.when(ajax_items, ajax_categories, ajax_vendors).done(function() {
        vue.loaded = true;
      })
    },
    onSubmit(bvm) {
      bvm.preventDefault();
      let vue = this;
      vue.$refs.item_edit_form.validate().then(function(success) {
        if (!success) {
          toastr.error("There are some errors in the form that need to be corrected!")
        } else {
          vue.item.notes = $("#id_notes").summernote('code');
          let send_data = $.ajax({
              url: vue.itemEditModal.url,
              method: vue.itemEditModal.method,
              data: vue.item})
            .done(function (data) {
              if (!data.success) {
                toastr.error("Holy shit, something is not working at the python level!")
              }
              console.log("returned Data: ", data);
              if (data.type == 'new') {
                vue.items.push(data.item);
                toastr.success("Successfully added new item: {0}".format(data.item.name));
              }
              vue.$bvModal.hide(vue.itemEditModal.id);
            });
        }
      });
    },
    initSummernote(item) {
      // Initialize summernote editor. Have to do it here because everywhere else fails.
      $("#id_notes").summernote({
        toolbar: summernote_toolbar,
        height: 150});
      $("#id_notes").summernote("code", item.notes || "");
    },
    updateItems(items) {
      let vue = this;
      console.log(vue.items);

      // Takes a list of item objects and updates them one at a time
      // TODO: Bulk update rather than one at a time.
      // $.ajax({
      //   url: "/inventory/api/items/",
      //   method: 'post',
      //   data: vue.items})
      // .done(function (data) {});
      _.forEach(items, function(i) {
        $.ajax({
          url: "/inventory/api/items/" + i.id + "/",
          method: 'put',
          data: i})
        .done(function (data) {});
      });
    },
    info: function(item, index, button) {
      let vue = this;
      vue.isBusy = true;
      vue.itemEditModal.item = _.find(vue.items, {id: item.id});
      vue.itemEditModal.title = 'Edit Item: ' + vue.itemEditModal.item.name;
      vue.itemEditModal.item_id = item.id;
      vue.itemEditModal.method = "put";
      vue.itemEditModal.url = "/inventory/api/items/" + item.id + "/"
      vue.itemEditModal.content = JSON.stringify(item, null, 2);
      vue.itemEditModal.buttonText = "Update";
      vue.$root.$emit('bv::show::modal', vue.itemEditModal.id, button);
      vue.item = vue.itemEditModal.item;

      vue.initSummernote(vue.item);
      vue.isBusy = false;
    },
    newItem: function(bvm) {
      let vue = this;
      vue.itemEditModal.method = "post";
      vue.itemEditModal.url = "/inventory/api/items/";
      // if (vue.item) {
        vue.itemEditModal.item = Object.assign({}, this.item);
      // }
      vue.itemEditModal.title = 'Create New Item';
      vue.item = vue.itemEditModal.item;
      vue.itemEditModal.buttonText = "Add New";
      vue.$root.$emit('bv::show::modal', vue.itemEditModal.id);

      vue.initSummernote(vue.item);
    },
    deleteItem(button) {
      var item_id = Number(button.node.dataset.item);
      var vue = this;
      console.log("OIyhg", typeof(item_id));

      console.log("Deletebutton: ", item_id);
      vue.item = _.find(vue.items, {id: item_id});
      console.log(vue.item);

      vue.itemEditModal.method = "delete";
      vue.itemEditModal.url = "/inventory/api/items/{0}/".format(item_id);
      let send_data = $.ajax({
        url: vue.itemEditModal.url,
        method: vue.itemEditModal.method,
        data: vue.item})
      .done(function (data) {
        if (!data.success) {
          toastr.error("Holy shit, something is not working at the python level!")
        }
        console.log("returned Data: ", data);
      });
    },
    resetitemEditModal: function() {
      this.itemEditModal.title = '';
      this.itemEditModal.content = '';
    },
    onFiltered: function(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    format_money(value, event) {
      return Number(value).toFixed(2);
    },
    format_int(value, event) {
      return Number(value).toFixed(0);
    }
  }
});


$(document).ready(function () {
  inventoryApp.load();

  // Handle some keyboard events. Such as moving a row up or down when 'Up' or 'Down' are pressed
  window.addEventListener('keydown', (e) => {
    switch (e.key) {
      case "ArrowUp":
        console.log('Up key pressed!');
        e.preventDefault();
        if (inventoryApp.hovered_item.position > inventoryApp.min_position) {
          let hovered_item = inventoryApp.hovered_item;
          let target = hovered_item.position - 1;
          let existing_item = _.find(inventoryApp.items, {position: target});
          if (existing_item === undefined) {
            while (existing_item === undefined) {
              target--;
              existing_item = _.find(inventoryApp.items, {position: target});
              if (existing_item) console.log("  ", target, existing_item.name, existing_item.position);
            }
          }
          console.log("existing_item", existing_item.name, existing_item.position, target);
          console.log("hovered_item", hovered_item.name, hovered_item.position);
          existing_item.position = hovered_item.position;
          hovered_item.position = target;
          inventoryApp.updateItems([hovered_item, existing_item]);
        }
        break;
      case "ArrowDown":
        console.log('Down key pressed!');
        e.preventDefault();
        console.log(inventoryApp.max_position);
        if (inventoryApp.hovered_item.position < inventoryApp.max_position) {
          let hovered_item = inventoryApp.hovered_item;
          let target = hovered_item.position + 1;
          let existing_item = _.find(inventoryApp.items, {position: target});
          if (existing_item === undefined) {
            while (existing_item === undefined) {
              target++;
              existing_item = _.find(inventoryApp.items, {position: target});
              if (existing_item) console.log("  ", target, existing_item.name, existing_item.position);
            }
          }
          console.log("existing_item", existing_item.name, existing_item.position, target);
          console.log("hovered_item", hovered_item.name, hovered_item.position);
          existing_item.position = hovered_item.position;
          setTimeout(function(){
            hovered_item.position = target;
            inventoryApp.updateItems([hovered_item, existing_item]);
          }, 500);
        }
        break;
      default:
        // console.log(e.key);
        break;
    }
  });
});
