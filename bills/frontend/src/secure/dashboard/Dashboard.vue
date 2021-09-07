<template>
  <div class="album py-5 bg-light">
    <div class="container">
      <!-- add new bill -->
      <div v-if="!update" class="d-flex justify-content-center">
        <form class="mb-3" @submit.prevent="addBill">
          <div class="input-group mb-3">
            <input type="text" v-model="billname" class="form-control" />
            <button type="submit" class="btn btn-info">
              Add Bill
            </button>
          </div>
          <div class="error" v-if="error">{{ error }}</div>
        </form>
      </div>
      <!-- update bill -->
      <div v-else class="d-flex justify-content-center">
        <form class="mb-3" @submit.prevent="updateBill">
          <div class="input-group mb-3">
            <input type="text" v-model="bill.name" class="form-control" />
            <button type="submit" class="btn btn-success">
              Update Bill
            </button>
            <button @click="update = false" class="btn btn-danger">
              Cancel
            </button>
          </div>
          <div class="error" v-if="error">{{ error }}</div>
        </form>
      </div>
      <!-- Bills list -->
      <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
        <div class="col" v-for="bill in bills" :key="bill.id">
          <div class="card shadow-sm">
            <div class="card-body">
              <h3 class="card-text">{{ bill.name }}</h3>
              <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                  <router-link
                    type="button"
                    class="btn btn-sm btn-outline-secondary"
                    :to="{ name: 'BillView', params: { id: bill.id } }"
                  >
                    View
                  </router-link>
                  <button
                    type="button"
                    class="btn btn-sm btn-outline-info"
                    @click="
                      this.bill = bill;
                      triggerUpdate();
                    "
                  >
                    Edit
                  </button>
                  <button
                    type="button"
                    class="btn btn-sm btn-outline-danger"
                    @click="
                      this.bill = bill;
                      triggerArchive();
                    "
                  >
                    Archive
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
      billname: null,
      error: null,
      update: false,
      bill: {},
    };
  },
  methods: {
    async getBills() {
      let endpoint = "endpoint/bills/";
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
    async addBill() {
      let endpoint = "endpoint/bills/";
      if (this.billname) {
        try {
          let res = await HTTP.post(
            endpoint,
            { name: this.billname },
            {
              headers: { Authorization: "Token " + this.token },
            }
          );
          if (res) {
            this.bills.unshift(res.data);
            this.billname = "";
            this.error = null;
          }
        } catch (e) {
          console.log(e);
        }
      } else {
        this.error = "this field is required";
      }
    },
    async updateBill() {
      let endpoint = "endpoint/bills/" + this.bill.id + "/";
      let token = window.localStorage.getItem("token");
      if (this.bill.name) {
        try {
          let res = await HTTP.patch(
            endpoint,
            { name: this.bill.name },
            {
              headers: { Authorization: "Token " + token },
            }
          );
          if (res) {
            this.error = null;
            this.update = false;
          }
        } catch (e) {
          console.log(e);
        }
      } else {
        this.error = "this field is required";
      }
    },
    triggerUpdate() {
      this.update = true;
      window.scrollTo(0, 0);
    },
    async triggerArchive() {
      let endpoint = "endpoint/bills/" + this.bill.id + "/archive/";

      let res = await HTTP.post(
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
  color: blue;
  font-size: 22px;
}
</style>
