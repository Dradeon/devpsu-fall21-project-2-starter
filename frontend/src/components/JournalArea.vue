<template>
    <div>
        <v-layout justify-center justify-content-center mt-4 column>
            <div>
                <v-icon v-blur @click="fetchDefaults" :class="icons[4].class">
                    {{ icons[4].icon }}
                </v-icon>
                <v-icon v-blur @click="updateContents" :class="icons[5].class">
                    {{ icons[5].icon }}
                </v-icon>
            </div>
            <textarea v-model = "journal_content"/>
        </v-layout>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'JournalArea',
        data() {
            return {
                journal_content: "",
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
            this.updateContents();
            next();
        },

        methods:{
            fetchDefaults : function(){
                const path = 'http://localhost:5000/journal'
                axios.get(path)
                .then((res) => {
                    console.log(res.data.journal_content)
                    this.journal_content = res.data.journal_content;
                })
                .catch((error) => {
                    console.error(error);
                });
            },
            updateContents : function(){
                const path = 'http://localhost:5000/journal'
                console.log(this.journal_content)
                axios.post(path, [this.journal_content])
                .then(() => {
                    this.fetchDefaults();
                })
                .catch((error) => {
                    console.log(error);
                });
            }
        }
    }
</script>

<style scoped>
    textarea{
        padding: 5px;
        border: 2px solid darkgrey;
        height: 400px;
        max-height: 500px;
    }
</style>