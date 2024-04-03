<template>
  <div class="app-content">
    <el-table
      :data="tableData"
      :span-method="objectSpanMethod"
      border
      style="width: 100%; margin-top: 20px"
    >
      <el-table-column prop="id" label="ID" width="180" />
      <el-table-column prop="name" label="姓名" />
    </el-table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tableData: [
        {
          id: "1",
          name: "王小虎"
        },
        {
          id: "1",
          name: "王小虎"
        },
        {
          id: "1",
          name: "王小虎"
        },
        {
          id: "2"
        },
        {
          id: "3",
          name: "王小虎"
        },
        {
          id: "3",
          name: "王小虎"
        },
        {
          id: "3",
          name: "王小虎"
        },
        {
          id: "3",
          name: "王小虎"
        },
        {
          id: "5",
          name: "王小虎"
        },
        {
          id: "5",
          name: "王小虎"
        }
      ]
    };
  },
  created() {
    this.setrowspans();
  },
  methods: {

    objectSpanMethod({ row, column, rowIndex, columnIndex }) {
      if (columnIndex === 0) {
        return {
          rowspan: row.rowspan,
          colspan: 1
        };
      }
    },
    setrowspans() {
      // 先给所有的数据都加一个v.rowspan = 1
      this.tableData.forEach(v => {
        v.rowspan = 1;
      });
      // 双层循环
      for (let i = 0; i < this.tableData.length; i++) {
        // 内层循环，上面已经给所有的行都加了v.rowspan = 1
        // 这里进行判断
        // 如果当前行的id和下一行的id相等
        // 就把当前v.rowspan + 1
        // 下一行的v.rowspan - 1
        for (let j = i + 1; j < this.tableData.length; j++) {
          //此处可根据相同字段进行合并，此处是根据的id
          if (this.tableData[i].id === this.tableData[j].id) {
            this.tableData[i].rowspan++;
            this.tableData[j].rowspan--;
          }
        }
        // 这里跳过已经重复的数据
        i = i + this.tableData[i].rowspan - 1;
      }
    }
  }
};
</script>

<style lang="scss" scoped>
</style>
