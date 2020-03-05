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
                <mu-text-field type='password' v-model="validateForm.password"></mu-text-field>
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
                    password: ''
                }
                
            }
        },
        methods:{
            regUser(){
                $.ajax({
                    url: 'http://127.0.0.1:8000/register/',
                    type: 'POST',
                    data:{
                        username: this.validateForm.login,
                        email: this.validateForm.email,
                        password: this.validateForm.password
                    },
                    success: (response) => {
                        alert('Success!')
                        window.location = '/'
                    },
                    error: (response) => {
                        console.log(response)
                    }
                })
                 
            }
        } 
    }
</script>