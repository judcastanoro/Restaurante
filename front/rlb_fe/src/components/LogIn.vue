<template>
  <div class="logIn_user">
    <div class="container_LogIn_user">
      <h2>Iniciar Sesión</h2>
      <form v-on:submit.prevent="processLogInUser">
        <input
          type="text"
          v-model="user.username"
          placeholder="Nombre de Usuario"
        />
        <br />
        <input
          type="password"
          v-model="user.password"
          placeholder="Contraseña"
        />
        <br />
        <button type="submit">Iniciar Sesión</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
//import { request } from "http";
export default {
  name: "LogIn",
  data: function () {
    return {
      user: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    processLogInUser: function () {
      axios.post(
                "https://rlb-mintic-be.herokuapp.com/login/",
                this.user,
                {headers:{}}
            )
            .then((result) => {
                let dataLogIn = {
                    token_access : result.data.access,
                    token_refresh: result.data.refresh,
                    username: this.user.username
                }
                this.$emit('completedLogIn',dataLogIn)
            })
            .catch((error) =>{
                if(error.response.status == "401")
                    alert("ERROR 401: Credenciales Incorrectas")
            });
    },
  },
};
</script>

<style>
.logIn_user {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;

  display: flex;
  justify-content: center;
  align-items: center;
}
.container_logIn_user {
  border: 3px solid #283747;
  border-radius: 10px;
  width: 25%;
  height: 60%;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.logIn_user h2 {
  color: #283747;
}
.logIn_user form {
  width: 70%;
}
.logIn_user input {
  height: 40px;
  width: 100%;
  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;
  border: 1px solid #283747;
}
.logIn_user button {
  width: 100%;
  height: 40px;
  color: #e5e7e9;
  background: #283747;
  border: 1px solid #e5e7e9;
  border-radius: 5px;
  padding: 10px 25px;
  margin: 5px 0;
}
.logIn_user button:hover {
  color: #e5e7e9;
  background: crimson;
  border: 1px solid #283747;
}
</style>
