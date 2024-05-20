<template>
  <div class="loginbox" style="text-align: center;" >
    <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="0px" label-height="500px" class="demo-ruleForm" style="width: 40%;position:absolute;top:20%;left:9.5%;transform:translate(50%,50%);">
      <el-form-item>
        <h1>用户登录</h1>
      </el-form-item>

      <el-form-item label="" prop="username">
        <el-input v-model="ruleForm.username" placeholder="请输入用户名"></el-input>
      </el-form-item>

      <el-form-item label="" prop="password">
        <el-input type="password" v-model="ruleForm.password" autocomplete="off" placeholder="请输入密码" ></el-input>
      </el-form-item>


      <el-form-item>
        <el-button type="primary" @click="submitForm('ruleForm')">登录</el-button>
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
        },
        rules: {
          username:[
            // 当组件离开焦点的时候进行验证
            {required:true, message:'请输入用户名',trigger:'blur'}
          ],
          password:[
            {required:true, message:'请输入密码',trigger:'blur'}
          ]
        }
      };
    },
    methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) =>{
          if (valid){
            const _this = this
           
            var data = Qs.stringify({"username":this.ruleForm.username,"password":this.ruleForm.password})
            var data1 =  {username:this.ruleForm.username}
            this.$http.post("/login/",data).then(
              function (resp) {
                const flag = resp.data.request['flag']
                if (flag == 'yes'){
                  // console.log(resp.data.request['flag'])
                 
                  _this.$router.push({path:"/nav",query:data1})
                }else {
                  alert("错误登录")
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
  background:url('../../public/source/6.jpg') no-repeat center center fixed; background-size: 100%;

}

</style>

