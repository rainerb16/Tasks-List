<template>
    <div id="app">
        <h1 id="title">TASK LIST</h1>
        <add-task />
        <view-tasks />
    </div>
</template>

<script>
import ViewTasks from "./components/ViewTasks.vue";
import AddTask from "./components/AddTask.vue";


export default {
  name: "App",
  components: {
    ViewTasks,
    AddTask,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
#title {
    text-decoration: underline;
}
</style>
