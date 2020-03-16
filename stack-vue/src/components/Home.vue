<template>

    <mu-container>
            <mu-appbar style="width: 100%;" color="primary">
                StackProject
                <mu-button v-if="!auth" @click="goLogin" flat slot="right">Login</mu-button>
                <mu-button v-if="!auth" @click="goReg" flat slot="right">Sign-up</mu-button>
                <mu-button v-else @click="logout" flat slot="right">Log out</mu-button>
            </mu-appbar>
    </mu-container>
        
</template>

<script>

    import $ from 'jquery'

    export default {
        name: 'Home',
        computed: {
            auth() {
                if(sessionStorage.getItem('token')){
                    return true
                }
            }
        },
        methods: {
            goLogin(){
                this.$router.push({name: 'login'})
            },
            goReg(){
                this.$router.push({name: 'registration'})
            },
            logout(){
                $.ajax({
                    url: 'http://3.19.77.231:8000/rest-auth/logout/',
                    type: "GET",
                    success: (response) =>{
                        sessionStorage.removeItem('token')
                        window.location = '/'
                    }
                })
            }
        },
        
    }
</script>