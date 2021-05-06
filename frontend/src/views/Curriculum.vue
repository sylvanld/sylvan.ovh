<template>
  <v-container>
    <v-row>
      <v-col cols="auto" md="6" sm="12">
        <h2>Experience</h2>
        <v-timeline align-top dense>
          <v-timeline-item color="orange" small>
            <v-row class="pt-1">
              <v-col cols="3">
                <strong>2020 - today</strong>
              </v-col>
              <v-col>
                <strong>Software Engineer </strong>@Orange Business Services
                <div class="caption">
                  Kubernetes security (admission controller development)
                </div>
                <div class="caption">Cisco Viptela migration (SDWan)</div>
                <div class="caption">
                  Software defined datacenter automation
                </div>
              </v-col>
            </v-row>
          </v-timeline-item>

          <v-timeline-item color="grey" small>
            <v-row class="pt-1">
              <v-col cols="3">
                <strong>2017 - 2020</strong>
              </v-col>
              <v-col>
                <strong>Internship </strong>@Orange Business Services
                <div class="caption">
                  Automate usage of old business applications using Python
                </div>
                <div class="caption">
                  Automate interfaces tests with Selenium
                </div>
                <div class="caption">
                  Deploy a Docker infrastructure (Swarm, Grafana, Traefik, ...)
                </div>
                <div class="caption">
                  Development of an automaton orchestration system based on
                  tasks queues (written in JEE)
                </div>
              </v-col>
            </v-row>
          </v-timeline-item>
          <v-timeline-item color="grey" small>
            <v-row class="pt-1">
              <v-col cols="3">
                <strong>2016</strong>
              </v-col>
              <v-col>
                <strong>Stage </strong>@STDM
                <div class="caption">
                  Development of a webapp allowing to visualize industrial
                  drawings in 3D.
                </div>
                <div class="caption">
                  Contribution in the development of a CMMS software.
                </div>
                <div class="caption">
                  Development of an RFID badging system (database, interface,
                  protocol).
                </div>
              </v-col>
            </v-row>
          </v-timeline-item>
        </v-timeline>
      </v-col>

      <v-col cols="auto" md="6" sm="12">
        <h2>Education</h2>
        <v-timeline align-top dense>
          <v-timeline-item color="grey" small>
            <v-row class="pt-1">
              <v-col cols="3">
                <strong>2017 - 2020</strong>
              </v-col>
              <v-col>
                <strong>Software Engineering Degree</strong> @ENSSAT
                <div class="caption">
                  (software development, machine learning, networks)
                </div>
              </v-col>
            </v-row>
          </v-timeline-item>
          <v-timeline-item color="grey" small>
            <v-row class="pt-1">
              <v-col cols="3">
                <strong>2016 - 2017</strong>
              </v-col>
              <v-col>
                <strong>Associate’s Degree</strong> @IUT de Lannion
                <div class="caption">
                  (two-year university degree in networks &amp;
                  telecommunications)
                </div>
              </v-col>
            </v-row>
          </v-timeline-item>
          <v-timeline-item color="grey" small>
            <v-row class="pt-1">
              <v-col cols="3">
                <strong>2014 - 2016</strong>
              </v-col>
              <v-col>
                <strong>CPGE</strong> @Lycée Rabelais
                <div class="caption">
                  (undergraduate courses to prepare nationwide competitive exams
                  in maths and physics)
                </div>
              </v-col>
            </v-row>
          </v-timeline-item>
        </v-timeline>
      </v-col>
    </v-row>
  </v-container>
</template>