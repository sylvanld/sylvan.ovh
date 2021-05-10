import Vue from 'vue'
import Vuex from 'vuex'

import blog from './blog'
import github from './github'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    blog,
    github
  }
})
