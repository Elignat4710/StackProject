<template>
    <div>
        <input placeholder="Login" v-model="login">
        <input placeholder="Password" type="password" v-model="password">
        <button @click="setLogin">Login</button>
    </div>
</template>

<script>

    import $ from 'jquery'

    export default {
        name: 'Login',
        data(){
            return{
                login: '',
                password: ''
            }
        },
        methods: {
            setLogin(){
                $.ajax({
                    url: 'http://127.0.0.1:8000/auth/token/login',
                    type: "POST",
                    data: {
                        username: this.login,
                        password: this.password
                    },
                    success: (response) =>{
                        sessionStorage.setItem('auth_token', response.auth_token)
                    }
                })
            }
        }   
    }
</script>