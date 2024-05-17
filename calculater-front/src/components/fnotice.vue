<template>
  <div >
   
    <el-row >
      <el-col :span="6" v-for="item in lists" :key="item.name"
        ><box><el-card :body-style="{ padding: '0px', marginBottom: '1px' }">
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
        </el-card></box></el-col
      >
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loading: true,

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
      console.log(username);
      await this.$http
        .get("/fnotice/", {
          params: { username },
        })
        .then((response) => {
          console.log(response.data);
          this.lists = response.data;
          console.log(this.lists);
        })
        .catch((error) => {
          console.log(error);
        });
      console.log("********");
    },
  },
};
</script>
<style >
</style>