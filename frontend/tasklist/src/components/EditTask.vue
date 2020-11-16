<template>
  <div>
    <div class="post-container">
        <h4>Complete Task</h4>
        <input type="checkbox" @click="editTask()">
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "editTask",
  data() {
    return {
      itemDescription: "",
      completed: Number
    };
  },
  props: {
    taskId: {
      type: Number,
      required: true,
    }
  },
  methods: {
    editTask: function() {
      axios
        .request({
          url: "http://localhost:5000/todo",
          method: "PATCH",
          headers: {
            "Content-Type": "application/json",
          },
          data: {
            description: this.itemDescription,
            id: this.taskId,
            completed: 1,
          },
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
/* .submit-btn {
  border: 1px solid black;
  width: 100%;
  border-radius: 5%;
  box-shadow: 1px 0px 3px black;
  cursor: pointer;
} */
.post-container {
  display: grid;
  align-items: center;
  justify-items: center;
  grid-template-columns: 2fr;
}
input {
    margin-bottom: 15px;
}
</style>
