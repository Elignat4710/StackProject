<template>
    <mu-container>
        <mu-row>
            <home></home>
        </mu-row>
            <mu-container>
            <mu-form ref="form" :model="validateForm" class="mu-demo-form">
                <mu-form-item label='Login'>
                    <mu-text-field v-model='validateForm.login'></mu-text-field>
                </mu-form-item>
                <mu-form-item label='Password'>
                    <mu-text-field type='password' v-model="validateForm.password"></mu-text-field>
                </mu-form-item>
                <mu-form-item>
                    <mu-button @click="setLogin" color='primary'>Log in</mu-button>
                </mu-form-item>
            </mu-form>
            </mu-container>
    </mu-container>
</template>

<script>

    import $ from 'jquery'
    import Home from '@/components/Home'

    export default {
        name: 'Login',
        components:{
            Home
        },
        data(){
            return{
                validateForm:{
                    login: '',
                    password: ''
                }
                
            }
        },
        methods: {
            setLogin(){
                $.ajax({
                    url: 'http://127.0.0.1:8000/auth/token/login',
                    type: "POST",
                    data: {
                        username: this.validateForm.login,
                        password: this.validateForm.password
                    },
                    success: (response) =>{
                        sessionStorage.setItem('auth_token', response.auth_token)
                        this.$router.push({name: 'home'})
                    }
                })
            }
        }   
    }
</script>

<style scoped>
</style>