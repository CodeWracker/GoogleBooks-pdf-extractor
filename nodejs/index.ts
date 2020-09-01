import api from "./configs/axios.config";

let response = api.data("").then((resp) => {
  console.log(resp.data);
});
