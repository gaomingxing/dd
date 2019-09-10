import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/home/home'
import Test from '@/views/test/test'
import Exercise from '@/views/test/exercise'
import Gmx from '@/views/test/gmx'
// import Exercise_test from '@/views/test/Exercise_test'

Vue.use(Router);

let router = new Router({
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home,
            title: '首页',
            meta: {
                title: '首页',
            }
        },
        {
            path: '/home',
            name: 'home',
            component: Home,
            title: '首页',
            meta: {
                title: '首页',
            }
        },
        {
            path: '/test',
            name: 'test',
            component: Test,
            title: '测试',
            // children: [
            //     {
            //         path: 'exercise',
            //         // name: 'exercise',
            //         component: Exercise,
            //     }
            // ]
        },
        {
            path: '/exercise',
            name: 'exercise',
            component: Exercise,
            title: '练习',
            meta: {
                title: '练习',
            }
        },
        {
            path: '/gmx',
            name: 'gmx',
            component: Gmx,
            title: '高明星',
            meta: {
                title: '高明星',
            }
        },
        // {
        //     path: '/exercise_test',
        //     name: 'exercise_test',
        //     component: Exercise_test,
        //     title: '我的练习',
        //     meta: {
        //         title: '我的练习',
        //     }
        // },
    ]
});

router.beforeEach((to, from, next) => {
    if (to.matched.length === 0) {
        from.path ? next({path: from.path}) : next('/');
    } else {
        next();
    }
});
export default router
