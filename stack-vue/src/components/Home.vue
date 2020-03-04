<template>
    <div>
        <h1>Test Login</h1>
        <button @click="goLogin">Login</button>
    </div>
</template>

<script>
    export default {
        name: 'Home',
        methods: {
            goLogin(){
                this.$router.push({name: 'login'})
            }
        }  
    }
</script>