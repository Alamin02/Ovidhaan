<template>
    <div class="container">
        <b-jumbotron header="Bangla Dictionary" lead="A dictionary made out of scraped web data">
            <hr>
            <p class="details">Data is scraped using Scrapy from <a href="http://www.english-bangla.com/" target="_blank">here.</a> </p>
            <p class="details">Collected data is saved to a sqlite database.</p>
            <p class="details">A Flask Restful Api is employed to handle request for dictionary data.</p>
            <p class="details">A single page application with Vue is serving as web front-end</p>
            <hr>
            <p class="lead">Developed by: Md. Al Amin</p>
        </b-jumbotron>
    </div>
</template>

<script>
    export default {
        name: "About"
    }
</script>

<style scoped>
.details {
    line-height: 1;
}
</style>
