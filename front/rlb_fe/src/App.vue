<template>
  <div id="app" class="app">
    <div class="header">
      <img class="img" src="https://icon-library.com/images/chef-512_108586.png"/>
      <h1>Restaurante Los Brayans</h1>
      <nav>
        <button v-if="is_auth" v-on:click="loadMenu">Menu</button>
        <button v-if="is_auth" v-on:click="loadReserva">Reserva</button>
        <button v-if="is_auth" v-on:click="logOut">Cerrar Sesión</button>
        <button v-if="!is_auth" v-on:click="loadLogIn">Iniciar Sesión</button>
        <button v-if="!is_auth" v-on:click="loadSignUp">Registrarse</button>
      </nav>
    </div>
    <div class="main-component">
      <router-view
        v-on:completedLogIn="completedLogIn"
        v-on:completedSignUp="completedSignUp"
        v-on:logOut="logOut"
      >
      </router-view>
    </div>

    <div class="footer">
      <h2>© Copyright 2022 Restaurante Los Brayans - Todos los derechos reservados - <a href="http://www.copyright.es/registro-y-deposito.html#ixzz5IJrWuR00" target="nblank">Más información</a></h2>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  data: function () {
    return {
      is_auth: false,
    };
  },
  components: {},
  methods: {
    verifyAuth: function () {
      this.is_auth = localStorage.getItem("isAuth") || false;
      if (this.is_auth == false) this.$router.push({ name: "logIn" });
      else this.$router.push({ name: "menu" });
    },
    loadLogIn: function () {
      this.$router.push({ name: "logIn" });
    },
    loadSignUp: function () {
      this.$router.push({ name: "signUp" });
    },
    loadMenu: function () {
      this.$router.push({ name: "menu" });
    },
    logOut: function () {
      localStorage.clear();
      alert("Sesión cerrada");
      this.verifyAuth();
    },
    loadReserva: function () {
      this.$router.push({ name: "reserva" });
    },
    completedLogIn: function (data) {
      localStorage.setItem("token_access", data.token_access);
      localStorage.setItem("token_refresh", data.token_refresh);
      localStorage.setItem("username", data.username);
      localStorage.setItem("isAuth", true);
      alert("El inicio sesión fue correcto");
      this.verifyAuth();
    },
    completedSignUp: function (data) {
      alert("El registro fue exitoso");
      this.completedLogIn(data);
    },
  },
  created: function () {
    this.verifyAuth();
  },
};
</script>

<style>
body {
  margin: 0 0 0 0;
}
.header {
  margin: 0%;
  padding: 0;
  width: 100%;
  height: 10vh;
  min-height: 100px;
  background-color: #b2836cb9;
  color: #e5e7e9;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.header h1 {
  width: 60%;
  margin-left: -60px;
  text-align: left;
  font-family: Garamond;
  font-size: 280%;
  display: inline-block;
}
.header nav {
  height: 100%;
  width: 25%;
  display: flex;
  justify-content: space-around;
  align-items: center;
  font-size: 20px;
}
.header nav button {
  white-space: nowrap;
  color: #e5e7e9;
  background: #b2836c;
  border: 1px solid #e5e7e9;
  border-radius: 5px;
  padding: 10px 20px;
  
}
.header nav button:hover {
  color: #283747;
  background: #e5e7e9;
  border: 1px solid #e5e7e9;
}
.header img{
  margin: 1px 0px 1px 30px;
  height: 100px;
  width: auto;
  display: inline-block;
}
.main-component {
  height: 75vh;
  margin: 0%;
  padding: 0%;
  background: #fdfefe;
}
.footer {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 10vh;
  min-height: 100px;
  background-color: #b2836cb9;
  color: #e5e7e9;
}
.footer h2 {
  width: 100%;
  height: 100%;
  font-size:large;
  font-family: Garamond;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
