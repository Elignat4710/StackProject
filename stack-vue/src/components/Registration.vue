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
        </mu-form>
    </mu-container>
</template>

<script>

    import Home from '@/components/Home'
    import $ from 'jquery'

    export default {
        name: 'Registration',
        components:{
            Home
        },
        data(){
            return{
                validateForm:{
                    login: '',
                    email: '',
                    password1: '',
                    password2: ''
                }
                
            }
        },
        methods:{
            regUser(){
                $.ajax({
                    url: 'http://3.19.77.231:8000/rest-auth/registration/',
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
                        console.log(response.responseText)
                    }
                })
                 
            }
        } 
    }
</script>