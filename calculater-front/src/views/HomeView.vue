<template>
  <div class="home" style="margin:0px;display:flex;justify-content:space-around;height:100vh;">
    <!--<img src="../../public/source/project_name.png"  style="position: absolute; left:110px;top:130px; z-index: -1; width: 180px; height: 500px" /> -->
    <!-- <img src="../../public/source/team_name.png"  style="position: absolute; left:10px;top:8px; z-index: -1; width: 240px; height: 60px" /> -->
    <!--<img src="../../public/source/author.png"  style="position: absolute; right:20px;bottom:12px; z-index: -1; width: 260px; height: 60px" /> -->
    <!--<img src="../../public/source/makabaka.gif"  style="position: absolute; right:120px;top:230px; z-index: -1; width: 230px; height: 280px" /> -->
    <img src="../../public/source/background1.jpg"  style="position: absolute; z-index: -10; width: 100%; height: 760px;"  />
    <img src="../../public/source/Sufe.png"  style="position: absolute; right:60px;top:0px; z-index: -1; width: 20%; height: 15%" />
    <div id="d1" class="whole" style="margin:0px;display:flex;justify-content:space-around;" transition-style>
      
      <div class="cal" style="margin-top:60px;border:2px solid #ccc;background:rgba(256,256,256,0.4);opacity:0.9;">
        
        <el-form :model="ruleForm"  ref="ruleForm" label-width="100px" class="demo-ruleForm" >
          <!--
          <div style="margin-top:20px;">
            <el-radio-group v-model="ruleForm.radio1" style="margin-left:120px;width:800px;height:50px" >
              <el-radio-button  label="大一"></el-radio-button>
              <el-radio-button label="大二"></el-radio-button>
              <el-radio-button label="大三"></el-radio-button>
              <el-radio-button label="大四"></el-radio-button>
            </el-radio-group>
          </div> -->
          <div class="sex" style="margin-top: 20px">
            <el-radio-group v-model="ruleForm.sex" size="small" style="margin-left:100px;">
              <el-radio label="男" border>
                <div class="sex_info">
                  <img class="sex_img" src="../../public/source/man.png">
                  <div class="sex_text">男</div>
                </div>
                
              </el-radio>
              <el-radio label="女" border>
                <div class="sex_info">
                  <img class="sex_img" src="../../public/source/woman.png">
                  <div class="sex_text">女</div>
                </div>
                
              </el-radio>
              
  
            </el-radio-group>
          </div>
          <el-row class="enity" v-for="(item,index) in ruleForm.rule_data" :key=item.name>
            <el-form-item :label="ruleForm.sex=='男'?item.name:item.name_f" :prop="'rule_data.' + index + '.value'" :rules="[
              { required: true, message: '成绩不能为空'}
            ]" class="col_left">
              <div class="inputs">
                <el-input class="frame" v-model='item.value'  v-if="item.int_==1"
                oninput="this.value=this.value.replace(/\D/g,'')" onafterpaste="this.value=this.value.replace(/\D/g,'')"  maxLength='9' :placeholder="`请输入${ruleForm.sex=='男'?item.name:item.name_f}成绩`" autocomplete="off"/>
                <el-input class="frame" v-model='item.value'  v-else
                oninput="if(isNaN(value)) { value = null } if(value.indexOf('.')>0){value=value.slice(0,value.indexOf('.')+2)}"   maxLength='9' :placeholder="`请输入${ruleForm.sex=='男'?item.name:item.name_f}成绩`" autocomplete="off"/>
              
                <span class="unit">{{item.unit}}</span>
              </div>
            </el-form-item>
          </el-row>
          <el-row class="enity" :gutter="30" style="margin-left: -15px; margin-right: 0px;width:480px;">
            <el-col :span="15">
              <el-form-item :label="ruleForm.sex=='男'?ruleForm.run_1000.name:ruleForm.run_1000.name_f " prop="run_1000.run_1000_min" :rules="[
              { required: true, message: '成绩不能为空'}
            ]" >
              <div class="inputs">
                <el-input class="frame" v-model='ruleForm.run_1000.run_1000_min' 
                :onkeyup="ruleForm.run_1000.input" :onafterpaste="my_input" maxLength='9' :placeholder="`请输入分钟`" autocomplete="off"/>
              
                <span class="unit">min</span>
              </div>
            </el-form-item>
              </el-col>
            <el-col :span="9" >
              <el-form-item  prop="run_1000.run_1000_sec" :rules="[
              { required: true, message: '成绩不能为空'}
            ]"  class="col_right">
              <div class="inputs">
                <el-input class="frame" v-model='ruleForm.run_1000.run_1000_sec'  size="large"
                onkeyup="this.value=this.value.replace(/\D/g,'')" onafterpaste="this.value=this.value.replace(/\D/g,'')" maxLength='9' :placeholder="`请输入秒数`" autocomplete="off"/>
              
                <span class="unit">s</span>
              </div>
            </el-form-item>
            </el-col>
          </el-row>
          <div>
            <el-form-item >
              <el-button type="primary" @click="submitForm('ruleForm')" style="margin-left:-310px;margin-top:13px;">立即创建</el-button>
              <el-button @click="clear_data" style="margin-left:20px;">重置</el-button>
              <!--<el-button type="primary" @click="go_chat" style="margin-left:-310px;margin-top:13px;">问问机器人</el-button>-->
            </el-form-item> 
          </div>
        </el-form>
      </div> 
      
    </div> 
  </div>
</template>

<script>
// @ is an alias to /src


export default {
  name: 'HomeView',
  mounted () {
    //****
    //对不同屏幕进行适配
    this.bodyScale()
    const t = this.$route.query.refresh
    
    // setInterval(() => {
    //   this.$router.go(0); //一种刷新的方法
    // }, 3000000); //每5分钟自动调用一次
    // this.$router.go(0);
    // if (t) {
    // // 强制刷新页面
    // location.reload()
    // // this.$router.push({path:'/'})
    // }
  },
  watch:{
    watch: {
      $route(to, from) {
      console.log('路由发生变化');
      // 执行其他逻辑处理
      this.$router.go(0)
}
}
  },

  data(){
    
    return {
      ruleForm:{
        rule_data:[
          {
            pro:"weight",
            name:"体重",
            name_f:"体重",
            unit:"kg",
            value:"",
            input:"if(isNaN(value)) { value = null } if(value.indexOf('.')>0){value=value.slice(0,value.indexOf('.')+2)}",
            int_:0
          },
          {
            pro:"height",
            name:"身高",
            name_f:"身高",
            unit:"cm",
            value:"",
            input:"if(isNaN(value)) { value = null } if(value.indexOf('.')>0){value=value.slice(0,value.indexOf('.')+2)}",
            int_:0
          },
          {
            pro:"vital_capacity",
            name:"肺活量",
            name_f:"肺活量",
            unit:"ml",
            value:"",
            input:"this.value=this.value.replace(/\D/g,'')",
            int_:1
          },
          {
            pro:"sit_and_reach",
            name:"坐位体前屈",
            name_f:"坐位体前屈",
            unit:"cm",
            value:"",
            input:"if(isNaN(value)) { value = null } if(value.indexOf('.')>0){value=value.slice(0,value.indexOf('.')+2)}",
            int_:0
          },
          {
            pro:"sit_or_pull",
            pull:'引体向上',
            sit:"仰卧起坐",
            name:"引体向上",
            name_f:"仰卧起坐",
            unit:"个",
            value:"",
            input:"this.value=this.value.replace(/\D/g,'')",
            int_:1
          },
          {
            pro:"run_50",
            name:"50m",
            name_f:"50m",
            unit:"s",
            value:"",
            input:"if(isNaN(value)) { value = null } if(value.indexOf('.')>0){value=value.slice(0,value.indexOf('.')+2)}",
            int_:0
          },
          
          {
            pro:"jump",
            name:"立定跳远",
            name_f:"立定跳远",
            unit:"cm",
            value:"",
            input:"if(isNaN(value)) { value = null } if(value.indexOf('.')>0){value=value.slice(0,value.indexOf('.')+2)}",
            int_:0
          }
          

      ],

        radio1: '大一',
        sex: '男',
        run_1000:{
            name:"1000m",
            name_f:"800m",
            unit1:"min",
            unit2:"s",
            value:"",
            run_1000_min:"",
            run_1000_sec:"",
            input:"this.value=this.value.replace(/\D/g,'')"
        }

      } ,
      input: 'as',
      number:0,
      program:{
        weight:"",
        height:"",
        vital_capacity:"",
        sit_and_reach:"",
        sit_or_pull:"",
        run_50:"",
        run_1000:"",
        run_1000_min:"",
        run_1000_sec:"",
        jump:"",
        
      },
      my_input:"this.value=this.value.replace(/\D/g,'')",
      
      rules: {
          value: [
            { required: true, trigger: ["blur", "change"], message: "请输入成绩" },
            { min: 1, max: 6, message: '长度在 1 到 6 个字符', trigger: 'blur' }
          ]
        },
      result_data:{
        each_score:[],
        all_score:[]
      },
      mal_name:["bmi","肺活量","50m","坐位体前屈","立定跳远","引体向上","1000m"],
      fe_name:["bmi","肺活量","50m","坐位体前屈","立定跳远","仰卧起坐","800m"],
      unit:["","ml",'s','cm','cm','个',''],
      pass_data:{}, //传递的参数
      username:this.$route.query.username,

      
      
    }
  },
  methods: {
   
    bodyScale () {
       //获取当前分辨率下的可是区域宽度
      var devicewidth = document.documentElement.clientWidth
      var scale = devicewidth / 1440// 分母——设计稿的尺寸
      document.body.style.zoom = scale//放大缩小相应倍数
      // alert(scale)
    },

    submitting(value){
        // this.$router.push('/about')
        console.log(value)
      },
      query(){
        console.log(this.program)
      },

      data_process(){
        //对用户输入的数据进行处理
        const weight=parseFloat(this.ruleForm.rule_data[0].value.trim())
        const height=parseInt(this.ruleForm.rule_data[1].value.trim())/100
        const vital_capacity=parseFloat(this.ruleForm.rule_data[2].value.trim())
        const sit_and_reach=parseFloat(this.ruleForm.rule_data[3].value.trim())
        const Pull_ups_and_sit_ups=parseInt(this.ruleForm.rule_data[4].value.trim())
        const run_50=parseFloat(this.ruleForm.rule_data[5].value.trim())
        const jump=parseFloat(this.ruleForm.rule_data[6].value.trim())
        const run_1000_min=parseInt(this.ruleForm.run_1000.run_1000_min.trim())
        const run_1000_sec=parseInt(this.ruleForm.run_1000.run_1000_sec.trim())
        const label=this.ruleForm.radio1+this.ruleForm.sex

        const run_1000=run_1000_min+run_1000_sec/100 //计算一千米的成绩
        const bmi=weight/(height*height) //计算bmi

        const data_pro={
          vital_capacity,
          sit_and_reach,
          Pull_ups_and_sit_ups,
          run_50,
          jump,
          run_1000,
          bmi,
          label
        }
        //获取传递的参数
        this.pass_data=data_pro
        return data_pro

      },
       submitForm(formName) {
        //提交各项成绩
        console.log(this.ruleForm)
        this.$refs[formName].validate((valid) => {
          if (valid) {
            // alert('submit!');
            
          } else {
            console.log('error submit!!');
            return false;
          }
        });
        const data=this.data_process() //获取处理完成的数据
        console.log(data)
        this.getAllScore(data) //获取所有的成绩
      },
      clear_data(){
        //对数据进行清空
        this.ruleForm.rule_data.forEach(item=>{
          item.value=' '
        })
        this.ruleForm.run_1000.run_1000_min=' '
        this.ruleForm.run_1000.run_1000_sec=' '
      },
      go_detail(){
        //跳转到分析的页面
        var div = document.getElementById('d1');
          div.setAttribute("class", "--in-custom whole");
        // console.log(this.result_data)
        username = this.username
        setTimeout(()=>{
          //进行route的push跳转
          this.$router.push({path:'/detail',query: {data:this.result_data,pass_data:this.pass_data,username}})
          
        },2000)
      },
      
      
      async getAllScore(data){
        //调用后端接口，获取各项成绩和总成绩
         await this.$http.get('/data/',{
          params:data
        })
          .then(response =>{
        console.log(response.data)
        const tem_arr=response.data.slice(0,-1)
        const name_arr= this.ruleForm.sex == '男'?this.mal_name:this.fe_name
        tem_arr.forEach((item,index)=>{
          //对数据进行简单的处理，添加需要的数据
          item.name_chin=name_arr[index]
          item.unit=this.unit[index]
        })
        this.result_data.each_score=tem_arr
        const [all]=response.data.slice(-1) //slice方式需要解构获取最后一个值
        this.result_data.all_score=all
        this.go_detail() //跳转到新的页面
        })
        .catch(error =>{
        console.log(error)
        })
        console.log("********")
      }
        
  }
}
</script>


<style>
@import "transition-style";
@keyframes circle-out-bottom-right {
  from {
    clip-path: circle(125%);
  }
  to {
    clip-path: circle(0% at bottom right);
  }
}

@keyframes circle-swoop {
  from {
    clip-path: var(--circle-top-right-out);
  }
  to {
    clip-path: var(--circle-bottom-right-in);
  }
}

.--in-custom {
  --transition__duration: 3s;
  --transition__easing: ease-out;
  animation-name: circle-out-bottom-right;
}
.col_left{
  margin-left: -20px;
}
.col_right{
  margin-left: -120px;
}
.sex .sex_info{
  display: flex;
  justify-content: space-around;
  margin-left: 15px;
  margin-top: -16px;
}
.sex .sex_img{
  width: 15px;
  height: 15px;
  margin-bottom: 20px;
}
.sex .sex_text{
  margin-top: 2px;
  margin-left: 1px;
}

.whole{
  display: flex;
  height:750px;
  width: 1500px;
  /* margin-top: 50px; */
}
.whole .cal {
  width: 38%;
  height: 90%;
  margin: 0 auto;

 /* border: 1px solid #ccc;*/
  border-radius: 20px;
}
.whole .pic{
  width: 300px;
  height: 300px;
  margin: 0 auto;
  background-color: aqua;
}
.whole .cal .enity{
    width: 450px;
    height: 45px;
    margin: 15px 20px;
    border-radius: 10px;
}
.whole .cal .enity .hint{
  font-family: 宋体;
  margin: 3px;
  color: #888;
  font-size: 15px;
}
.whole .cal .enity  .inputs{
  display: flex;
  height: 44px;
}

.whole .cal .enity .inputs .frame{
  margin-right: 8px;
  width: 90%;
}

.whole .cal .enity .inputs .unit{
  
  margin-top: 4px;
  font-size: 18px;
  color: #888;
}
.el-form-item__error{
  margin-top:-4px;
}
</style>