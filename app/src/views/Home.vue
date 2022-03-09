<template>
  <div>
    <section class="px-4 py-5 my-5 text-center">
      <h1 class="display-5 fw-bold">isitabot</h1>
      <div class="col-lg-6 mx-auto">
        <p
          class="lead mb-4"
        >Use our Machine Learning Model to analyze plain text to detect whether it was written by a bot or a person</p>
        <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
          <router-link
            to="/text-analysis"
            class="btn btn-primary btn-lg px-4 gap-3"
          >Plain Text Analysis</router-link>
        </div>
      </div>
    </section>

    <section>
      <div class="row">
        <div class="col-md mb-4 mx-4 text-center">
          <div class="my-3 py-3">
            <h2 class="display-5 text-nowrap">Plain Text Analysis</h2>
            <p class="lead">No frills. No nonsense. Just analytics.</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>