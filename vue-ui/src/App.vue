<template>
  <div id="app">
      <NavBar />
    <router-view />
  </div>
</template>

<script>
    import NavBar from './components/home_comps/NavBar'
    export default {
      name: 'app',
        components: {
          NavBar
        }
    }
</script>

<style>
  html,
  body {
    height: 100%
  }
</style>
