<script>

export default{
  data(){
    return {
      ruleForm:{
        rule_data:[
          {
            pro:"weight",
            name:"体重",
            name_f:"体重",
            unit:"kg",
            value:null,
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
            name:"座位体前屈",
            name_f:"座位体前屈",
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
      
      
      
    }
  },
  mounted(){
    document.title = "体测小助手"
  },
  methods: {
    submitting(value){
        // this.$router.push('/about')
        console.log(value)
      },
      query(){
        console.log(this.program)
      },
      onSubmit(){
        
      },
      data_process(){
        //对用户输入的数据进行处理
        const weight=parseFloat(this.ruleForm.rule_data[0].value)
        const height=parseInt(this.ruleForm.rule_data[1].value)/100
        const vital_capacity=parseFloat(this.ruleForm.rule_data[2].value)
        const sit_and_reach=parseFloat(this.ruleForm.rule_data[3].value)
        const Pull_ups_and_sit_ups=parseInt(this.ruleForm.rule_data[4].value)
        const run_50=parseFloat(this.ruleForm.rule_data[5].value)
        const jump=parseFloat(this.ruleForm.rule_data[6].value)
        const run_1000_min=parseInt(this.ruleForm.run_1000.run_1000_min)
        const run_1000_sec=parseInt(this.ruleForm.run_1000.run_1000_sec)


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
        }
        return data_pro

      },
       submitForm(formName) {
        
        console.log(this.ruleForm)
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('submit!');
            
          } else {
            console.log('error submit!!');
            return false;
          }
        });
        const data=this.data_process()
        console.log(data)
        this.getAllScore(data)
      },
      
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
      async getAllScore(data){
         await this.$http.get('/api/data/',{
          params:data
        })
          .then(response =>{
        console.log(response.data)
        })
        .catch(error =>{
        console.log(error)
        })
        console.log("********")
      }
        
  }
  

}

</script>



<template>
  <div id="app" style="margin:0px;">
  <link rel="icon" href="../public/source/logo.webp">
    <router-view/>
    <!-- <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav> -->
    

    <!-- <router-view/> -->
  </div>
</template>

<style>
* {
  margin: 0;
  padding: 0;
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
  /*margin-top: 50px;*/
}
.whole .cal {
  width: 600px;
  height: 800px;
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>



