<!--
 * @Date: 2021-11-05 14:25:04
 * @LastEditTime: 2021-11-29 21:22:39
 * @Description: 基于element-plus组件封装
-->
<script lang="tsx">
import { defineComponent } from 'vue'

export const yoTableProps = {
  data: {
    type: Array,
    default: () => []
  },
  align: {
    type: String,
    default: 'center'
  },
  column: {
    type: Array,
    default: () => []
  }
}

export default defineComponent({
  name: 'YoTable',
  props: {
    ...yoTableProps
  },
  setup(props, { attrs }) {
    return () => {
      const { data, column, align } = props

      const columnsSlots = column.map((column) => {
        const { render, ...restAtts } = column
        if (typeof render === 'function') {
          return <el-table-column align={align} {...restAtts}
            v-slots={{
              default: (scope) => {
                if (restAtts.prop) {
                  return render(scope.row[restAtts.prop], scope)
                }
                return render(scope)
              }
            }}
          />
        }
        return (
          <el-table-column align={align} {...restAtts} />
        )
      })
      return (
        <el-table data={data} class="wrapperr-table" ref="yoTable" {...attrs}>
          {
            columnsSlots
          }
        </el-table>
      )
    }
  },
  mounted() {
    const _self = this
    this.injectTablePrimaryMethods(_self)
  },
  methods: {
    // 将$refs.yoTable上的属性映射到this上, 防止父组件访问Table链过长
    // https://element-plus.org/zh-CN/component/table.html#table-方法
    injectTablePrimaryMethods(_self) {
      const tableMethodNameList = ['clearSelection', 'toggleRowSelection', 'toggleAllSelection', 'toggleRowExpansion', 'setCurrentRow', 'clearSort', 'clearFilter', 'doLayout', 'sort']
      for (const methodName of tableMethodNameList) {
        if (_self[methodName]) {
          console.warn(`the ${methodName} method is exist!, please rename it `)
        } else {
          _self[methodName] = this.$refs.yoTable[methodName]
        }
      }
    }
  },
  render(){
    console.log(this)
    const { data, column, align } = this
    // return (
    //     <el-table data={data} class="wrapperr-table" ref="yoTable" {...attrs}>
    //       {
    //         columnsSlots
    //       }
    //     </el-table>
    //   )
  }
})
</script>

<style scoped>
.wrapperr-table {
  margin-top: 24px;
  width: 100%;
  min-height: 300px;
}
</style>
