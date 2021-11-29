import Vue from 'vue';
import Router from 'vue-router';
import Short from '@/components/Short';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Short',
      component: Short,
    },
  ],
});
