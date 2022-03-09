<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <router-link class="navbar-brand" to="/">Isitabot</router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link
              class="nav-link active"
              aria-current="page"
              to="text-analysis"
            >Plaintext Analysis</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link active" aria-current="page" to="about">About</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>