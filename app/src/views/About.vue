<template>
	<div>
  <div class="p-5 mb-4 bg-light rounded-3">
    <div class="container-fluid py-5">
      <h1 class="display-5 fw-bold">about the project</h1>
      <p class="col-md-8 fs-4">
        isitabot is an adversarial model to detect the likelyhood text being machine generated. our text analysis tool can be used via a locally hosted application, or directly through its API.
        </p>
      <a class="btn btn-dark" href="https://github.com/badrchoubai/isitabot">
        <i class="bi bi-github"></i> view on github
      </a>
    </div>
  </div>

  <section class="w-100 m-auto">
    <h2>contributors</h2>

    <div class="row w-100 m-auto">
      <div class="card m-2 col-md">
        <div class="card-body d-flex flex-column justify-content-around">
          <h3 class="card-title">max b.</h3>
          <p class="card-text">max worked on the analysis of the probability matrix resulting from pretrained model comparison, as well as developing the overall architecture of the ML approach we took.</p>
          <div>
            <a href="https://github.com/maxwellbanks" class="my-1 btn btn-dark card-btn w-100"><i
                class="bi bi-github"></i> their github</a>
            <a href="https://www.linkedin.com/in/maxwell-a-banks" class="my-1 btn btn-secondary card-btn w-100"><i
                class="bi bi-linkedin"></i> their linkedin</a>
          </div>
        </div>
      </div>
      <div class="card m-2 col-md">
        <div class="card-body d-flex flex-column justify-content-around">
          <h3 class="card-title">george j.</h3>
          <p class="card-text">george created the custom module that takes a user's sample text and compares it to various pretrained GPT models. this module calculates the probabilities for an AI/ML model to have generated each word.</p>
          <div>
            <a href="https://github.com/georgej1144" class="my-1 btn btn-dark card-btn w-100"> <i
                class="bi bi-github"></i> their github</a>
            <a href="https://www.linkedin.com/in/george-johnson-37b641169"
              class="my-1 btn btn-secondary card-btn w-100"><i class="bi bi-linkedin"></i> their linkedin</a>
          </div>
        </div>
      </div>
      <div class="card m-2 col-md">
        <div class="card-body d-flex flex-column justify-content-around">
          <h3 class="card-title">jonathan</h3>
          <p class="card-text">jonathan worked on researching api wrappers for future milestones on the project, he also
            worked on gathering data and parsing it for use in training our model.</p>
          <div>
            <a href="https://github.com/spuwun" class="my-1 btn btn-dark card-btn w-100"><i class="bi bi-github"></i>
              their github</a>
            <a href="https://www.linkedin.com/in/badr-choubai-11b915223/" class="my-1 btn btn-secondary card-btn w-100"><i
                class="bi bi-linkedin"></i> their linkedin</a>
          </div>
        </div>
      </div>
      <div class="card m-2 col-md">
        <div class="card-body d-flex flex-column justify-content-around">
          <h3 class="card-title">badr c.</h3>
          <p class="card-text">badr worked on the front-end and contributed to both data aggregation and devops tasks.</p>
          <div>
            <a href="https://github.com/BadrChoubai" class="my-1 btn btn-dark card-btn w-100"><i class="bi bi-github"></i>
              their github</a>
            <a href="https://www.linkedin.com/in/BadrChoubai" class="my-1 btn btn-secondary card-btn w-100"><i
                class="bi bi-linkedin"></i> their linkedin</a>
          </div>
        </div>
      </div>
    </div>
  </section>
</div>
</template>