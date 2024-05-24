<template>
  <div class="loginbox" style="text-align: center;" >
    <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="0px" label-height="500px" class="demo-ruleForm" style="width: 30%;position:absolute;top:5%;left:47%;transform:translate(50%,50%);">
      <el-form-item>
        <h1>用户注册</h1>
      </el-form-item>

      <el-form-item label="" prop="username">
        <el-input v-model="ruleForm.username" placeholder="请输入用户名"></el-input>
      </el-form-item>

      <el-form-item label="" prop="password">
        <el-input type="password" v-model="ruleForm.password" autocomplete="off" placeholder="请输入密码" ></el-input>
      </el-form-item>
      
      <el-form-item label="" prop="group">
        <el-input type="group" v-model="ruleForm.group" autocomplete="off" placeholder="请输入组别" ></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="submitForm('ruleForm')">注册</el-button>
        <el-button @click="resetForm('ruleForm')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
  import axios from 'axios';
  import Qs from 'qs';
  export default {
    data() {
      return {
        ruleForm: {
          username: '',
          password: '',
          group:'',
        },
        rules: {
          username:[
            // 当组件离开焦点的时候进行验证
            {required:true, message:'请输入用户名',trigger:'blur'}
          ],
          password:[
            {required:true, message:'请输入密码',trigger:'blur'}
          ],
          group:[
            {required:true, message:'请输入组别',trigger:'blur'}
          ]
        }
      };
    },
    methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) =>{
          if (valid){
            const _this = this
            console.log("!!!!!!!!!!")
            console.log(this.ruleForm.group)
            var data = Qs.stringify({"username":this.ruleForm.username,"password":this.ruleForm.password,"group":this.ruleForm.group})
            
            var data1 =  {username:this.ruleForm.username}
            this.$http.post("/signup/",data).then(
              function (resp) {
                const flag = resp.data.request['flag']
                if (flag == 'yes'){
                  // console.log(resp.data.request['flag'])
                 
                  _this.$router.push({path:"/nav",query:data1})
                }else {
                  alert("用户已注册，请先登录。")
                }
              }
            )
            // 开始用的 axios 发送请求
            // console.log(this.ruleForm)
          }else {
            alert("验证错误")
          }
        })
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
    }
  }
</script>
<style>
.loginbox{
  height: 100vh;
  width: 100%;
  background:url('../../public/source/background1.jpg') no-repeat center center fixed; background-size: 100%;

}

</style>

