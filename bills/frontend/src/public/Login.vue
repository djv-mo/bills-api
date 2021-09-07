<template>
  <div class="main">
    <section class="signup">
      <div class="container">
        <div class="signup-content">
          <form class="signup-form" @submit.prevent="Login">
            <h2 class="form-title">Login</h2>
            <div class="form-group">
              <input
                type="text"
                class="form-input"
                name="name"
                placeholder="Your Name"
                required
                v-model="username"
              />
            </div>
            <div class="form-group">
              <input
                type="password"
                class="form-input"
                name="password"
                placeholder="Password"
                required
                v-model="password"
              />
              <div class="error" v-if="error">{{ error }}</div>
            </div>
            <div class="form-group">
              <input
                type="submit"
                name="submit"
                id="submit"
                class="form-submit"
                value="Login"
              />
            </div>
          </form>
          <p class="loginhere">
            Don't have an account ?
            <router-link :to="{ name: 'register' }" class="loginhere-link"
              >Register</router-link
            >
          </p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { ref } from "vue";
import { HTTP } from "@/common/api.service.js";
import { useRouter } from "vue-router";
import { onBeforeMount } from "vue";

export default {
  name: "Login",
  setup() {
    const username = ref("");
    const password = ref("");
    // catching errors
    const error = ref("");
    // Router const
    const router = useRouter();
    // Api call
    const Login = async () => {
      try {
        const response = await HTTP.post("accounts/login-auth/", {
          password: password.value,
          username: username.value,
        });
        const token = response.data["token"];
        window.localStorage.setItem("token", token);
        await router.push("/");
        error.value = "";
      } catch (err) {
        error.value = "Invalid Username or Password";
      }
      
    };
    onBeforeMount(() => {
      if (window.localStorage.getItem("token")) {
        router.push("/");
      }
    });

    return {
      username,
      password,
      error,
      Login,
    };
  },
};
</script>

<style scoped>
display-flex,
.display-flex,
.display-flex-center {
  display: flex;
  display: -webkit-flex;
}
list-type-ulli {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

a:focus,
a:active {
  text-decoration: none;
  outline: none;
  transition: all 300ms ease 0s;
  -moz-transition: all 300ms ease 0s;
  -webkit-transition: all 300ms ease 0s;
  -o-transition: all 300ms ease 0s;
  -ms-transition: all 300ms ease 0s;
}
input,
select,
textarea {
  outline: none;
  appearance: unset !important;
  -moz-appearance: unset !important;
  -webkit-appearance: unset !important;
  -o-appearance: unset !important;
  -ms-appearance: unset !important;
}
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  appearance: none !important;
  -moz-appearance: none !important;
  -webkit-appearance: none !important;
  -o-appearance: none !important;
  -ms-appearance: none !important;
  margin: 0;
}
input:focus,
select:focus,
textarea:focus {
  outline: none;
  box-shadow: none !important;
  -moz-box-shadow: none !important;
  -webkit-box-shadow: none !important;
  -o-box-shadow: none !important;
  -ms-box-shadow: none !important;
}
input[type="checkbox"] {
  appearance: checkbox !important;
  -moz-appearance: checkbox !important;
  -webkit-appearance: checkbox !important;
  -o-appearance: checkbox !important;
  -ms-appearance: checkbox !important;
}
input[type="radio"] {
  appearance: radio !important;
  -moz-appearance: radio !important;
  -webkit-appearance: radio !important;
  -o-appearance: radio !important;
  -ms-appearance: radio !important;
}
img {
  max-width: 100%;
  height: auto;
}
figure {
  margin: 0;
}
p {
  margin-bottom: 0;
  font-size: 15px;
  color: #777;
}
h2 {
  line-height: 1.66;
  margin: 0;
  padding: 0;
  font-weight: 900;
  color: #222;
  font-family: montserrat;
  font-size: 24px;
  text-transform: uppercase;
  text-align: center;
  margin-bottom: 40px;
}
.clear {
  clear: both;
}
body {
  font-size: 14px;
  line-height: 1.8;
  color: #222;
  font-weight: 400;
  font-family: montserrat;
  background-repeat: no-repeat;
  background-size: cover;
  -moz-background-size: cover;
  -webkit-background-size: cover;
  -o-background-size: cover;
  -ms-background-size: cover;
  background-position: center center;
  padding: 115px 0;
}
.container {
  width: 660px;
  position: relative;
  margin: 0 auto;
}
.display-flex {
  justify-content: space-between;
  -moz-justify-content: space-between;
  -webkit-justify-content: space-between;
  -o-justify-content: space-between;
  -ms-justify-content: space-between;
  align-items: center;
  -moz-align-items: center;
  -webkit-align-items: center;
  -o-align-items: center;
  -ms-align-items: center;
}
.display-flex-center {
  justify-content: center;
  -moz-justify-content: center;
  -webkit-justify-content: center;
  -o-justify-content: center;
  -ms-justify-content: center;
  align-items: center;
  -moz-align-items: center;
  -webkit-align-items: center;
  -o-align-items: center;
  -ms-align-items: center;
}
.position-center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  -moz-transform: translate(-50%, -50%);
  -webkit-transform: translate(-50%, -50%);
  -o-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
}
.signup-content {
  background: #fff;
  border-radius: 10px;
  -moz-border-radius: 10px;
  -webkit-border-radius: 10px;
  -o-border-radius: 10px;
  -ms-border-radius: 10px;
  padding: 50px 85px;
}
.form-group {
  overflow: hidden;
  margin-bottom: 20px;
}
.form-input {
  width: 100%;
  border: 1px solid #ebebeb;
  border-radius: 5px;
  -moz-border-radius: 5px;
  -webkit-border-radius: 5px;
  -o-border-radius: 5px;
  -ms-border-radius: 5px;
  padding: 17px 20px;
  box-sizing: border-box;
  font-size: 14px;
  font-weight: 500;
  color: #222;
}
.form-input::-webkit-input-placeholder {
  color: #999;
}
.form-input::-moz-placeholder {
  color: #999;
}
.form-input:-ms-input-placeholder {
  color: #999;
}
.form-input:-moz-placeholder {
  color: #999;
}
.form-input::-webkit-input-placeholder {
  font-weight: 500;
}
.form-input::-moz-placeholder {
  font-weight: 500;
}
.form-input:-ms-input-placeholder {
  font-weight: 500;
}
.form-input:-moz-placeholder {
  font-weight: 500;
}
.form-input:focus {
  border: 1px solid transparent;
  -webkit-border-image-source: -webkit-linear-gradient(
    to right,
    #9face6,
    #74ebd5
  );
  -moz-border-image-source: -moz-linear-gradient(to right, #9face6, #74ebd5);
  -o-border-image-source: -o-linear-gradient(to right, #9face6, #74ebd5);
  border-image-source: linear-gradient(to right, #9face6, #74ebd5);
  -webkit-border-image-slice: 1;
  border-image-slice: 1;
  border-radius: 5px;
  -moz-border-radius: 5px;
  -webkit-border-radius: 5px;
  -o-border-radius: 5px;
  -ms-border-radius: 5px;
  background-origin: border-box;
  background-clip: content-box, border-box;
}
.form-input:focus::-webkit-input-placeholder {
  color: #222;
}
.form-input:focus::-moz-placeholder {
  color: #222;
}
.form-input:focus:-ms-input-placeholder {
  color: #222;
}
.form-input:focus:-moz-placeholder {
  color: #222;
}
.form-submit {
  width: 100%;
  border-radius: 5px;
  -moz-border-radius: 5px;
  -webkit-border-radius: 5px;
  -o-border-radius: 5px;
  -ms-border-radius: 5px;
  padding: 17px 20px;
  box-sizing: border-box;
  font-size: 14px;
  font-weight: 700;
  color: #fff;
  text-transform: uppercase;
  border: none;
  background-image: -moz-linear-gradient(to left, #74ebd5, #9face6);
  background-image: -ms-linear-gradient(to left, #74ebd5, #9face6);
  background-image: -o-linear-gradient(to left, #74ebd5, #9face6);
  background-image: -webkit-linear-gradient(to left, #74ebd5, #9face6);
  background-image: linear-gradient(to left, #74ebd5, #9face6);
}
input[type="checkbox"]:not(old) {
  width: 2em;
  margin: 0;
  padding: 0;
  font-size: 1em;
  display: none;
}
input[type="checkbox"]:not(old) + label {
  display: inline-block;
  margin-top: 7px;
  margin-bottom: 25px;
}
input[type="checkbox"]:not(old) + label > span {
  display: inline-block;
  width: 13px;
  height: 13px;
  margin-right: 15px;
  margin-bottom: 3px;
  border: 1px solid #ebebeb;
  border-radius: 2px;
  -moz-border-radius: 2px;
  -webkit-border-radius: 2px;
  -o-border-radius: 2px;
  -ms-border-radius: 2px;
  background: #fff;
  background-image: -moz-linear-gradient(white, white);
  background-image: -ms-linear-gradient(white, white);
  background-image: -o-linear-gradient(white, white);
  background-image: -webkit-linear-gradient(white, white);
  background-image: linear-gradient(white, white);
  vertical-align: bottom;
}
input[type="checkbox"]:not(old):checked + label > span {
  background-image: -moz-linear-gradient(white, white);
  background-image: -ms-linear-gradient(white, white);
  background-image: -o-linear-gradient(white, white);
  background-image: -webkit-linear-gradient(white, white);
  background-image: linear-gradient(white, white);
}
input[type="checkbox"]:not(old):checked + label > span:before {
  content: "\f26b";
  display: block;
  color: #222;
  font-size: 11px;
  line-height: 1.2;
  text-align: center;
  font-family: material-design-iconic-font;
  font-weight: 700;
}
.label-agree-term {
  font-size: 12px;
  font-weight: 600;
  color: #555;
}
.term-service {
  color: #555;
}
.loginhere {
  color: #555;
  font-weight: 500;
  text-align: center;
  margin-top: 91px;
  margin-bottom: 5px;
}
.loginhere-link {
  font-weight: 700;
  color: #222;
}
.field-icon {
  float: right;
  margin-right: 17px;
  margin-top: -32px;
  position: relative;
  z-index: 2;
  color: #555;
}
@media screen and (max-width: 768px) {
  .container {
    width: calc(100% - 40px);
    max-width: 100%;
  }
}
@media screen and (max-width: 480px) {
  .signup-content {
    padding: 50px 25px;
  }
}
div.error {
  color: red;
}
</style>
