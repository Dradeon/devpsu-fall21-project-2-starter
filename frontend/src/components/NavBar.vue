<template>
    <header class="masthead mb-auto site-header">
        <div class="inner">
            <nav class="nav nav-masthead justify-content-center">
                <router-link to="/" class="nav-link" exact>
                    Home
                </router-link>
                <router-link to="/todolist" class="nav-link" exact>
                    To Do List
                </router-link>
                <router-link to='/journal' class = "nav-link" exact>
                    Journal
                </router-link>
            </nav>
        </div>
    </header>
</template>

<style scoped>
    .nav-link:hover{
        text-decoration: underline;
    }
</style>
