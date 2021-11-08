r<template>
  <div class="custom-home">
    <main role="main" class="inner cover">
      <h3 class="cover-heading">To Do List Manager and Bullet Journal</h3>
      <p class="lead">Click below to manage your to do list or journal</p>
      <p class="lead">
        <router-link pill class="btn btn-lg custom-btn" to="/todolist">Manage list</router-link>
      </p>
      <p class="lead">
        <router-link pill class= "btn btn-lg custom-btn" to="/journal">Write in Journal</router-link>
      </p>
    </main>
  </div>
</template>

<script>

export default {
  name: 'home'
}
</script>

