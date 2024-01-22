import { createRouter, createWebHashHistory } from "vue-router";
import App from "./App.vue";
import LogIn from "./components/LogIn.vue";
import SignUp from "./components/SignUp.vue";
import Menu from "./components/Menu.vue";
import ListMenu from "./components/ListMenu.vue";
import PlatoDia from "./components/PlatoDia.vue";
import Reserva from "./components/Reserva.vue";

const routes = [
  {
    path: "/",
    name: "App",
    component: App,
  },
  {
    path: "/user/logIn",
    name: "logIn",
    component: LogIn,
  },
  {
    path: "/user/signUp",
    name: "signUp",
    component: SignUp,
  },
  {
    path: "/user/menu",
    name: "menu",
    component: Menu,
  },
  {
    path: "/user/menu/listmenu",
    name: "listMenu",
    component: ListMenu,
  },
  {
    path: "/user/menu/platodia",
    name: "platoDia",
    component: PlatoDia,
  },
  {
    path: "/user/reserva",
    name: "reserva",
    component: Reserva,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
