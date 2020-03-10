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
        <mu-row>
            <g-signin-button
            :params="googleSignInParams"
            @success="onGoogleSignInSuccess"
            >
            <button class="btn btn-block btn-success">
              Google Signin
            </button>
          </g-signin-button>
        </mu-row>
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
            onGoogleSignInSuccess(resp){
                console.log(resp)
                const token = resp.uc.access_token
                console.log(token)
                
                $.ajax({
                    url: 'http://localhost:8000/user/auth/google/',
                    type: 'POST',
                    data: {
                        access_token: token
                    },
                    success: (response) => {
                        sessionStorage.setItem('token', response.token)
                        this.$router.push({name: 'home'})
                    },
                    error: (response) => {
                        console.log(response)
                    }
                    
                })
            }
        }   
    }
</script>

<style scoped>
</style>