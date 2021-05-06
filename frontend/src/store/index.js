import Vue from 'vue'
import Vuex from 'vuex'

import github from './github'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    github
  }
})
