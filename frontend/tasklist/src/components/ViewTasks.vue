<template>
  <div>
    <h2>YOUR TASK LIST</h2>
    <h4 id="refresh-btn" @click="getTasks()">Refresh</h4>
    <div class="task-container" v-for="task in tasks" :key="task[3]">
      <h4>{{ task[0] }}</h4>
      <div class="is-completed" v-if="task[2] == 1">
        <p>Completed</p>
      </div>
      <edit-task :taskId="task[3]" v-if="task[2] != 1" />
      <delete-task :taskId="task[3]" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import EditTask from "./EditTask.vue";
import DeleteTask from "./DeleteTask.vue";

export default {
  name: "ViewTasks",
  data() {
    return {
      tasks: [],
    };
  },
  components: {
    EditTask,
    DeleteTask,
  },
  methods: {
    getTasks: function() {
      axios
        .request({
          url: "http://localhost:5000/todo",
          method: "GET",
        })
        .then((response) => {
          console.log(response);
          this.tasks = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
    mounted() {
        this.getTasks();
    }
};
</script>

<style scoped>
.task-container {
  display: grid;
  align-items: center;
  justify-items: center;
  grid-template-columns: 4fr 2fr 2fr;
  border: 1px solid black;
  margin: 20px 0px 20px 0px;
  width: 90%;
  margin-left: 5%;
}
.date {
  display: grid;
  align-items: center;
  justify-items: center;
  grid-template-columns: 4fr 4fr;
}
#refresh-btn {
    border: 1px solid black;
    width: 5%;
    margin-left: 47.5%;
    padding: 3px;
    border-radius: 5%;
    box-shadow: 1px 0px 5px darkgray;
    cursor: pointer;
}
</style>
