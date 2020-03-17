<template>
    <g-signin-button
            :params="googleSignInParams"
            @success="onGoogleSignInSuccess"
            >
            <mu-button class="btn btn-block btn-success">
              Google
            </mu-button>
          </g-signin-button>
</template>

<script>

    import $ from 'jquery'


    export default {
        name: 'Google',
        data(){
            return{
                googleSignInParams: {
                    client_id: '559920722496-ic02pjffmjq267e84pggsjhtb0vhq6ls.apps.googleusercontent.com'
                }
            }
        },
        methods:{
            onGoogleSignInSuccess(resp){
                console.log(resp)
                const token = resp.uc.access_token
                console.log(token)
                
                $.ajax({
                    url: 'http://127.0.0.1:8000/user/auth/google/',
                    type: 'POST',
                    data: {
                        access_token: token
                    },
                    success: (response) => {
                        console.log(response)
                        sessionStorage.setItem('token', response.token)
                        alert('auth success!')
                        this.$router.push({name: 'home'})
                    },
                    error: (response) => {
                        console.log(response)
                    }
                    
                })
            },
        }
    }
</script>