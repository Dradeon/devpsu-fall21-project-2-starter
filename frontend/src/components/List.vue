<template>
  <main role="main" class="inner cover">
    <v-icon v-blur @click="fetchDefaults" :class="icons[4].class">
      {{ icons[4].icon }}
    </v-icon>
    <v-icon v-blur @click="updateList" :class="icons[5].class">
      {{ icons[5].icon }}
    </v-icon>
    <v-layout justify-center justify-content-center mt-4>
      <v-simple-table fixed-header>
          <thead>
            <th></th>
            <th>Name</th>
            <th>Description</th>
            <th>Deadline</th>
            <th style="display: none;">Completed?</th>
            <th></th>
          </thead>
          <tbody v-cloak>
            <tr v-for="(item, index) in to_do_list"
                :key="index"
            >
              <td>
                <v-icon v-blur
                        :class="icons_list[index].class"
                        @click="checkRow(index)"
                        v-model="icons_list[index]"
                >
                  {{ icons_list[index].icon }}
                </v-icon>
              </td>
              <td>
                <input class="on-fly-input"
                       v-model="to_do_list[index].name"
                       :style="icons_list[index].style"
                />
              </td>
              <td>
                <input class="on-fly-input"
                       v-model="to_do_list[index].description"
                       :style="icons_list[index].style"
                />
              </td>
              <td>
                <input class="on-fly-input"
                       v-model="to_do_list[index].deadline"
                       :style="icons_list[index].style"
                />
              </td>
              <td style="display: none;">
                <input class="on-fly-input"
                       v-model="to_do_list[index].completed"
                       :style="icons_list[index].style"
                />
              </td>
              <td>
                <v-icon v-blur
                        @click="removeRow(index)"
                >
                  {{ icons[2].icon }}
                </v-icon>
              </td>
            </tr>
            <tr class="no-highlight">
              <td>
                <v-icon v-blur
                        @click="addRow"
                        :class="icons[3].class"
                >
                  {{ icons[3].icon }}
                </v-icon>
              </td>
            </tr>
          </tbody>
      </v-simple-table>
    </v-layout>
  </main>
</template>

<script>
  import axios from 'axios';
  
  export default {
    name: 'List',
    data() {
      return {
        to_do_list: [],
        icons: [
          {
            'icon': 'mdi-checkbox-blank-outline',
            'class': '',
            'style': 'text-decoration:none;color:unset;'
          },
          {
            'icon': 'mdi-checkbox-marked-outline',
            'class': 'v-icon-highlighted',
            'style': 'text-decoration:line-through;color:#adb7bbd1;'
          },
          {
            'icon': 'mdi-close',
            'class': '',
            'style': ''
          },
          {
            'icon': 'mdi-plus',
            'class': 'v-icon-highlighted',
            'style': ''
          },
          {
            'icon': 'mdi-refresh',
            'class': 'v-icon-highlighted pl-1 pb-1',
            'style': ''
          },
          {
            'icon': 'mdi-content-save',
            'class': 'v-icon-highlighted pl-1 pb-1',
            'style': ''
          }
        ],
        icons_list: []
      }
    },

    created: function () {
      this.fetchDefaults();
    },

    beforeRouteLeave: function (to, from, next) {
      this.updateList();
      next();
    },

    methods: {
      fetchDefaults: function () {
        const path = 'http://localhost:5000/todolist';
        axios.get(path)
          .then((res) => {
            this.to_do_list = res.data.to_do_list;
            this.icons_list = [];
            for (var i = 0; i < this.to_do_list.length; i++) {
              if (this.to_do_list[i].completed == false) {
                this.icons_list.push(this.icons[0]);
              } else {
                this.icons_list.push(this.icons[1]);
              }
            }
          })
          .catch((error) => {
            console.error(error);
          });
      },

      updateList: function () {
        const path = 'http://localhost:5000/todolist';
        axios.post(path, this.to_do_list)
          .then(() => {
            this.fetchDefaults();
          })
          .catch((error) => {
            console.log(error);
          });
      },

      removeRow: function (index) {
        this.to_do_list.splice(index, 1);
        this.icons_list.splice(index, 1);
      },

      addRow: function () {
        this.to_do_list.push({
          name: '',
          description:'',
          deadline: '',
          completed: false,
        });
        this.icons_list.push(this.icons[0]);
      },

      checkRow: function (index) {
          if (this.icons_list[index].icon == this.icons[0].icon) {
              this.icons_list[index] = this.icons[1];
              this.to_do_list[index].completed = true;
          } else {
              this.icons_list[index] = this.icons[0];
              this.to_do_list[index].completed = false;
          }
      },

      directives: {
        focus: {
          inserted (el) {
            el.focus();
          }
        }
      }

    }
  };
</script>