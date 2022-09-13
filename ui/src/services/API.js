import axios from "axios";

// this will have to be broken down further for diff microservices
export default (url = "http://localhost:8000") => {
  return axios.create({
    baseURL: url,
  });
};
