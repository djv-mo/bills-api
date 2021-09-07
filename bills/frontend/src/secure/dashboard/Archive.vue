<template>
  <div class="album py-5 bg-light">
    <div class="container" v-if="bills.length">
      <!-- Bills list -->
      <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
        <div class="col" v-for="bill in bills" :key="bill.id">
          <div class="card shadow-sm">
            <div class="card-body">
              <h3 class="card-text">{{ bill.name }}</h3>
              <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                  <button
                    type="button"
                    class="btn btn-sm btn-outline-info"
                    @click="
                      this.bill = bill;
                      triggerUnArchive();
                    "
                  >
                    UnArchive
                  </button>
                </div>
                <strong>Total: {{ formatPrice(bill.total) }}</strong>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="d-flex mt-5 justify-content-center">
        <p class="font-weight-bold" v-show="isLoading">Loading .....</p>
        <br />
        <button v-show="next" class="btn btn-outline-info" @click="getBills">
          LoadMore
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { HTTP } from "@/common/api.service.js";

export default {
  name: "Dashboard",
  data() {
    return {
      token: window.localStorage.getItem("token"),
      bills: [],
      next: null,
      isLoading: false,
      bill: {},
    };
  },
  methods: {
    async getBills() {
      let endpoint = "endpoint/archived/";
      if (this.next) {
        endpoint = this.next;
      }
      this.isLoading = true;
      this.next = null;
      try {
        let res = await HTTP.get(endpoint, {
          headers: { Authorization: "Token " + this.token },
        });
        this.bills.push(...res.data.results);
        this.isLoading = false;
        if (res.data.next) {
          this.next = res.data.next;
        } else {
          this.next = null;
        }
      } catch (e) {
        console.log(e);
      }
    },
    async triggerUnArchive() {
      let endpoint = "endpoint/bills/" + this.bill.id + "/archive/";

      let res = await HTTP.put(
        endpoint,
        {},
        {
          headers: { Authorization: "Token " + this.token },
        }
      );
      if (res) {
        this.bills.splice(
          this.bills.findIndex((bill) => bill.id === this.bill.id),
          1
        );
      }
    },
    formatPrice(value) {
      let val = (value / 1).toFixed(2).replace(".", ",");
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    },
  },
  created() {
    this.getBills();
  },
};
</script>
<style scoped>
div.error {
  color: red;
}
div.no-bills {
  text-align: center;
  color: rgb(221, 117, 75);
  font-size: 22px;
}
</style>
