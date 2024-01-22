<template>
    <div class="menu">
        <div class="container">
            <h1>Elige la opción de menu que quieres ver</h1>
            <button v-if="!is_auth" v-on:click="loadListMenu">Todo el menú</button>
            <button v-if="!is_auth" v-on:click="loadPlatoDia">Menú del día</button>
        </div>
    </div>
</template>

<script>
export default{
    name: "Menu",
    data: function() {

    },
    components: {

    },
    methods: {
        loadListMenu: function () {
            this.$router.push({ name: "listMenu" });
        },
        loadPlatoDia: function () {
            this.$router.push({ name: "platoDia" });
        },
    }

};
</script>

<style>
.menu{
    margin: 0;
    padding: 0%;
    height: 104%;
    width: 100%;
    background: url(https://www.enter.co/wp-content/uploads/2017/02/menu-restaurant-vintage-tableFINAL.jpg) no-repeat;
    background-attachment: fixed; 
    background-size: cover;
    display: flex;
    justify-content: center;
    align-items: center;
}
.container h1
{
    margin: 50px 0 0 0;
    color: #E5E7E9;
    font-family: Verdana, Geneva, Tahoma, sans-serif;
}
.container{
    text-align: center;
    width: 60%;
    height: 60%;
    box-shadow: 0 0 1rem 0 rgba(0, 0, 0, .2); 
    border-radius: 5px;
    position: relative;
    z-index: 1;
    background: inherit;
    overflow: hidden;
}
.container:before {
  content: "";
  position: absolute;
  background: inherit;
  z-index: -1;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  box-shadow: inset 0 0 2000px rgba(191, 248, 245, 0.486);
  filter: blur(10px);
  margin: -20px;
}
 .container button
{
    width: 250px;
    height: 45px;
    color: #E5E7E9;
    background: #b2836c;
    border: 1px solid #E5E7E9;
    border-radius: 5px;
    padding: 10px 25px;
    margin: 5px 10px 25px 10px;
    position:relative;
    top:20%;
    font-size: medium;
}
 .container button:hover {
    color: #283747;
    background: #e5e7e9;
    border: 1px solid #e5e7e9;
 }
</style>