import axios from "axios";

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

export const HTTP = axios.create({

  baseURL: `http://127.0.0.1:8000/`,
  headers: {
    Accept: "application/json",
    "Content-type": "application/json"
  },
  timeout: 10000,
  withCredentials: true
})
