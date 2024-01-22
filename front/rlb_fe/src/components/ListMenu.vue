<template>
    <div v-if="loaded" class="listMenu">
        <h1>Este es todo nuestro menú...</h1>
        <br/>
        <div class="container-menu columns">
            <div class="entradas">
                <h2>Entradas</h2>
                <hr>
                <tr v-for="menu in all_menu">
                    <td v-if="menu.categoria == 'Entradas'"><b>{{menu.nombre_plato}}</b></td>
                    <td class="descrip" v-if="menu.categoria == 'Entradas'">{{menu.descripcion}}</td>
                </tr>
            </div>
            <div class="platos_fuertes">
                <h2>Platos Fuertes</h2>
                <hr>
                <tr v-for="menu in all_menu">
                    <td v-if="menu.categoria == 'Platos fuertes'"><b>{{menu.nombre_plato}}</b></td>
                    <td class="descrip" v-if="menu.categoria == 'Platos fuertes'">{{menu.descripcion}}</td>
                </tr>
            </div>
            <div class="bebidas">
                <h2>Bebidas</h2>
                <hr>
                <tr v-for="menu in all_menu">
                    <td v-if="menu.categoria == 'Bebidas'"><b>{{menu.nombre_plato}}</b></td>
                    <td class="descrip" v-if="menu.categoria == 'Bebidas'">{{menu.descripcion}}</td>
                </tr>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import jwt_decode from 'jwt-decode';
export default {
    name:"ListMenu",
    data:function(){
        return{
            all_menu:[],
            loaded:false
        }
    },
    methods:{
        getData: async function(){
            if(localStorage.getItem("token_access")===null || localStorage.getItem("token_refresh")===null){
                this.$emit('logOut');
                return;
            }
            await this.verifyToken();
            let token = localStorage.getItem("token_access");

            axios.get(
                "https://rlb-mintic-be.herokuapp.com/list-menu/",
                {headers:{'Authorization': `Bearer ${token}`}} 
            )
            .then((result) => {
                this.all_menu=result.data;
                this.loaded=true;
            })
            .catch((error) =>{
                this.$emit('logOut');
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
    created: async function(){
        this.getData();   
    },
}
</script>

<style>
.listMenu{
    margin: 0;
    padding: 1%;
    height: 100%;
    width: 97%;
    display: flex;
    justify-content: center;
    background: url(https://png.pngtree.com/element_origin_min_pic/16/10/28/87fd55a6ef649a92e5fb3e0b13466f82.jpg) no-repeat;
    background-attachment: fixed; 
    background-size: cover;
}
.listMenu h1{
    font-family: Brush Script MT;
    font-size:60px;
    color: #301f16;
    margin-top: 1%;
    position: relative;
    text-shadow: 0px 0px 10px whitesmoke, 0px 0px 20px rgb(179, 175, 175);
}
.container-menu{
    margin: 7% 0 2% 0;
    padding: 2%;
    height: 45%;
	width: 90%;
	border: 1px solid #ddd;
    box-shadow: 0 0 1rem 0 rgba(0, 0, 0, .2); 
    border-radius: 5px;
	background: #f1f1f1;
    overflow-y: scroll;
    position: absolute;
    justify-content: center;
    align-items: center;
    display: grid;
    grid-template-columns:repeat(3,1fr);
    column-gap: 20px;
    row-gap: 20px;
 }
 .container-menu h2{
    font-family: Brush Script MT;
    font-size: 50px;
    text-align: center;
    color: #583e31f8;
 }
 .container-menu .entradas, .platos_fuertes, .bebidas{
    background-color: #b2836c65;
    background-size: cover;
    height: 100%;
 }

 .container-menu td{
    width: 30%;
    text-align: center;
    font-family: Garamond;
    font-size:x-large;
    padding: 20px;
 }
 .container-menu .descrip{
    text-align: justify;
    width: 70%;
 }
</style>