
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
      <el-menu-item index="4"
        ><a @click="testClick4()" target="_blank">健身助手</a></el-menu-item
      >
    </el-menu>

    <div class="fnotice">
      <el-row>
        <el-col :span="10" v-for="(item, index) in lists" :key="item.name"
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
              <br>
              <br>
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
    setTimeout(() => {
      this.showpic(0);
    }, 500);
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
        // title: {
        //   text: '体育测试成绩可视化',
        //   left: 'center',
        //   textStyle: {
        //     color: '#333',
        //     fontFamily: 'Arial',
        //     fontWeight: 'bold',
        //     fontSize: 16,
        //     marginBottom: 100
        //   }
        // },
        tooltip: {
          // trigger: 'axis'
        },
        legend: {
          orient: 'horizontal',
          // left: 100,
          bottom: -20,
          data: chin_name_arr
        },
        radar: [
          {
            // 雷达图的指示器，表示多个变量的名称和最大值
            indicator: [
              // TODO 展示7项成绩
              { name: 'BMI', max: 100 },
              { name: '肺活量', max: 100 },
              { name: '50m', max: 100 },
              { name: '坐位体前屈', max: 100 },
              { name: '立定跳远', max: 100 },
              { name: '引体向上', max: 100 },
              { name: '1000m', max: 100 }
              // { name: 'BMI', max: 30 },
              // { name: '肺活量', max: 6000 },
              // { name: '50m', min: 6 },
              // { name: '坐位体前屈', max: 30 },
              // { name: '立定跳远', max: 290 },
              // { name: '引体向上', max: 30 },
              // { name: '1000m', min: "3'15" }
            ],
            center: ['20%', '50%'], // 调整雷达图的中心位置
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
                // TODO
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
                // value: [
                //   all_score_tem.bmi,
                //   all_score_tem.vital_capacity,
                //   all_score_tem.run_50,
                //   all_score_tem.sit_and_reach,
                //   all_score_tem.Pull_ups_and_sit_ups,
                //   all_score_tem.jump,
                //   all_score_tem.run_1000
                // ],
                
                // TODO
                value: [
                  this.data[0].score,
                  this.data[1].score,
                  this.data[2].score,
                  this.data[3].score,
                  this.data[4].score,
                  this.data[5].score,
                  this.data[6].score,
                  this.data[7].score,
                ],
                lineStyle: {
                  color: "#c4546b"
                },
                symbolSize: 4,
                symbol: 'circle', // 定义 symbol 为圆形
                name: '你的成绩',
                itemStyle: {
                  normal: {
                    color: '#ff6666',  // 红色
                    borderColor: '#ff6666', // 定义边界线颜色
                    borderWidth: 4, // 定义边界线宽度
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
          {
            name: '单项成绩',
            type: 'pie',
            radius: '40%',
            center: ['80%', '50%'],
            data: each_score_num.map((score, index) => ({
              value: score,
              name: chin_name_arr[index]
            })),
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            },
            itemStyle: { 
              normal: {
                color: function(params) {
                  var colorList = [
                    '#ff9a9e', '#fad0c4', '#fad0c4', '#f6d365', '#fda085',
                    '#96fbc4', '#f093fb', '#4facfe', '#00f2fe', '#4facfe',
                    '#f093fb', '#96fbc4', '#f6d365', '#fda085', '#ff9a9e'
                  ];
                  return new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                    {offset: 0, color: colorList[params.dataIndex * 2 % colorList.length]},
                    {offset: 1, color: colorList[(params.dataIndex * 2 + 1) % colorList.length]}
                  ]);
                },
                shadowBlur: 20,
                shadowColor: 'rgba(0, 0, 0, 0.1)'
              }
            },
            label: {
              position: 'outside',
              formatter: '{b}: {c}分 ({d}%)',
              textStyle: {
                fontSize: 12,
              }
            },
            labelLine: {
              show: true,
              length: 15, // 连接线长度
              length2: 10, // 连接线第二段长度
              lineStyle: {
                color: '#aaa' // 线条颜色
              }
            },
            animationType: 'scale',
            animationEasing: 'elasticOut',
            animationDelay: function (idx) {
              return Math.random() * 200;
            }
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