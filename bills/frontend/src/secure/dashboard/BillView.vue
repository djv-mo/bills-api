<template>
  <div class="album py-5 bg-light">
    <div class="container">
      <div class="row d-flex justify-content-center">
        <form v-if="!update" class="row" @submit.prevent="addItem">
          <div class="col-5">
            <input
              type="text"
              class="form-control"
              placeholder="Bill Item"
              aria-label="Bill Item"
              v-model="item"
              required
            />
          </div>
          <div class="col-5">
            <input
              step="0.01"
              pattern="^\d+(?:\.\d{1,2})?$"
              class="form-control"
              placeholder="price"
              aria-label="price"
              v-model="price"
              required
            />
          </div>
          <div class="col-1">
            <button type="submit" class="btn btn-info">
              Add
            </button>
          </div>
        </form>
        <!-- edit form -->
        <form v-else class="row" @submit.prevent="editItem">
          <div class="col-4">
            <input
              type="text"
              class="form-control"
              placeholder="Bill Item"
              aria-label="Bill Item"
              v-model="edit.item"
              required
            />
          </div>
          <div class="col-3">
            <input
              type="number"
              step="0.01"
              pattern="^\d+(?:\.\d{1,2})?$"
              class="form-control"
              placeholder="price"
              aria-label="price"
              v-model="edit.price"
              required
            />
          </div>
          <div class="col-3">
            <button type="submit" class="btn btn-success">
              ✓
            </button>
            <button
              @click="update = false"
              type="submit"
              class="btn btn-danger"
            >
              X
            </button>
          </div>
        </form>
      </div>
      <!-- list bills -->
      <div class="row d-flex justify-content-center py-3">
        <h5 class="col-4">Bill Name : {{ billname }}</h5>
        <h5 class="col-3">Total : {{ formatPrice(total) }}</h5>
        <h5 class="col-2">Count : {{ count }}</h5>
      </div>
      <!-- Export CSV -->
      <div class="row d-flex justify-content-center py-1">
        <button
          href="#"
          type="button"
          class="btn btn-outline-success col-3"
          @click="exportCSV()"
        >
          Export CSV
        </button>
      </div>
      <!-- End export CSV -->

      <div class="row d-flex justify-content-center py-3">
        <div class="row mb-1" v-for="item in items" :key="item.id">
          <div class="col-7">
            <ul class="list-group">
              <li
                class="list-group-item d-flex justify-content-between align-items-center"
              >
                {{ item.item }}

                <span class="badge bg-secondary rounded-pill">{{
                  formatPrice(item.price)
                }}</span>
              </li>
            </ul>
          </div>

          <div class="col-5">
            <button
              type="button"
              class="btn btn-outline-success"
              @click="
                this.edit = item;
                triggerUpdate();
              "
            >
              Edit
            </button>
            <button
              @click="
                this.edit = item;
                deleteItem();
              "
              type="button"
              class="btn btn-outline-danger"
            >
              Delete
            </button>
          </div>
          <p class="text-muted">Created : {{ item.created_at }}</p>
        </div>
      </div>
      <!-- load more -->
      <div class="d-flex mt-2 justify-content-center">
        <p class="font-weight-bold" v-show="isLoading">Loading .....</p>
        <br />
        <button v-show="next" class="btn btn-outline-info" @click="getItems">
          LoadMore
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { HTTP } from "@/common/api.service.js";

export default {
  name: "BillView",
  props: {
    id: {
      type: String,
      requried: true,
    },
  },
  data() {
    return {
      token: window.localStorage.getItem("token"),
      item: null,
      price: null,
      items: [],
      next: null,
      loading: false,
      total: null,
      billname: null,
      count: null,
      edit: {},
      update: false,
    };
  },
  methods: {
    async getItems() {
      let endpoint = "endpoint/bills/" + this.id + "/items/";
      if (this.next) {
        endpoint = this.next;
      }
      this.isLoading = true;
      this.next = null;
      try {
        let res = await HTTP.get(endpoint, {
          headers: { Authorization: "Token " + this.token },
        });
        this.items.push(...res.data.results);
        this.count = res.data.count;
        this.isLoading = false;
        if (res.data.next) {
          this.next = res.data.next;
        } else {
          this.next = null;
        }
      } catch (e) {
        await this.$router.push("/");
      }
    },
    async getTotal() {
      let endpoint = "endpoint/bills/" + this.id + "/";
      let res = await HTTP.get(endpoint, {
        headers: { Authorization: "Token " + this.token },
      });
      this.total = res.data.total;
    },
    async getBillName() {
      let endpoint = "endpoint/bills/" + this.id + "/";
      let res = await HTTP.get(endpoint, {
        headers: { Authorization: "Token " + this.token },
      });
      this.billname = res.data.name;
    },
    async addItem() {
      let endpoint = "endpoint/bills/" + this.id + "/items/";

      let res = await HTTP.post(
        endpoint,
        { item: this.item, price: this.price },
        {
          headers: { Authorization: "Token " + this.token },
        }
      );
      if (res) {
        this.items.unshift(res.data);
        this.item = "";
        this.price = "";
        this.count += 1;
      }
      this.getTotal();
    },
    async editItem() {
      let endpoint = "endpoint/items/" + this.edit.id + "/";
      let token = window.localStorage.getItem("token");

      let res = await HTTP.patch(
        endpoint,
        { item: this.edit.item, price: this.edit.price },
        {
          headers: { Authorization: "Token " + token },
        }
      );
      if (res) {
        this.update = false;
      }
      this.getTotal();
    },
    async deleteItem() {
      let endpoint = "endpoint/items/" + this.edit.id + "/";

      let res = await HTTP.delete(endpoint, {
        headers: { Authorization: "Token " + this.token },
      });
      if (res) {
        this.items.splice(
          this.items.findIndex((item) => item.id === this.edit.id),
          1
        );

        this.count -= 1;
      }
      this.getTotal();
    },
    async exportCSV() {
      let endpoint = "endpoint/bills/" + this.id + "/export/";
      let res = await HTTP.get(
        endpoint,
        {
          headers: { Authorization: "Token " + this.token },
        },
        { responseType: "blob" }
      );
      if (res) {
        var fileURL = window.URL.createObjectURL(
          new Blob([res.data], { type: "text/csv" })
        );

        var fileLink = document.createElement("a");

        fileLink.href = fileURL;

        fileLink.setAttribute("download", this.billname + ".csv");

        document.body.appendChild(fileLink);

        fileLink.click();
      }
    },
    triggerUpdate() {
      this.update = true;
      window.scrollTo(0, 0);
    },
    formatPrice(value) {
      let val = (value / 1).toFixed(2).replace(".", ",");
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    },
  },
  created() {
    this.getItems();
    this.getTotal();
    this.getBillName();
  },
};
</script>
