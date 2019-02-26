<template>
    <div class="container">
        <b-jumbotron>
            <p id="word-display">{{word}}</p>
            <p class="bangla-meaning">{{meaning}} </p>
            <div v-if="!word" class="alert alert-danger" role="alert">
                {{message}}
            </div>
        </b-jumbotron>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "Details",
        data () {
            return {
                word: '',
                meaning: '',
                message: 'Loading..'
            }
        },
        created() {
            axios
                .get('http://localhost:5000/api/words/' + this.$route.params.word)
                .then(response => {
                    this.word = response.data.word[0];
                    this.meaning = response.data.word[1];
                    this.message= 'Oops! Word not found in the database. Sorry about that!'
                })
        }
    }
</script>

<style scoped>
    @import url('https://fonts.maateen.me/charukola-ultra-light/font.css');
    #word-display {
        font-size: 2.5rem;
        font-weight: 300;
    }
    .bangla-meaning {
        font-family: 'CharukolaUltraLight', Arial, sans-serif !important;
    }
</style>
