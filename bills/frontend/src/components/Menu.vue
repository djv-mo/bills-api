<template>
  <header>
    <div class="collapse bg-info" id="navbarHeader">
      <div class="container">
        <div class="row">
          <div class="col-sm-4 offset-md-1 py-4">
            <ul class="nav nav-pills">
              <li class="nav-item me-3 ">
                <router-link
                  :to="{ name: 'Dashboard' }"
                  class="nav-link active "
                  aria-current="page"
                  href="#"
                  >Home</router-link
                >
              </li>
              <li class="nav-item me-3">
                <router-link
                  class="nav-link active"
                  aria-current="page"
                  href="#"
                  :to="{ name: 'Archive' }"
                  >Archived</router-link
                >
              </li>
              <li class="nav-item">
                <a
                  class="nav-link active"
                  aria-current="page"
                  href="#"
                  @click="logout"
                  >Logout</a
                >
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="navbar navbar-dark bg-info shadow-sm">
      <div class="container">
        <router-link
          href="#"
          :to="{ name: 'Dashboard' }"
          class="navbar-brand d-flex align-items-center"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-journals me-2"
            viewBox="0 0 16 16"
          >
            <path
              d="M5 0h8a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2 2 2 0 0 1-2 2H3a2 2 0 0 1-2-2h1a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V4a1 1 0 0 0-1-1H3a1 1 0 0 0-1 1H1a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v9a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1H3a2 2 0 0 1 2-2z"
            />
            <path
              d="M1 6v-.5a.5.5 0 0 1 1 0V6h.5a.5.5 0 0 1 0 1h-2a.5.5 0 0 1 0-1H1zm0 3v-.5a.5.5 0 0 1 1 0V9h.5a.5.5 0 0 1 0 1h-2a.5.5 0 0 1 0-1H1zm0 2.5v.5H.5a.5.5 0 0 0 0 1h2a.5.5 0 0 0 0-1H2v-.5a.5.5 0 0 0-1 0z"
            />
          </svg>
          <strong>Bills</strong>
        </router-link>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarHeader"
          aria-controls="navbarHeader"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: "Menu",
  methods: {
    logout() {
      window.localStorage.setItem("token", "");
      this.$router.push("/login");
    },
  },
};
</script>
