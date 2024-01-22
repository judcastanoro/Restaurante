<template>
  <div class="reserva">
    <div class="container_reserva">
      <h2>Realizar Reserva</h2>
      <form v-on:submit.prevent="realizarReserva">
        <input
          type="date"
          v-model="reserva.fecha_reserva"
          placeholder="Fecha"
        />
        <br />
        <input
          type="number"
          v-model="reserva.cant_personas"
          placeholder="Cant. Personas"
        />
        <br />
        <input type="text" v-model="reserva.observaciones" placeholder="Observasiones" />
        <br />
        <button type="submit">RESERVAR</button>
      </form>
    </div>
  </div>
</template>


<script>
import axios from "axios";
import jwt_decode from 'jwt-decode';
//import { request } from "http";
let token = localStorage.getItem("token_access");
export default {
  name: "Reserva",
  data: function () {
    return {
      reserva: {
        username: "",
        cant_personas: 0,
        observaciones: "",
        id_cliente_fk: jwt_decode(token).user_id.toString(),
      },
    };
  },
  methods: {
    realizarReserva: async function () {
           if(localStorage.getItem("token_access")===null || localStorage.getItem("token_refresh")===null){
                this.$emit('logOut');
                return;
            }
        await this.verifyToken();
       let token = localStorage.getItem("token_access");


      axios.post(
        
            "https://rlb-mintic-be.herokuapp.com/create-reserva/",
            this.reserva,
            //{headers:{}}
            {headers:{'Authorization': `Bearer ${token}`}}
        )
        .then((result) =>{
          alert("Reserva Realizada")
            /*let dataSignUp = {
                token_access:result.data.access,
                token_refresh : result.data.refresh,
                username : this.user.username
            }
            this.$emit('completedReservation',dataSignUp)*/
        })
        .catch((error)=> {
            console.log(error)
            alert("ERROR en el registro del usuario")
        });
      
    },

      verifyToken: function(){
            return axios.post(
                "https://rlb-mintic-be.herokuapp.com/refresh/",
                {refresh:localStorage.getItem("token_refresh")},
                {headers:{}})
                .then((result)=>{
                    localStorage.setItem("token_access",result.data.access)
                })
                .catch(()=>{
                    this.$emit("logOut");
                });
        }


  },
};
</script>

<style>
.reserva {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: url(https://www.esan.edu.pe/images/blog/2019/12/11/1500x844-restaurantes-offline.jpg);
  background-attachment: fixed;
  background-size: cover;
}
.container_reserva {
  border: 3px solid #c9ccb9;
  border-radius: 10px;
  width: 25%;
  height: 60%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.reserva h2 {
  color: #242422;
}
.reserva form {
  width: 70%;
}
.reserva input {
  height: 40px;
  width: 100%;
  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;
  border: 1px solid #283747;
}
.reserva button {
  width: 100%;
  height: 40px;
  color: #e5e7e9;
  background: #283747;
  border: 1px solid #e5e7e9;
  border-radius: 5px;
  padding: 10px 25px;
  margin: 5px 0 25px 0;
}
.reserva button:hover {
  color: #e5e7e9;
  background: rgb(206, 205, 164);
  border: 1px solid #283747;

}
</style>
