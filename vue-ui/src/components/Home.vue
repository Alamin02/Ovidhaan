<template>
    <div>
        <div class="container">
            <b-jumbotron header="Bangla Dictionary" lead="A dictionary made out of scraped web data">
                <div id="input-field">
                    <p class="lead input-caption">Find Bengali meaning by typing the word</p>

                    <div class="input-group">
                        <input type="text" placeholder="Type in here to search!" aria-label="User Input"
                               aria-describedby="search-area" class="form-control"  v-model="search" @keydown.enter="getWord(search)">
                        <div class="input-group-append">
                            <button type="button" id="search-btn" class="btn btn-outline-secondary" @click="getWord(search)">Go! <b-spinner type="grow" small label="Loading..." /></button>
                        </div>
                    </div>
                    <ul v-if="suggestions" class="list-group" style="position: absolute; width: 100%">
                        <ListItem v-for="suggestion in suggestions" :getWord="getWord" :key="suggestion" :text="suggestion"></ListItem>
                    </ul>
                </div>
            </b-jumbotron>

        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import ListItem from './home_comps/ListItem'

    export default {
        name: "Home",
        components: {
            ListItem
        },
        data() {
            return {
                search: '',
                suggestions: [],
                selection: {
                    word: '',
                    meaning: ''
                }
            }
        },
        watch: {
            search: function () {
                this.getSearchResult()
            }
        },
        methods: {
            getSearchResult() {
                axios
                    .get('http://localhost:5000/api/search?word=' + this.search)
                    .then(response => (this.suggestions = response.data.words))
            },
            getWord(word) {
                this.$router.push('/details/'+ word)
            }
        }
    }
</script>

<style scoped>
#input-field {
    position: relative;
    margin-top: 3.5rem;
    margin-bottom: 2.5rem;
}
.input-caption {
    font-size: 1.25rem;
}
</style>
