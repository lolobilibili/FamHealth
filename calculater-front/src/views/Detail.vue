
<template>
  <div class="about">
    <img src="../../public/source/background5.jpg"  style="position: fixed; z-index: -10; width: 100%; height: 100%" />
    <img src="../../public/source/Sufe.png"  style="position: absolute; right:10px;top:-60px; z-index: -1; width: 220px; height: 200px" />
    <!-- 弹窗 -->
  <el-popover
    placement="left-end"
    title="上海财经大学体测评分表（2024）"
    width="640"
    trigger="click"
    content="这是一段内容,这是一段内容,这是一段内容,这是一段内容。" style="position: absolute; right:350px;top:0px; z-index: 1; width: 220px; height: 200px">
      <ScoreTables></ScoreTables>
    <el-button slot="reference">点击查看体测评分表</el-button>
  </el-popover>

    <img src="../../public/source/recommend.png"  style="position: absolute; right:575px;top:36px; z-index: -1; width: 200px; height: 55px" />
    <div class="title" style="position: absolute; left:20px;top:30px; z-index: 1;" @click="go_back">
      <i class="el-icon-back" style="font-size:40px;color:#777" ></i>
    </div>
    <div class="body " style="display:flex;" transition-style="in:circle:top-left" >
      <div>
        <div id="maychar" ref="chart" style="width:680px; height:600px;"></div>
        <div class="suggestion" style="margin:12px 0 5px 50px;">
          <div style="font-size:20px;margin-bottom:5px;">小助手指南:</div>
          <ul v-if="score_data.total_data.score < 90">
            <div class="suggestion_item" v-for="(item,index) in suggestion" :key="index" style="margin:5px 0;color:#555;font-family:gb5;width:600px;">
              <li class="li_item" style="font-family:'gb5';">{{item}}</li>
            </div>
          </ul>
          <ul v-else>
            <div style="margin:5px 0;color:#555;font-family:gb5;width:600px;">
              <li class="li_item" style="font-family:'gb5';">当前成绩优秀，请继续保持。如需提升专项运动表现，请访问专项锻炼栏目。</li>
            </div>
            
          </ul>
          
        </div>
      </div>
      <div class="score" v-if="score_data.total_data.score >= 90" style="margin:120px 0 0 140px;">
        <img src="../../public/source/dance.gif" style="height:400px;width:400px;">
      </div>
      <div class="score" v-else>
        <div class="program_allscore" style="display:flex;margin: 50px;"></div>
        <div class="program" v-for="(item,index) in score_data.each_data" :key="index">
            <div class="program_front">
              <div class="program_title">{{item.name_chin}}</div>
              <div class="program_score">{{item.score}}<span class="unit">分</span> / {{item.performance}}<span class="unit">{{item.unit}}</span></div>
            </div>
            <div class="arrow" style="width:120px;">
              <img style="margin-left:30px;width:70px;height:30px;" src="../../public/source/arrow.gif">
            </div>
            <div v-if="show_recommend_flag==true" class="program_back" style="display:flex;justify-content: space-between;width:300px;">
              <div  :class="new_recommend_data.each_score[index].score>item.score?'program_score change_color':'program_score'">{{new_recommend_data.each_score[index].score }}<span class="unit">分</span> / {{new_recommend_data.each_score[index].performance || ""}}<span class="unit">{{item.unit}}</span> 
              <span class="arrow" style="margin:10px 0 0 10px;font-size:20px;" v-if="new_recommend_data.each_score[index].score>item.score"><i class="el-icon-top"></i></span></div>
              <el-button-group style="display:flex">
                <div class="btn_" style="margin:0 6px 0 2px;" @click="data_change(item,-1,index)">
                  <el-button class="btn_left btnn"    icon="el-icon-arrow-left"></el-button>
                </div>
                <div class="btn_" @click="data_change(item,1,index)" >
                  <el-button class="btn_right btnn"  ><i class="el-icon-arrow-right el-icon--right"></i></el-button>
                </div>
                
              </el-button-group>
            </div>
        
            


          

          

        </div>
        
        <div class="recommend_allscore">
          <div class="allscore_hint" style="font-size:26px;">
            预期总分
          </div>
          <div style=" margin-left: 350px;">
            {{this.new_recommend_data.all_score.score}}
          </div>
          
        </div>
      </div>
    </div>
    <!-- <h1>This is an about page</h1> -->
  <div>
  
  </div>
  
  </div>
</template>

<script>
import * as echarts from "echarts";
import ScoreTables from '../components/ScoreTables.vue'
export default {
  components:{
    ScoreTables:ScoreTables,
  },
  name: "Detail",
  data() {
    return {
      score_data:{
        each_data:[],
        total_data:{},
        mysuggestion:""
      },
      pass_data:{},
      new_recommend_data:{
        each_score:[],
        all_score:{}
      },
      visible: false,
      changed_item_score:{},
      show_recommend_flag:false,
      suggestion:[]
        
    };
  },
  async mounted() {
    this.bodyScale()
    console.log(this.$route.query.data);
    //对上一个页面传递的参数进行赋值
    this.score_data.each_data=this.$route.query.data.each_score
    this.score_data.total_data=this.$route.query.data.all_score
    this.score_data.mysuggestion=this.$route.query.data.all_score.suggestion
    console.log("建议",this.score_data.mysuggestion)
    console.log(this.score_data)
    this.pass_data=this.$route.query.pass_data
    const tem_pass_data=this.pass_data

    //获取推荐成绩接口
    await this.get_recommend_data(tem_pass_data)

    //展示图表，防止图表的渲染越界
    setTimeout(()=>{
      this.showPic()
    },200) 

    //处理给出的建议信息
    this.suggestion_process()
  },
  created(){
    
  },

  methods: {
    suggestion_process(){
      //对建议进行处理
      let suggestion=this.score_data.mysuggestion
      let suggestion_array=suggestion.split("*")
      let suggestion_array_length=suggestion_array.length
      let suggestion_array_new=[]
      for(let i=0;i<suggestion_array_length;i++){
        if(suggestion_array[i]!=""){
          suggestion_array_new.push(suggestion_array[i])
        }
      }
      this.suggestion=suggestion_array_new
    },
    async get_change_data(data,index){
      //获取后端第三个接口，当用户点击左右按钮
      await this.$http.get('/button/',{
          params:data
        })
          .then(response =>{
        console.log(data,"第三个接口请求",response.data)
        //将后端返回的数据，进行赋值
        this.changed_item_score=response.data[0]
        this.new_recommend_data.each_score[index].score=response.data[0].score;
        this.new_recommend_data.each_score[index].performance=response.data[0].performance;
        if(index==6) this.new_recommend_data.each_score[index].num_performance=response.data[0].num_performance;
        
        //更新传递参数
        const option=response.data[0].name
        if(option=="run_1000"){
          this.pass_data[option]=response.data[0].num_performance
        }else{
          this.pass_data[option]=response.data[0].performance
        }
        

        //更新总分
        this.get_data()
        })
        .catch(error =>{
        console.log(error)
        })
    },
    data_change(item,flag,index){
      //先判断按钮是否可以点击
      if((flag==-1 && this.new_recommend_data.each_score[index].score==10) || (flag==1 && this.new_recommend_data.each_score[index].score==100)){
        return
      }

      //点击按钮button后对数据进行调整
      const label=this.pass_data.label //获取基础信息
      const option=item.name
      const score=this.new_recommend_data.each_score[index].score
      const p_data={
        label,
        option,
        score,
        flag
      }
      //获取调整之后的数据
      this.get_change_data(p_data,index)
      
    },
    go_back(){
      //回到首页
      // console.log("点击了返回")
      // this.$router.push({path:'/'})
      this.$router.push({ path:  '/'})
    },
    async get_data(){
      console.log(this.pass_data)
      await this.$http.get('/data/',{
          params:this.pass_data
        })
          .then(response =>{
        console.log("第一个接口请求",response.data)
        //将接口返回的数据进行整理
        const tem_arr=response.data.slice(0,-1)
        this.new_recommend_data.each_score=JSON.parse(JSON.stringify(tem_arr))
        const [all]=response.data.slice(-1) //slice方式需要解构获取最后一个值
        this.new_recommend_data.all_score=all

        // this.show_recommend_flag=true
        
        console.log(this.new_recommend_data)
        })
        .catch(error =>{
        console.log(error)
        })
    },
    async get_recommend_data(data){
      //调用后端接口，获取各项成绩和总成绩
      await this.$http.get('/advise/',{
          params:data
        })
          .then(response =>{
        console.log("第二个接口请求",response.data)
        //将接口返回的数据进行整理
        const tem_arr=response.data.slice(0,-1)
        this.new_recommend_data.each_score=JSON.parse(JSON.stringify(tem_arr))
        const [all]=response.data.slice(-1) //slice方式需要解构获取最后一个值
        this.new_recommend_data.all_score=all

        this.show_recommend_flag=true
        
        console.log(this.new_recommend_data)
        this.create_recommend_pass_data()
        })
        .catch(error =>{
        console.log(error)
        
        })
        // console.log("********")
    },
    create_recommend_pass_data(){
      //更新传递的参数
     this.pass_data['bmi']=this.new_recommend_data.each_score[0].performance
     this.pass_data['vital_capacity']=this.new_recommend_data.each_score[1].performance
     this.pass_data['run_50']=this.new_recommend_data.each_score[2].performance
     this.pass_data['sit_and_reach']=this.new_recommend_data.each_score[3].performance
     this.pass_data['jump']=this.new_recommend_data.each_score[4].performance
     this.pass_data['Pull_ups_and_sit_ups']=this.new_recommend_data.each_score[5].performance
     const run_1000_score_str=this.new_recommend_data.each_score[6].num_performance
     this.pass_data['run_1000']=run_1000_score_str
     console.log("ok")

    },
    get_pic_data(){
      //生成图表的数据
      console.log(this.score_data.each_data)
      const all_score_tem=this.score_data.total_data
      const chin_name_arr=[]
      const each_score_num=[]
      const each_data=this.score_data.each_data
      for(var i=0;i<each_data.length;i++){
        //添加中文名和分数信息
        chin_name_arr.push(each_data[i].name_chin)
        each_score_num.push(each_data[i].score)
      }
      
      return {chin_name_arr,each_score_num,all_score_tem}

    },
    bodyScale () {
       //获取当前分辨率下的可是区域宽度
      var devicewidth = document.documentElement.clientWidth
      var scale = devicewidth / 1440// 分母——设计稿的尺寸
      document.body.style.zoom = scale//放大缩小相应倍数
      // alert(scale)
    },
    showPic(){
      //设置图形显示
      const {chin_name_arr,each_score_num,all_score_tem}=this.get_pic_data()
      each_score_num.unshift("体测成绩")
      const chin_col_name=chin_name_arr
      chin_col_name.unshift("quarter")
      

      const chartBox = echarts.init(document.getElementById("maychar"));
      
      const option = {
          title: {
            text: '当前总分',
            subtext:all_score_tem.score,
            left: 'center',
            top: 'center',
            textStyle: {
                        color: '#999',
                        fontFamily:'江西拙楷',
                        fontWeight: 'bold',
                        fontSize: 30,
                    },
            subtextStyle: {
                        color: '#000',
                        fontSize: 40,
                        fontFamily:"walk",
                        fontWeight:'bold'

                    }
          },
          legend: {
                    left: 'center',
                    bottom: '10',
                    orient:"horizontal",
                    data:chin_col_name,
                },
                dataset: {
                    source: [
                        chin_col_name,
                        each_score_num
                    ]
                },
                tooltip: {
                  trigger: "item"
                },
                series: [
                    {
                        name: '体测成绩',
                        type: 'pie',
                        seriesLayoutBy: 'row',
                        encode: {
                            itemName: 0,   //数据项名称，在legend中展示
                            value: 1
                        },
                        label: {
                            show: true,
                            formatter: "{b}: {@[1]}分"
                        },
                        emphasis: {
                            label: {
                              position: "outer",  
                              alignTo: "edge",  
                              margin: 30,
                              // position: 'outside',
                              
                                show: false,
                                color: '#484',
                                fontSize: '20',
                                fontWeight: 'bold'
                                // padding: [5, 10]
                            },
                            labelLine: {
						normal: {
							show: false
						}
					},  
          scaleSize:30,
                            // focus: 'series',
                            // blurScope: 'coordinateSystem'
                        },
                        radius: ['40%', '70%']    //设置不同的内外半径
                    }
                ]

        };
      //对饼图进行配置
      chartBox.setOption(option);
      window.addEventListener(
          'resize',
          () => {
            setTimeout(() => {
              chartBox && chartBox.resize()
            }, 100)
          },
          false,
        )

    }
  }


};

</script>


<style>

.unit{
  font-weight: 400;
  font-size: 18px;
  margin-left: 2px;
  margin-bottom: 10px;
}
.arrow,
.change_color{
  color:#60D546 ;
}
.li_item{
  font-family: "gb5";
}
.recommend_allscore{
  display: flex;
  font-family: "walk";
  font-size: 38px;
  color: #666;
  font-weight: 800;
  margin-top: -10px;
  border-bottom: 2.5px solid;
  /*设置线性渐变*/
  border-image: linear-gradient(90deg, rgba(0, 216, 247, 0) 0%, #00afed 100%) 2 2 2 2; 

}
@import "transition-style";
@keyframes circle-swoop {
  from {
    clip-path: var(--circle-top-right-out);
  }
  to {
    clip-path: var(--circle-bottom-right-in);
  }
}

.--in-custom {
  --transition__duration: 2s;
  --transition__easing: ease-in-out;
  animation-name: circle-swoop;
}
@keyframes circle-in-top-left {
  from {
    clip-path: circle(0%);
  }
  to {
    clip-path: circle(150% at top left);
  }
}

[transition-style="in:circle:top-left"] {
  animation: 6s cubic-bezier(.25, 1, .30, 1) circle-in-top-left both;
}
.program{
  display:flex;
  margin:35px 0px;
  /*首先我们设置边框只显示底部，宽度为2px的实线。*/
  border-bottom: 2.5px solid;
  /*设置线性渐变*/
  border-image: linear-gradient(90deg, rgba(0, 216, 247, 0) 0%, #00afed 100%) 2 2 2 2; 


  padding-bottom: 5px;
}

.btn_left{
  border-radius: 10px;
  padding: 0;
  width: 60px;
  height: 30px;
  background: #D4D4D4;  /* fallback for old browsers */


}
.btn_right{
  border-radius: 10px;
  padding: 0;
  width: 60px;
  height: 30px;
  background: #D4D4D4;  /* fallback for old browsers */


}
.program_front{
  display: flex;
  justify-content: space-between;
  width: 280px;
}
  .score .program .program_title{
    font-size: 24px;
    font-weight: bold;
    color: #666;
  }
  .score .program .program_score{
    /*margin-left:50px;*/
    font-size: 20px;
  }

 
</style>