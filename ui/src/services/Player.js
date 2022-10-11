import axios from "axios";

const API = () => {
  return axios.create({
    baseURL: "https://yhb9zv.deta.dev/api",
    // baseURL: "http://localhost:8080/api"
  });
};

// just a sample, not the actual one
export default {
  async getPlayers() {
    try {
      const response = await API().get("/players");
      return response.data;
    } catch (err) {
      return err;
    }
  },
  getPlayer(player_id) {
    return API().get(`/player/${player_id}`);
  },
};
