<template>
    <div>
        <h4 class="delete-btn" @click="deleteTask()">Delete</h4>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "deleteTask",
    data() {
        return {
        status: ""
        };
    },
    props: {
        taskId: {
            type: Number,
            required: true 
        }
    },
    methods: {
        deleteTask: function(){
            axios.request({
                url: "http://localhost:5000/todo",
                method: 'DELETE',
                headers: {
                    "Content-Type": "application/json",
                },
                data: {
                    id: this.taskId
                }
            }).then((response) => {
                console.log(response)
                this.status = response.data
            }).catch((error) => {
                console.log(error)
            })
        }
    },
};
</script>

<style scoped>
.delete-btn {
    border: 1px solid black;
    width: 100%;
    padding: 3px;
    border-radius: 5%;
    box-shadow: 1px 0px 5px darkgray;
    cursor: pointer;
}
</style>
