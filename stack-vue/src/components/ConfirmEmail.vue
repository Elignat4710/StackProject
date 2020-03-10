<template>
    
</template>

<script>
    export default {
        name: 'ConfirmEmail',
        created(){
            this.redirect()
        },
        methods:{
            redirect(){
                alert('Confirm email success!')
                window.location = '/'
            }
        }
    }
</script>