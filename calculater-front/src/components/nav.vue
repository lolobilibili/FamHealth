
<template>

<div>
  <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
  <el-menu-item index="1"><a  @click="testClick1()" target="_blank">运动表现</a></el-menu-item>
  <el-menu-item index="2"><a @click="testClick2()" target="_blank">饮食管理</a></el-menu-item>
  <el-menu-item index="3"><a @click="testClick3()" target="_blank">家庭看板</a></el-menu-item>
  <el-menu-item index="4"><a @click="testClick4()" target="_blank">健身助手</a></el-menu-item>
</el-menu>

</div>
</template>
<script>
  export default {
    data() {
      return {
        activeIndex: '1',
        
        username:this.$route.query.username
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath)

      },
      testClick1(){
        this.$router.push({ path:  '/home',query:{username:this.username}})
      },
      testClick2(){
        this.$router.push({ path:  '/plan',query:{username:this.username}})
      },
      testClick3(){
        this.$router.push({ path:  '/fnotice',query:{username:this.username}})
      },
      testClick4(){
        this.$router.push({ path:  '/chatbase',query:{username:this.username}})
      },
    }
  }
</script>