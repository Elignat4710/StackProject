webpackJsonp([1],{E51W:function(t,e){},NHnr:function(t,e,o){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var a=o("7+uW"),n={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{attrs:{id:"app"}},[e("router-view")],1)},staticRenderFns:[]};var s=o("VU/8")({name:"App"},n,!1,function(t){o("gsu9")},null,null).exports,r=o("/ocq"),i=o("7t+N"),l=o.n(i),m={name:"Home",computed:{auth:function(){if(sessionStorage.getItem("token"))return!0}},methods:{goLogin:function(){this.$router.push({name:"login"})},goReg:function(){this.$router.push({name:"registration"})},logout:function(){l.a.ajax({url:"http://127.0.0.1:8000/rest-auth/logout/",type:"GET",success:function(t){sessionStorage.removeItem("token"),window.location="/"}})}}},u={render:function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("mu-container",[o("mu-appbar",{staticStyle:{width:"100%"},attrs:{color:"primary"}},[t._v("\n            StackProject\n            "),t.auth?t._e():o("mu-button",{attrs:{slot:"right",flat:""},on:{click:t.goLogin},slot:"right"},[t._v("Login")]),t._v(" "),t.auth?o("mu-button",{attrs:{slot:"right",flat:""},on:{click:t.logout},slot:"right"},[t._v("Log out")]):o("mu-button",{attrs:{slot:"right",flat:""},on:{click:t.goReg},slot:"right"},[t._v("Sign-up")])],1)],1)},staticRenderFns:[]},c=o("VU/8")(m,u,!1,null,null,null).exports,d=(o("mtWM"),{name:"Login",components:{Home:c},data:function(){return{validateForm:{login:"",password:""},googleSignInParams:{client_id:"559920722496-ic02pjffmjq267e84pggsjhtb0vhq6ls.apps.googleusercontent.com"}}},methods:{setLogin:function(){var t=this;l.a.ajax({url:"http://127.0.0.1:8000/rest-auth/login/",type:"POST",data:{username:this.validateForm.login,password:this.validateForm.password},success:function(e){console.log(e),sessionStorage.setItem("token",e.token),t.$router.push({name:"home"})}})},onGoogleSignInSuccess:function(t){console.log(t);var e=t.uc.access_token;console.log(e),l.a.ajax({url:"http://localhost:8000/user/auth/google/",type:"POST",data:{access_token:e},success:function(t){console.log(t),sessionStorage.setItem("token",t.token),alert("auth success!")},error:function(t){console.log(t)}})}}}),p={render:function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("mu-container",[o("mu-row",[o("home")],1),t._v(" "),o("mu-container",[o("mu-form",{ref:"form",staticClass:"mu-demo-form",attrs:{model:t.validateForm}},[o("mu-form-item",{attrs:{label:"Login"}},[o("mu-text-field",{model:{value:t.validateForm.login,callback:function(e){t.$set(t.validateForm,"login",e)},expression:"validateForm.login"}})],1),t._v(" "),o("mu-form-item",{attrs:{label:"Password"}},[o("mu-text-field",{attrs:{type:"password"},model:{value:t.validateForm.password,callback:function(e){t.$set(t.validateForm,"password",e)},expression:"validateForm.password"}})],1),t._v(" "),o("mu-form-item",[o("mu-button",{attrs:{color:"primary"},on:{click:t.setLogin}},[t._v("Log in")])],1)],1)],1),t._v(" "),o("mu-row",[o("g-signin-button",{attrs:{params:t.googleSignInParams},on:{success:t.onGoogleSignInSuccess}},[o("button",{staticClass:"btn btn-block btn-success"},[t._v("\n          Google Signin\n        ")])])],1)],1)},staticRenderFns:[]};var g=o("VU/8")(d,p,!1,function(t){o("iHDi")},"data-v-62f4c6da",null).exports,f={name:"Registration",components:{Home:c},data:function(){return{validateForm:{login:"",email:"",password1:"",password2:""}}},methods:{regUser:function(){l.a.ajax({url:"http://127.0.0.1:8000/rest-auth/registration/",type:"POST",data:{username:this.validateForm.login,email:this.validateForm.email,password1:this.validateForm.password1,password2:this.validateForm.password2},success:function(t){alert("Success!"),window.location="/"},error:function(t){console.log(t.responseText)}})}}},v={render:function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("mu-container",[o("mu-container",[o("home")],1),t._v(" "),o("mu-form",{ref:"form",staticClass:"mu-demo-form",attrs:{model:t.validateForm}},[o("mu-form-item",{attrs:{label:"Display name"}},[o("mu-text-field",{model:{value:t.validateForm.login,callback:function(e){t.$set(t.validateForm,"login",e)},expression:"validateForm.login"}})],1),t._v(" "),o("mu-form-item",{attrs:{label:"Email"}},[o("mu-text-field",{attrs:{type:"email"},model:{value:t.validateForm.email,callback:function(e){t.$set(t.validateForm,"email",e)},expression:"validateForm.email"}})],1),t._v(" "),o("mu-form-item",{attrs:{label:"Password"}},[o("mu-text-field",{attrs:{type:"password"},model:{value:t.validateForm.password1,callback:function(e){t.$set(t.validateForm,"password1",e)},expression:"validateForm.password1"}})],1),t._v(" "),o("mu-form-item",{attrs:{label:"Confirm password"}},[o("mu-text-field",{attrs:{type:"password"},model:{value:t.validateForm.password2,callback:function(e){t.$set(t.validateForm,"password2",e)},expression:"validateForm.password2"}})],1),t._v(" "),o("mu-form-item",[o("mu-button",{attrs:{color:"primary"},on:{click:t.regUser}},[t._v("Sign in")])],1)],1)],1)},staticRenderFns:[]},h=o("VU/8")(f,v,!1,null,null,null).exports,w={name:"ConfirmEmail",created:function(){this.redirect()},methods:{redirect:function(){alert("Confirm email success"),window.location="/"}}},_={render:function(){var t=this.$createElement;return(this._self._c||t)("div")},staticRenderFns:[]},F=o("VU/8")(w,_,!1,null,null,null).exports;a.a.use(r.a);var b=new r.a({routes:[{path:"/",name:"home",component:c},{path:"/login",name:"login",component:g},{path:"/registration",name:"registration",component:h},{path:"/confirm_email",name:"confirm_email",component:F}]}),k=o("fSYm"),x=o.n(k),S=o("aFc6");o("E51W");a.a.use(S.a),a.a.use(x.a),a.a.config.productionTip=!1,new a.a({el:"#app",router:b,components:{App:s},template:"<App/>"})},gsu9:function(t,e){},iHDi:function(t,e){}},["NHnr"]);
//# sourceMappingURL=app.511f96c5fcc637b88038.js.map