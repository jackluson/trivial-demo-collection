<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  props: {
    init: {
      default: 0,
      type: Number,
    },
  },
  setup(props) {
    const count = ref(props.init);

    const increment = () => {
      count.value++;
    };
    return {
      count: count,
      increment,
    };
  },
  data() {
    return { msg: "setup demo" };
  },
  mounted() {
    setInterval(() => {
      this.increment();
    }, 1000);
  },
  methods: {
    // increment() {
    //   console.log("in");
    //   this.count++;
    // },
  },
});
</script>

<template>Counter: {{ count }}</template>
