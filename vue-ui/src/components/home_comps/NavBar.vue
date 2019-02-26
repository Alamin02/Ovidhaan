<template>
    <div>
        <b-navbar toggleable="lg" type="dark" variant="info">
            <div class="container">
                <b-navbar-brand href="/"><v-icon name="book-reader" /> Dictionary!</b-navbar-brand>

                <b-navbar-toggle target="nav_collapse" />

                <b-collapse is-nav id="nav_collapse">
                    <b-navbar-nav>
                        <b-nav-item @click.prevent="goTo('/')">Home</b-nav-item>
                        <b-nav-item @click.prevent="goTo('/about')">About</b-nav-item>
                    </b-navbar-nav>

                    <!-- Right aligned nav items -->

                    <b-navbar-nav class="ml-auto">

                        <b-nav-item-dropdown id="lang-drop-down" text="Lang" right>
                            <b-dropdown-item href="#">EN</b-dropdown-item>
                        </b-nav-item-dropdown>

                    </b-navbar-nav>
                </b-collapse>
            </div>
        </b-navbar>
    </div>
</template>

<script>
    export default {
        name: "NavBar",
        methods: {
            goTo(url) {
                this.$router.push(url)
            }
        }
    }
</script>

<style scoped>
    .navbar-brand {
        padding-left: 2rem;
    }
    #lang-drop-down {
        padding-right: 2rem;
    }
</style>
