<!--
 * @Date: 2021-10-12 10:45:32
 * @LastEditTime: 2021-10-20 11:35:37
 * @Description: 
-->
<script>
import { defineComponent, ref, watchEffect, reactive, watch } from "vue";
import {useDark} from '../hooks/useDark'

export default defineComponent({
  props: {
    init: {
      default: 0,
      type: Number,
    },
  },
  setup(props) {
    const count = ref(props.init);
    const dark = useDark()

    const increment = () => {
      count.value++;
    };

    watch(
      ()=> count.value,
      (count, prevCount) => {
        console.log("🚀 ~ setup ~ count, prevCount", count, prevCount)
        /* ... */
      }
    )

    watchEffect((...rest) => {
      console.log("🚀 ~ watchEffect ~ rest", rest)
      /* 
      count 会在初始运行时同步打印出来
      更改 count 时，将在组件更新前执行副作用。
       */
      console.log('watchEffect', count.value)
    }, 
     {
        flush: 'post' //  post值时, 更改 count 时，将在组件更新后执行副作用。
      }
    )

    // 
    const state = reactive({ 
      id: 1,
      attributes: { 
        name: '',
      }
    })

    const resWatch = watch(
      () => state,
      (state, prevState, onInvalidate) => {
        onInvalidate(()=>{
          console.log("🚀 ~ setup ~ onInvalidate", onInvalidate)
        })
        console.log("🚀 ~ setup ~ state, prevState", JSON.stringify(state, null, 2 ), JSON.stringify(prevState, null, 2 ))
        console.log("🚀 ~ setup ~ state.id, prevState.id", state.id, prevState.id) // 此处log id是一样的, 原因是返回都是同一个对象的引用, 除非用clonedeep
        /* ... */
      },
      {
        deep: true,
      }
    )

    // setTimeout(() => {
    //   resWatch()
    // }, 2500);
    return {
      count: count,
      increment,
      nested: {
        count
      },
      nested2: reactive({
        count,
        },
      ),
      state
    };
  },
  data() {
    return { msg: "setup demo" };
  },
  mounted() {
    let count = 3
    const timer = setInterval(() => {
      this.increment();
      this.state.id = Math.random()
      count++
      if(count >= 3){
        clearTimeout(timer)
      }

    }, 1000);
    console.log("🚀 ~ timer ~ timer", timer)
  },
  methods: {
    log(){
      console.log('this.count', this.count)
    }
    // increment() {
    //   console.log("in");
    //   this.count++;
    // },
  },
});
</script>

<template>
<div>
  <p>Counter: {{ count }} {{log && log()}}</p>
  <button @click="count ++">Increment count</button>
  <br>
  <button @click="nested.count.value++">ref -- Nested Increment count</button>
  <br>
  <button @click="nested2.count++">reactive -- Nested Increment count</button>

</div>
</template>
