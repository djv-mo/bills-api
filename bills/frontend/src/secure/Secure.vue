<template>
  <Menu />
  <main>
    <router-view />
  </main>
  <Footer />
</template>

<script>
import Menu from "@/components/Menu";
import Footer from "@/components/Footer";
import { HTTP } from "@/common/api.service.js";

export default {
  name: "Secure",
  components: {
    Menu,
    Footer,
  },
  data() {
    return {
      token: window.localStorage.getItem("token"),
    };
  },
  methods: {
    getUser() {
      HTTP.get("user/", {
        headers: { Authorization: "Token " + this.token },
      })
        .then((response) => {
          console.log("good");
        })
        .catch((e) => {
          window.localStorage.setItem("token", "");
          location.reload();
        });
    },
  },
  beforeMount() {
    this.getUser();
    if (this.token == "") {
      this.$router.push("/login");
    }
  },
};
</script>
