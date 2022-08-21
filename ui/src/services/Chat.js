import API from "./API";

// just a sample, not the actual one
export default {
    getChats(){
        return API().get('/chat')
    },
    createChat(data){
        return API().post('/', data)
    }
}