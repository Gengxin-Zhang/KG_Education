<template>
    <div class="kg-container">
            <div class="content markdown">
                <h1>404 Not Found! :(</h1>
                <h3>您要找的页面不存在,要不去查一下试试？<router-link to="/search">>> GO !</router-link></h3>
            </div>
    </div>
</template>

<style lang="scss">
@import '../assets/style/views.scss';
</style>

<script>
export default {
    created() {
        document.title = "404 Not Found -- KG_Education"
    },
}
</script>
