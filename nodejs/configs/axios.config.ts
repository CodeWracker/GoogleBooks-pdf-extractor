import axios from "axios";

const data = axios.create({
  baseURL:
    "https://books.google.com.br/books?id=xxoXcuh0oS0C&hl=pt-BR&pg=PA3&jscmd=click3",
});
export default { data };
