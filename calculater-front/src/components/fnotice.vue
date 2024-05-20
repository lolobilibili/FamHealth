<template>
  <div class="fnotice">
    <el-row>
      <el-col :span="6" v-for="item in lists" :key="item.name"
        ><el-card :body-style="{ padding: '0px', marginBottom: '1px' }">
            <div style="padding: 14px">
              <span
                ><b>{{ item.username }}</b></span
              >
              <div
                class="bottom card-header"
                style="height: 100px; word-wrap: break-word"
              >
                {{ item.text }}
              </div>
            </div>
          </el-card></el-col
      >
    </el-row> 
    <el-input
      type="textarea"
      :rows="2"
      style="width:60%;font-size:18px;"
      placeholder="请输入内容"
      v-model="textarea"
    >
    </el-input>
    <el-button @click="update_notice(username,textarea)" type="primary">更新留言</el-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loading: true,
      textarea:'',
      lists: [],
      username: this.$route.query.username,
    };
  },
  mounted() {
    this.loading = false;
    this.lists = [];
    this.get_data(this.username);
  },
  methods: {
    setLoading() {
      this.loading = true;
      setTimeout(() => (this.loading = false), 2000);
      console.log(this.username);
    },
    async get_data(username) {

      await this.$http
        .get("/fnotice/", {
          params: { username },
        })
        .then((response) => {

          this.lists = response.data;

        })
        .catch((error) => {
          console.log(error);
        });

    },
    async update_notice(username,textarea){
      
      await this.$http.get("/update_notice/",{
        params:{username,textarea}
      }).then((response) => {
        console.log(response);
        this.get_data(username);
        this.textarea=''
      }).catch((error) => {
        console.log(error);
      })
    }
  },
};
</script>
<style scoped>
.fnotice{
  height:100vh;
  background:url('../../public/source/6.jpg') no-repeat center center fixed; background-size: 100%;
}
.el-card{
  background:rgba(255,255,255,0.7);
}
</style>