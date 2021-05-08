<template>
  <v-container>
    <v-row style="align-items: center">
      <v-col cols="auto" md="8">
        <header style="display: flex; align-item: center">
          <img
            src="https://media-exp1.licdn.com/dms/image/C4D03AQEv5pwuqH27wA/profile-displayphoto-shrink_100_100/0/1592516435483?e=1625702400&v=beta&t=Blk4ad1rNtLA2pDgeCqWQJO-afDqtJ16Xsghl_RVeUE"
            alt="photo-of-me-(lol)"
            style="border-radius: 50%; margin-right: 1.5em"
          />
          <div>
            <p style="font-size: 2em; font-weight: bold">Hi there!</p>
            <h2>
              I am <a href="https://github.com/sylvanld">@hoshiyosan</a> (Sylvan
              Le Deunff)
            </h2>
          </div>
        </header>

        <hr style="margin: 1.5em auto" />

        <p>
          I currently work as a software engineer at Orange Business Services
          (in France).
        </p>

        <p>
          In my spare time, I like to develop many side projects, to improve my
          skills and learn new things, but mostly for fun!
        </p>
      </v-col>
      <v-col cols="auto" md="4">
        <figure>
          <img
            src="@/assets/raspberry.jpg"
            alt="home-made kubernetes cluster with 3 raspberry pi"
          />
          <figcaption>
            Home-made kubernetes cluster of 3 raspberry pi <br />
            this site is hosted on.
          </figcaption>
        </figure>
      </v-col>
    </v-row>
  </v-container>
</template>