<script lang="tsx">
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'hellojsx',
  setup(){
    return {
      count: 3
    }
    // return ()=> {
    //   return (
    //     <h3>Vue3 TSX</h3>
    //   )
    // }
  },
  render(){
    console.log('this', this)
    return (
      <h3>Vue3 TSX{this.count}</h3>
    )
  },

})
</script>

<style scoped>

</style>
