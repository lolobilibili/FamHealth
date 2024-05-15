<template>
<div class="plan">
<el-descriptions title="饮食运动记录" :column="3" border>
  <el-descriptions-item label="预算" label-class-name="my-label" content-class-name="my-content">2200</el-descriptions-item>
  <el-descriptions-item label="饮食">{{breakfast.hot+lunch.hot+dinner.hot+snack.hot}}</el-descriptions-item>
  <el-descriptions-item label="运动*0.9">{{roundToTwoDecimalPlaces(sport.hot*0.9)}}</el-descriptions-item>
  <el-descriptions-item label="还可以旋（千卡）">
    {{-roundToTwoDecimalPlaces(breakfast.hot+lunch.hot+dinner.hot+snack.hot-2200-sport.hot*0.9)}}
  </el-descriptions-item>
  
</el-descriptions>

<el-collapse accordion>
  <el-collapse-item title="早餐">
    <template slot="title">
      早餐<i class="header-icon el-icon-apple"></i>
    </template>
    <div >预计摄入：{{breakfast.hot}}千卡</div>
    <div>准备吃：{{breakfast.des}}</div>
  </el-collapse-item>
  <el-collapse-item title="午餐">
    <template slot="title">
      午餐<i class="header-icon el-icon-burger"></i>
    </template>
    <div>预计摄入：{{lunch.hot}}千卡</div>
    <div>准备吃：{{lunch.des}}</div>
  </el-collapse-item>
  <el-collapse-item title="晚餐">
  <template slot="title">
      晚餐<i class="header-icon el-icon-dish"></i>
    </template>
    <div>预计摄入：{{dinner.hot}}千卡</div>
    <div>准备吃：{{dinner.des}}</div>
    <div>就算白天很累，晚上也要吃饱哦，千万不要亏待自己</div>
  </el-collapse-item>
  <el-collapse-item title="运动">
    <template slot="title">
      运动<i class="header-icon el-icon-bicycle"></i><i class="header-icon el-icon-basketball"></i><i class="header-icon el-icon-soccer"></i>
    </template>
    <div>预计消耗：{{sport.hot}}千卡</div>
    <div>运动计划：{{sport.des}}</div>
    <div class="hahalihai">专家还是建议你少吃，别浪费时间跑步</div>
  </el-collapse-item>
  <el-collapse-item title="夜宵">
    <template slot="title">
      爽吃<i class="header-icon el-icon-platform-eleme"></i>
    </template>
    <div>预计摄入：{{snack.hot}}千卡</div>
    <div class="laobamizhixiaohanbao">嘴里没味er：{{snack.des}}</div>
  </el-collapse-item>
</el-collapse>
<template>
  <div class="block">
    <el-date-picker
      v-model="value1"
      type="date"
      placeholder="选择日期">
    </el-date-picker>
    <el-button type="primary" @click="onSubmit2" round>查看健身信息</el-button>
  </div>
  
</template>



<template>
  <el-form ref="form" :model="form" label-width="80px">
  <el-form-item label="活动名称">
    <el-select v-model="form.name" placeholder="请选择">
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
  </el-form-item>

  <el-form-item label="活动时间">
    <el-col :span="11">
      <el-date-picker type="date" placeholder="选择日期" v-model="form.date" style="width: 100%;"></el-date-picker>
    </el-col>
  </el-form-item>

  <el-form-item label="热量">
    <el-input type="input" v-model="form.input"></el-input>
  </el-form-item>
  <el-form-item label="描述">
    <el-input type="textarea" v-model="form.desc" :rows="2"
  placeholder="（描述）例：荷包蛋*2 117千卡/个，苹果*1 97千卡/个，打胶*9999 0千卡/次" style="width:500px"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="onSubmit">立即更新运动信息</el-button>
    <el-button>取消</el-button>
  </el-form-item>
</el-form>
</template>

</div>


</template>

<script>

export default {
  created(){
    
  },
  data() {
      return {
        pickerOptions: {
          disabledDate(time) {
            return time.getTime() > Date.now();
          },
          
        },
        options: [{
          value: '1',
          label: '早饭'
        }, {
          value: '2',
          label: '中饭'
        }, {
          value: '3',
          label: '晚饭'
        }, {
          value: '4',
          label: '夜宵'
        }, {
          value: '5',
          label: '运动'
        }],

        value1: new Date(),
        breakfast:{},
        lunch:{},
        dinner:{},
        snack:{},
        sport:{},
        form: {
          name: '',

          date: '',


          desc: '',
          input:''
        }
      };
    },
  mounted(){
    this.onSubmit2()
  },
    methods:{
      
      async onSubmit(){
        
         await this.$http.get('/submit/',{
          params:this.form
        })
          .then(response =>{
        console.log(response.data)
   
        })
        .catch(error =>{
        console.log(error)
        })
        console.log("********")
      },
      async onSubmit2(){
        console.log(this.value1)
         await this.$http.get('/submit2/',{
          params:{date:this.value1}
        })
          .then(response =>{
        console.log(response.request.status)
        console.log(response.data[0])
        this.breakfast = response.data[0]
        this.lunch = response.data[1]
        this.dinner = response.data[2]
        this.snack = response.data[3]
        this.sport = response.data[4]

   
        })
        .catch(error =>{
        console.log(error)
        })
        console.log("********")
       },
    //    getNextDay(d){
    // d = new Date(d);
    // d = +d - 1000*60*60*24;
    // d = new Date(d);
    // //return d;
    // //格式化
    // return d.getFullYear()+"-"+(d.getMonth()+1)+"-"+d.getDate();     
    // },
      roundToTwoDecimalPlaces(num) {
      return parseFloat(num.toFixed(2));
    },




    }
}
</script>

<style>
.el-input{
  width: 100px;
  color: aqua;
}
.hahalihai{
  color: aqua;
}
.laobamizhixiaohanbao{
  color: violet;
}
</style>