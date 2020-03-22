<template>
    <mu-container>
        <mu-container>
            <home></home>
        </mu-container>
        <mu-form ref="form" :model="validateForm" class="mu-demo-form">
            <mu-form-item label='Display name'>
                <mu-text-field v-model="validateForm.login"></mu-text-field>
            </mu-form-item>
            <mu-form-item label='Email'>
                <mu-text-field type='email' v-model="validateForm.email"></mu-text-field>
            </mu-form-item>
            <mu-form-item label='Password'>
                <mu-text-field type='password' v-model="validateForm.password1"></mu-text-field>
            </mu-form-item>
             <mu-form-item label='Confirm password'>
                <mu-text-field type='password' v-model="validateForm.password2"></mu-text-field>
            </mu-form-item>
            <mu-form-item>
                <mu-button @click="regUser" color='primary'>Sign in</mu-button>
            </mu-form-item>
            <mu-form-item>
                <Google></Google>
            </mu-form-item>
            <mu-form-item>
                <mu-button
                :params='LinkedInParam'
                @click="LinkedInSignIn"
                color='primary'
                >
                LinkedIn
                </mu-button>
            </mu-form-item>
        </mu-form>
    </mu-container>
</template>

<script>

    import Home from '@/components/Home'
    import $ from 'jquery'
    import Google from '@/components/Google'

    export default {
        name: 'Registration',
        components:{
            Home,
            Google
        },
        data(){
            return{
                validateForm:{
                    login: '',
                    email: '',
                    password1: '',
                    password2: ''
                },
                LinkedInParam:{
                    client_id: '86x3tsdy42o73h'
                }
                
            }
        },
        methods:{
            regUser(){
                $.ajax({
                    url: 'http://127.0.0.1:8000/rest-auth/registration/',
                    type: 'POST',
                    data:{
                        username: this.validateForm.login,
                        email: this.validateForm.email,
                        password1: this.validateForm.password1,
                        password2: this.validateForm.password2
                    },
                    success: (response) => {
                        alert('Success!')
                        window.location = '/'
                    },
                    error: (response) => {
                        
                    }
                })
                 
            },
            LinkedInSignIn(resp){
                $.ajax({
                    url: 'http://localhost:8000/user/linkedin/login/',
                    type: 'GET',
                    success: (response) => {
                        console.log(response)
                    },
                    error: (response) => {
                        
                    }
                })
            }
        } 
    }
</script>