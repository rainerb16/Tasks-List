<template>
    <div class="post-container">
        <h3>Add New Task</h3>
        <textarea v-model="itemDescription" type="text" />
        <br />
        <input v-model="createdAt" type="date" />
        <h4 class="submit-btn" @click="addTask()">Submit</h4>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "addTask",
    data() {
        return {
        itemDescription: "",
        createdAt: ""
        };
    },
    methods: {
        addTask: function(){
            axios.request({
                url: "http://localhost:5000/todo",
                method: 'POST',
                headers: {
                    "Content-Type": "application/json"
                },
                data: {
                    description: this.itemDescription,
                    created_at: this.createdAt
                }
            }).then((response) => {
                console.log(response)
            }).catch((error) => {
                console.log(error)
            })
        }
    },
};
</script>

<style scoped>
.submit-btn {
    border: 1px solid black;
    width: 10%;
    border-radius: 5%;
    margin-left: 45%;
    box-shadow: 1px 0px 5px darkgray;
    cursor: pointer;
}
.post-container {
    margin-bottom: 10vh;
}
input {
    margin: 15px;
}
</style>