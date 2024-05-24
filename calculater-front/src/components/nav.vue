
<template>
  <div class="wholepage">
    <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
    >
      <el-menu-item index="1"
        ><a @click="testClick1()" target="_blank" active-text-color = "#ffffff">运动表现</a></el-menu-item
      >
      <el-menu-item index="2"
        ><a @click="testClick2()" target="_blank" active-text-color = "#ffffff">饮食管理</a></el-menu-item
      >
      <el-menu-item index="4"
        ><a @click="testClick4()" target="_blank" active-text-color = "#ffffff">健身助手</a></el-menu-item
      >
      <el-menu-item index="5" style="float:right"  active-text-color = "#ffffff"
        ><a @click="testClick5()">欢迎，{{ this.username }}</a>
      </el-menu-item>
    </el-menu>

    <div class="fnotice">
      <el-row>
        <el-col :span="12" v-for="(item, index) in lists" :key="item.name">
          <el-card :body-style="{ padding: '0px', marginBottom: '1px' }" >
            <div style="padding: '14px'">
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
                style="width: 50%; height: 300px; display:none;float:left"
              ></div>
              <!--控制按钮 -->
              <br>
              <br>
              <div
                :id="'chart-container-' + index + '_2'"
                style="width: 50%; height: 300px; display:none;float: right"
              ></div>
              <el-button @click="toggleChart(index)">{{
                chartsVisible[index] ? "隐藏图表" : "显示图表"
              }}</el-button> 
            </div>
          </el-card>
        </el-col>
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
      calory_data: [],
      chartsVisible:[],
    };
  },
  mounted() {
    this.loading = false;
    this.lists = [];
    this.get_data(this.username, this);
    this.get_data_by_username(this.username);
    this.get_calory_by_username(this.username);
    // setTimeout(() => {
    //   this.showpic(0);
    // }, 500);
  },
  methods: {
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
    testClick5(){
      this.$router.push(
        {path:"/"});
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
    async get_calory_by_username(username, date){
      await this.$http
        .get("/submit2/", {
          params: { username: username,
                    date: date ,
          }
        })
        .then((response) => {
          console.log("[CALORY1]")
          console.log(response.data)
          this.calory_data = response.data[5];
          // console.log("[LOADED]")
          // console.log(this.calory_data[0][0].hot)
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
          console.log('!!!!')
          console.log(response.data)
          this.data = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    showpic(index) {
      const item = this.lists[index];
      const container = document.getElementById('chart-container-' + index);
      const chin_name_arr = []
      const each_score_num = []

      this.chart = echarts.init(container);
      console.log(this.data);
      for(var i=0;i<this.data.length;i++){
        //添加中文名和分数信息
        chin_name_arr.push(this.data[i].name)
        each_score_num.push(this.data[i].score)
      }
      

      

      const option = {
        color: ['#67F9D8', '#FFE434', '#56A3F1', '#FF917C'],
        tooltip: {
          trigger: 'axis',
        },
        legend: {
          orient: 'horizontal',
          bottom: -20,
          data: chin_name_arr
        },
        grid: [
          { left: '5%', right: '60%', top: '10%', bottom: '10%' },
          { left: '50%', right: '5%', top: '10%', bottom: '10%' }
        ],
        radar: [
          {
            indicator: [
              { name: 'BMI', max: 100 },
              { name: '肺活量', max: 100 },
              { name: '50m', max: 100 },
              { name: '坐位体前屈', max: 100 },
              { name: '立定跳远', max: 100 },
              { name: '引体向上', max: 100 },
              { name: '1000m', max: 100 }
            ],
            // center: ['20%', '50%'],
            radius: 100,
            axisName: {
              color: '#fff',
              backgroundColor: '#666',
              borderRadius: 3,
              padding: [3,5]
            },
            splitArea: {
              areaStyle: {
                color: ['#e6f3ff', '#ffffff'],
                shadowColor: 'rgba(0, 0, 0, 0.2)',
                shadowBlur: 10
              }
            },
          }
        ],

        series: [
          {
            name: '体能测试',
            type: 'radar',
            data: [
              {
                value: [100, 78, 78, 72, 72, 60, 74],
                name: '平均水准(70%)',
                symbol: 'rect',
                symbolSize: 6,
                lineStyle: {
                  type: 'dashed'
                },
                label: {
                  show: true,
                  formatter: function (params) {
                    return params.value;
                  }
                },
                itemStyle: {
                  normal: {
                    color: '#3399FF',  // 蓝色
                    borderColor: '#3399FF', // 定义边界线颜色
                    borderWidth: 3, // 定义边界线宽度
                  }
                }
              },
              {
                value: [this.data[0].score, this.data[1].score,this.data[2].score, this.data[3].score, this.data[4].score, this.data[5].score, this.data[6].score], // 假定这些值已正确定义
                name: '你的成绩',
                lineStyle: {
                  color: "#c4546b"
                },
                symbolSize: 4,
                symbol: 'circle',
                itemStyle: {
                  normal: {
                    color: '#ff6666',  // 红色
                    borderColor: '#ff6666',
                    borderWidth: 4,
                  }
                },
                lineStyle: {
                  normal: {
                    color: 'rgba(255, 102, 102, 0.5)', // 边界线颜色，透明度为 0.5 的红色
                    width: 2 // 边界线宽度
                  }
                },
                areaStyle: {
                  color: new echarts.graphic.RadialGradient(0.1, 0.6, 1, [
                    {
                      color: '#ff1a49',
                      offset: 1
                    },
                    {
                      color: '#ffccd7',
                      offset: 0
                    }
                  ])
                }
              }
            ]
          },
        ]
      };

      if (this.chart.getOption()) {
        //方法二
        this.chart.dispose();
        this.chart = echarts.init(container);
      }
      this.chart.setOption(option);
    },
    showpic_2(index) {
      const container = document.getElementById('chart-container-' + index + '_2');

      console.log('[PIC]')
      console.log(this.calory_data)
      this.chart = echarts.init(container);
      
      const option = {
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: ['早餐','午餐','晚餐','小吃','运动']
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            name: '早餐',
            type: 'line',
            stack: 'Total',
            data: [
              this.calory_data[0][0].hot,
              this.calory_data[0][0].hot,
              this.calory_data[0][0].hot,
              this.calory_data[0][0].hot,
              this.calory_data[0][0].hot,
              this.calory_data[0][0].hot,
              this.calory_data[0][0].hot,
            ]
          },
          {
            name: '午餐',
            type: 'line',
            stack: 'Total',
            data: [
              this.calory_data[0][1].hot,
              this.calory_data[1][1].hot,
              this.calory_data[2][1].hot,
              this.calory_data[3][1].hot,
              this.calory_data[4][1].hot,
              this.calory_data[5][1].hot,
              this.calory_data[6][1].hot,
            ]
          },
          {
            name: '晚餐',
            type: 'line',
            stack: 'Total',
            data: [
            this.calory_data[0][2].hot,
              this.calory_data[1][2].hot,
              this.calory_data[2][2].hot,
              this.calory_data[3][2].hot,
              this.calory_data[4][2].hot,
              this.calory_data[5][2].hot,
              this.calory_data[6][2].hot,
            ]
          },
          {
            name: '小吃',
            type: 'line',
            stack: 'Total',
            data: [
            this.calory_data[0][3].hot,
              this.calory_data[1][3].hot,
              this.calory_data[2][3].hot,
              this.calory_data[3][3].hot,
              this.calory_data[4][3].hot,
              this.calory_data[5][3].hot,
              this.calory_data[6][3].hot,
            ]
          },
          {
            name: '运动',
            type: 'line',
            stack: 'Total',
            data: [
            this.calory_data[0][4].hot,
              this.calory_data[1][4].hot,
              this.calory_data[2][4].hot,
              this.calory_data[3][4].hot,
              this.calory_data[4][4].hot,
              this.calory_data[5][4].hot,
              this.calory_data[6][4].hot,
            ]
          }
        ]
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
        document.getElementById(containerId + '_2').style.display = display;

        console.log
        
        if (this.chartsVisible[index]) {
          this.$nextTick(() => {
            this.initChart(index);
            this.initChart_2(index);
          });
        }
      },
    initChart(index){
      this.get_data_by_username(this.lists[index].username)
      this.get_calory_by_username(this.lists[index].username, new Date("2024-05-26"))
      console.log(this.lists[index].username)
      setTimeout(()=>{
        this.showpic(index)
      },500)
    },
    initChart_2(index){
      this.get_data_by_username(this.lists[index].username)
      this.get_calory_by_username(this.lists[index].username, new Date("2024-05-26"))
      console.log(this.lists[index].username)
      setTimeout(()=>{
        this.showpic_2(index)
      },500)
    },
  }
}

</script>
<style scoped>
.wholepage{
  height: 250vh;
  width: 100%;
  background:url('../../public/source/6.jpg') no-repeat center center fixed; background-size: 100%;
}
.el-card{
  background:rgba(255,255,255,0.5);
}


</style>