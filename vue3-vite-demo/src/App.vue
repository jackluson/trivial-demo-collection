<script setup lang="ts">

import HelloWorld from "./components/HelloWorld.vue";
import HelloWorldJSX from "./components/HelloWorld-JSX.vue";
console.log("🚀 ~ file: App.vue ~ line 5 ~ HelloWorldJSX", HelloWorldJSX)
import Counter from "./components/Counter.vue";
import CounterJS from "./components/CounterJS.vue";
import Table from './components/Table.vue'
defineExpose({
  name: 'MobileGameSwitchMgr'
})
</script>

<template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <HelloWorld msg="Hello Vue 3 + TypeScript + Vite" />
  <hr />
  <HelloWorldJSX/>
  <hr>
  <h3>Element plus</h3>
  <Table/>
  <hr>
  <Counter :init="3" />
  <CounterJS />
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
