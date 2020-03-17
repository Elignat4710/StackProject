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
                <mu-form-item>
                    <Google></Google>
                </mu-form-item>
            </mu-form>
            </mu-container>
    </mu-container>
</template>

<script>

    import $ from 'jquery'
    import Home from '@/components/Home'
    import Google from '@/components/Google'

    export default {
        name: 'Login',
        components:{
            Home,
            Google
        },
        data(){
            return{
                validateForm:{
                    login: '',
                    password: ''
                },
                googleSignInParams: {
                    client_id: '559920722496-ic02pjffmjq267e84pggsjhtb0vhq6ls.apps.googleusercontent.com'
                }
                
            }
        },
        methods: {
            setLogin(){
                $.ajax({
                    url: 'http://127.0.0.1:8000/rest-auth/login/',
                    type: "POST",
                    data: {
                        username: this.validateForm.login,
                        password: this.validateForm.password
                    },
                    success: (response) =>{
                        console.log(response)
                        sessionStorage.setItem('token', response.token)
                        this.$router.push({name: 'home'})
                    }
                })
            },
        }   
    }
</script>

<style scoped>
</style>