
<template>
  <div>
    <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
    >
      <el-menu-item index="1"
        ><a @click="testClick1()" target="_blank">运动表现</a></el-menu-item
      >
      <el-menu-item index="2"
        ><a @click="testClick2()" target="_blank">饮食管理</a></el-menu-item
      >
      <el-menu-item index="3"
        ><a @click="testClick3()" target="_blank">家庭看板</a></el-menu-item
      >
      <el-menu-item index="4"
        ><a @click="testClick4()" target="_blank">健身助手</a></el-menu-item
      >
    </el-menu>

    <div class="fnotice">
      <el-row>
        <el-col :span="6" v-for="(item, index) in lists" :key="item.name"
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
              <div
                :id="'chart-container-' + index"
                style="width: 100%; height: 300px; display:none "
              ></div>
              <!--控制按钮 -->
              <el-button @click="toggleChart(index)">{{
                chartsVisible[index] ? "隐藏图表" : "显示图表"
              }}</el-button> 
            </div>
          </el-card></el-col
        >
      </el-row>
      <el-input
        type="textarea"
        :rows="4"
        style="width: 75%; font-size: 18px"
        placeholder="请输入内容"
        v-model="textarea"
      >
      </el-input>
      <el-button @click="update_notice(username, textarea)" type="primary"
        >更新留言</el-button
      >
      <div id="pic" style="width: 400px; height: 400px; background: "></div>
    </div>
  </div>
</template>
<script>
import * as echarts from "echarts";

export default {
  data() {
    return {
      activeIndex: "1",

      username: this.$route.query.username,
      textarea: "",
      lists: [],
      username: this.$route.query.username,
      data: [],
      chartsVisible:[],
    };
  },
  mounted() {
    this.loading = false;
    this.lists = [];
    this.get_data(this.username, this);
    this.get_data_by_username(this.username);
    // setTimeout(() => {
    //   this.showpic(0);
    // }, 500);
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    testClick1() {
      this.$router.push({ path: "/home", query: { username: this.username } });
    },
    testClick2() {
      this.$router.push({ path: "/plan", query: { username: this.username } });
    },
    testClick3() {
      this.$router.push({
        path: "/fnotice",
        query: { username: this.username },
      });
    },
    testClick4() {
      this.$router.push({
        path: "/chatbase",
        query: { username: this.username },
      });
    },
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
    async update_notice(username, textarea) {
      await this.$http
        .get("/update_notice/", {
          params: { username, textarea },
        })
        .then((response) => {
          console.log(response);
          this.get_data(username);
          this.textarea = "";
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async get_data_by_username(username) {
      this.spp = await this.$http
        .get("/get_user_data/", {
          params: { username: username },
        })
        .then((response) => {
          // console.log(response.data)
          this.data = response.data;
          // this.chart = echarts.init(document.getElementById("pic"))
          // const option = {
          //   series: [
          //     {
          //       type: "pie",
          //       data: [
          //         {
          //           value: response.data[0].score,
          //           name: String(response.data[0].name),
          //         },
          //         {
          //           value: response.data[1].score,
          //           name: String(response.data[1].name),
          //         },
          //         {
          //           value:response.data[2].score,
          //           name: String(response.data[2].name),
          //         },
          //       ],
          //     },
          //   ],
          // };
          // if (this.chart.getOption()) { //方法二
          //   this.chart.dispose()
          //   this.chart = echarts.init(document.getElementById(id))
          // }

          // this.chart.setOption(option);
          // console.log(response.data)
        })
        .catch((error) => {
          console.log(error);
        });
    },
    showpic(index) {
      const item = this.lists[index];
      const container = document.getElementById('chart-container-' + index);
      
      this.chart = echarts.init(container);
      console.log(this.data);
      const option = {
        series: [
          {
            type: "pie",
            data: [
              {
                value: this.data[0].score,
                name: String(this.data[0].name),
              },
              {
                value: this.data[1].score,
                name: String(this.data[1].name),
              },
              {
                value: this.data[2].score,
                name: String(this.data[2].name),
              },
            ],
            radius: "50%",
          },
        ],
      };
      if (this.chart.getOption()) {
        //方法二
        this.chart.dispose();
        this.chart = echarts.init(container);
      }

      this.chart.setOption(option);
    },
      toggleChart(index) {
        this.chartsVisible[index] = !this.chartsVisible[index];
        const containerId = 'chart-container-' + index;
        const display = this.chartsVisible[index] ? 'block' : 'none';
        // 定位图表
        document.getElementById(containerId).style.display = display;
        if (this.chartsVisible[index]) {
          this.$nextTick(() => {
            this.initChart(index);
          });
        }
      },
    initChart(index){
      this.get_data_by_username(this.lists[index].username)
      console.log(this.lists[index].username)
      setTimeout(()=>{
        this.showpic(index)
      },500)
    }
  },
};
</script>