<template>
    <li class="list-group-item" :class="{active: isActive}" @mouseover="toggleActive" @mouseleave="toggleActive" @click="getWord(text)">{{text}}</li>
</template>

<script>
    export default {
        name: "ListItem",
        props: ['text', 'getWord'],
        data () {
            return{
                isActive: false
            }
        },
        methods: {
            toggleActive () {
                this.isActive = !this.isActive
            }
        }
    }
</script>

<style scoped>

</style>
