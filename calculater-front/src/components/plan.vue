<template>
<div class="plan">

<div>
  <div class="block">
    <el-date-picker
      v-model="value1"
      type="date"
      placeholder="选择日期"
      value-format="yyyy-MM-dd"
      >
    </el-date-picker>

    <el-button type="primary" @click="onSubmit2" round style="margin-left:10px;">查看健身信息</el-button>

    <div id="app" class="container" style="margin-top:20px;">
      <div class="top-section">
          <el-card class="top-card">
            <div style="display: flex;justify-content: space-between;">
              <div>
                <h3>身高和体重</h3>
                <p>身高: {{ body.height }}cm</p>
                <p>体重: {{ body.weight }}kg</p>
              </div>
              <div >
                <img src="../../public/source/meimei.jpg" style="width:80px;height:110px;" >
              </div>
            </div>
          </el-card>
          <el-card class="top-card " style="background-color:rgba(240,251,247,1);">
              <div class="cal">
                <div class="cal-remain">
                  <div class="cal-text">还可吃(千卡)</div>
                  <div class="cal-all-num">{{ 2222 - this.hot.all_food + 0.9*this.hot.sport}}</div>
                </div>
                <div class="cal-sign" style="margin-right:2px;">=</div>
                <div class="cal-box">
                  <div class="cal-text">预算</div>
                  <div class="cal-num">2222</div>
                </div>
                <div class="cal-sign">-</div>
                <div class="cal-box">
                  <div class="cal-text">饮食</div>
                  <div class="cal-num">{{ this.hot.all_food }}</div>
                </div>
                <div class="cal-sign">+</div>
                <div class="cal-box">
                  <div class="cal-text">运动*0.9</div>
                  <div class="cal-num">{{ this.hot.sport }}</div>
                </div>
              </div>
              <!-- <h3>卡路里记录</h3>
              <p>已消耗: 500kcal</p>
              <p>目标消耗: 2000kcal</p>
              <p>剩余消耗: 1500kcal</p> -->
          </el-card>
      </div>
      <div class="meal-cards" >
        
          <el-card class="meal-card breakfast" >
            <div @click="editMeal({name:1,zhongwen:'早餐'})">
              <h3>早餐</h3>
              <p>内容: {{ breakfast.des }}</p>
              <p>数量: {{ breakfast.hot }}kcal</p>
            </div>
            
           </el-card>



          <el-card class="meal-card lunch" >
            <div @click="editMeal({name:2,zhongwen:'中饭'})">

              <h3>中饭</h3>
              <p>内容: {{ lunch.des }}</p>
              <p>数量: {{ lunch.hot }}kcal</p>
            </div>
          </el-card>

          
          
          <el-card class="meal-card dinner"  >
              <div @click="editMeal({name:3,zhongwen:'晚饭'})">
                <h3>晚饭</h3>
                <p>内容: {{ dinner.des }}</p>
                <p>数量: {{ dinner.hot }}kcal</p>
              </div>
          </el-card>
          <el-card class="meal-card snack" >
              <div @click="editMeal({name:4,zhongwen:'夜宵'})" >
                <h3>夜宵</h3>
                <p>内容: {{ snack.des }}</p>
                <p>数量: {{ snack.hot }}kcal</p>
              </div>
          </el-card>
      </div>
      <div class="meal-cards" >
      
        <el-card class="exercise-card " >
          <div @click="add_sport()">
            <div style="display:flex;justify-content:space-between">
              <div style="margin-top:12px; font-size:22px;"> 运动记录 </div>
              <div style="margin-right:30px;margin-bottom:18px;display:flex;justify-content:space-between"> 
                <span style="margin-top: 14px;">共消耗</span>
                <span style="font-weight:bold;font-size:34px;margin:2px 0px 5px 10px;">{{ sport.hot }}</span>
              </div>
            </div>
            <!-- <p>{{ sport.des }}</p> -->
          <div v-for="item in sport.des" :key="item">
            
              <p><span class="el-icon-check"></span>{{ item }}</p>

            
          </div>
          </div>

      </el-card>
      <el-card class="meal-card " style="background-color: #f2f4f4;">
        <el-carousel indicator-position="outside" type="card" style="height:170px;margin-top:10px;" >
          <el-carousel-item v-for="item in imgArray" :key="item.img">
            <div style="text-align: center;width:150px;height:120px;position:relative" @click="go_eat_plan(item.name)">
              <img :src="item.img" class="rightImg" >
              <span class="overlay-text">{{ item.name }}</span>
            </div>
          </el-carousel-item>
        </el-carousel>
        
    </el-card>
      </div>

      <!-- 弹窗 -->
      <!-- 弹窗 -->
      <el-dialog :visible.sync="dialogVisible" :title="'编辑'+ this.form.zhongwen" width="30%">

        <el-form ref="form" :model="form" >
          <!-- <el-form-item label="活动名称">
            <el-select v-model="form.name" placeholder="请选择">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>  
          </el-form-item> -->
        
          <el-form-item label="时间">
            <el-col :span="11">
              <el-date-picker type="date" placeholder="选择日期" v-model="form.date" style="width: 100%;" value-format="yyyy-MM-dd"></el-date-picker>
            </el-col>
          </el-form-item>
        
          <el-form-item label="热量">
            <el-input type="input" v-model="form.input" style="width: 46%;"></el-input><span style="margin: 5px;">kcal</span>
          </el-form-item>
          <el-form-item label="描述">
            <el-input type="textarea" v-model="form.desc" :rows="2"
          placeholder="（描述）例：荷包蛋*2 117千卡/个，苹果*1 97千卡/个，打胶*9999 0千卡/次" style="width:100%"></el-input>
          </el-form-item>
          <el-form-item style="text-align:center;">
            <el-button type="primary" @click="onSubmit" >立即更新</el-button>
            <el-button>取消</el-button>
          </el-form-item>
        </el-form>
      </el-dialog>
  </div>

  </div>

  
</div>




<!-- <el-form ref="form" :model="form" label-width="80px">
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
</el-form> -->






<el-dialog :visible.sync="plan_visible"  width="30%">
  <div id="app2">
    <div class="card">
        <div class="header">
            <h1>{{ activePlan }}菜单</h1>
        </div>
        <div class="content">
            <!-- <div class="tabs">
                <button v-for="plan in Object.keys(plans)" :key="plan" @click="setActivePlan(plan)" :class="{ active: activePlan === plan }">{{ plan }}</button>
            </div> -->
            <div class="tabs">
                <button v-for="day in 7" :key="day" @click="setActiveDay(day)" :class="{ active: activeDay === day }">第{{ day }}天</button>
            </div>
            <div class="meals">
                <div class="meal" v-for="(meals, mealType) in plans[activePlan][activeDay]" :key="mealType">
                    <h3>{{ mealType }}</h3>
                    <ul>
                        <li v-for="meal in meals" :key="meal">{{ meal }}</li>
                    </ul>
                </div>
            </div>
        </div>
        <!-- <div class="footer">
            <button class="use-plan-btn">使用此食谱</button>
        </div> -->
    </div>
  </div>
</el-dialog>


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
        imgArray: [
        {name:"减脂",img:require('../../public/source/eat/1.png')},
        {name:"高蛋白增肌",img:require('../../public/source/eat/2.png')},
        {name:"低碳水减重",img:require('../../public/source/eat/3.png')},

      ],
        dialogVisible: false,
        currentMeal: {
                    content: '',
                    amount: ''
                },
        activeDay: 1,
        activePlan: '减脂',
        plan_visible:false,
        plans: {
            '减脂': {
                1: {
                    breakfast: ['牛奶 - 约250克', '水煮鸡蛋 - 约60克', '红豆粥 - 约120克'],
                    lunch: ['杂粮饭 - 约180克', '白灼西兰花虾仁 - 约200克', '照烧鸡腿 - 约180克'],
                    dinner: ['糙米饭 - 约150克', '蒸鱼 - 约200克', '蔬菜沙拉 - 约100克'],
                    snack: ['苹果 - 约100克']
                },
                2: {
                    breakfast: ['豆浆 - 约300克', '全麦面包 - 约50克', '水果沙拉 - 约150克'],
                    lunch: ['糙米饭 - 约200克', '清蒸鸡胸肉 - 约150克', '蔬菜沙拉 - 约100克'],
                    dinner: ['红薯 - 约150克', '烤鱼 - 约200克', '菠菜 - 约100克'],
                    snack: ['香蕉 - 约100克']
                },
                3: {
                    breakfast: ['酸奶 - 约200克', '鸡蛋饼 - 约100克', '水果 - 约150克'],
                    lunch: ['红豆饭 - 约180克', '蒸鱼 - 约200克', '蔬菜 - 约100克'],
                    dinner: ['杂粮粥 - 约150克', '烤鸡胸肉 - 约200克', '花椰菜 - 约100克'],
                    snack: ['坚果 - 约30克']
                },
                4: {
                    breakfast: ['燕麦片 - 约200克', '牛奶 - 约250克', '苹果 - 约100克'],
                    lunch: ['糙米饭 - 约180克', '烤鱼 - 约200克', '生菜沙拉 - 约100克'],
                    dinner: ['红薯 - 约150克', '鸡胸肉 - 约200克', '蔬菜沙拉 - 约100克'],
                    snack: ['橙子 - 约100克']
                },
                5: {
                    breakfast: ['酸奶 - 约200克', '煎鸡蛋 - 约100克', '水果 - 约150克'],
                    lunch: ['红豆饭 - 约180克', '蒸鱼 - 约200克', '蔬菜 - 约100克'],
                    dinner: ['杂粮粥 - 约150克', '烤鸡胸肉 - 约200克', '花椰菜 - 约100克'],
                    snack: ['水果 - 约100克']
                },
                6: {
                    breakfast: ['豆浆 - 约300克', '全麦面包 - 约50克', '水果沙拉 - 约150克'],
                    lunch: ['糙米饭 - 约200克', '清蒸鸡胸肉 - 约150克', '蔬菜沙拉 - 约100克'],
                    dinner: ['红薯 - 约150克', '烤鱼 - 约200克', '菠菜 - 约100克'],
                    snack: ['香蕉 - 约100克']
                },
                7: {
                    breakfast: ['酸奶 - 约200克', '鸡蛋饼 - 约100克', '水果 - 约150克'],
                    lunch: ['红豆饭 - 约180克', '蒸鱼 - 约200克', '蔬菜 - 约100克'],
                    dinner: ['杂粮粥 - 约150克', '烤鸡胸肉 - 约200克', '花椰菜 - 约100克'],
                    snack: ['坚果 - 约30克']
                }
            },
            '高蛋白增肌': {
                1: {
                    breakfast: ['蛋白粉奶昔 - 约300克', '水煮鸡蛋 - 约60克', '香蕉 - 约100克'],
                    lunch: ['糙米饭 - 约200克', '煎鸡胸肉 - 约200克', '花椰菜 - 约100克'],
                    dinner: ['红薯 - 约150克', '烤鱼 - 约200克', '菠菜 - 约100克'],
                    snack: ['坚果 - 约30克']
                },
                2: {
                    breakfast: ['燕麦片 - 约200克', '牛奶 - 约250克', '苹果 - 约100克'],
                    lunch: ['糙米饭 - 约180克', '烤鸡胸肉 - 约200克', '生菜沙拉 - 约100克'],
                    dinner: ['红薯 - 约150克', '煎鱼 - 约200克', '胡萝卜 - 约100克'],
                    snack: ['蛋白棒 - 1根']
                },
                3: {
                    breakfast: ['蛋白粉奶昔 - 约300克', '水煮鸡蛋 - 约60克', '蓝莓 - 约100克'],
                    lunch: ['糙米饭 - 约200克', '烤鸡胸肉 - 约200克', '蔬菜沙拉 - 约100克'],
                    dinner: ['红薯 - 约150克', '烤鱼 - 约200克', '菠菜 - 约100克'],
                    snack: ['蛋白棒 - 1根']
                },
                4: {
                    breakfast: ['酸奶 - 约200克', '鸡蛋饼 - 约100克', '水果 - 约150克'],
                    lunch: ['糙米饭 - 约180克', '蒸鱼 - 约200克', '蔬菜 - 约100克'],
                    dinner: ['杂粮粥 - 约150克', '烤鸡胸肉 - 约200克', '花椰菜 - 约100克'],
                    snack: ['坚果 - 约30克']
                },
                5: {
                    breakfast: ['蛋白粉奶昔 - 约300克', '水煮鸡蛋 - 约60克', '香蕉 - 约100克'],
                    lunch: ['糙米饭 - 约200克', '煎鸡胸肉 - 约200克', '花椰菜 - 约100克'],
                    dinner: ['红薯 - 约150克', '烤鱼 - 约200克', '菠菜 - 约100克'],
                    snack: ['坚果 - 约30克']
                },
                6: {
                    breakfast: ['燕麦片 - 约200克', '牛奶 - 约250克', '苹果 - 约100克'],
                    lunch: ['糙米饭 - 约180克', '烤鸡胸肉 - 约200克', '生菜沙拉 - 约100克'],
                    dinner: ['红薯 - 约150克', '煎鱼 - 约200克', '胡萝卜 - 约100克'],
                    snack: ['蛋白棒 - 1根']
                },
                7: {
                    breakfast: ['酸奶 - 约200克', '鸡蛋饼 - 约100克', '水果 - 约150克'],
                    lunch: ['糙米饭 - 约180克', '蒸鱼 - 约200克', '蔬菜 - 约100克'],
                    dinner: ['杂粮粥 - 约150克', '烤鸡胸肉 - 约200克', '花椰菜 - 约100克'],
                    snack: ['坚果 - 约30克']
                }
            },
            '低碳水减重': {
                1: {
                    breakfast: ['牛油果沙拉 - 约200克', '水煮鸡蛋 - 约60克', '杏仁 - 约30克'],
                    lunch: ['烤鸡胸肉 - 约200克', '生菜沙拉 - 约100克', '黄瓜 - 约100克'],
                    dinner: ['牛排 - 约200克', '西兰花 - 约100克', '菠菜 - 约100克'],
                    snack: ['核桃 - 约30克']
                },
                2: {
                    breakfast: ['希腊酸奶 - 约200克', '浆果 - 约100克', '坚果 - 约30克'],
                    lunch: ['烤鸡胸肉 - 约200克', '菠菜沙拉 - 约100克', '黄瓜 - 约100克'],
                    dinner: ['三文鱼 - 约200克', '花椰菜 - 约100克', '菠菜 - 约100克'],
                    snack: ['橄榄 - 约30克']
                },
                3: {
                    breakfast: ['牛油果沙拉 - 约200克', '水煮鸡蛋 - 约60克', '杏仁 - 约30克'],
                    lunch: ['烤鸡胸肉 - 约200克', '生菜沙拉 - 约100克', '黄瓜 - 约100克'],
                    dinner: ['牛排 - 约200克', '西兰花 - 约100克', '菠菜 - 约100克'],
                    snack: ['核桃 - 约30克']
                },
                4: {
                    breakfast: ['希腊酸奶 - 约200克', '浆果 - 约100克', '坚果 - 约30克'],
                    lunch: ['烤鸡胸肉 - 约200克', '菠菜沙拉 - 约100克', '黄瓜 - 约100克'],
                    dinner: ['三文鱼 - 约200克', '花椰菜 - 约100克', '菠菜 - 约100克'],
                    snack: ['橄榄 - 约30克']
                },
                5: {
                    breakfast: ['牛油果沙拉 - 约200克', '水煮鸡蛋 - 约60克', '杏仁 - 约30克'],
                    lunch: ['烤鸡胸肉 - 约200克', '生菜沙拉 - 约100克', '黄瓜 - 约100克'],
                    dinner: ['牛排 - 约200克', '西兰花 - 约100克', '菠菜 - 约100克'],
                    snack: ['核桃 - 约30克']
                },
                6: {
                    breakfast: ['希腊酸奶 - 约200克', '浆果 - 约100克', '坚果 - 约30克'],
                    lunch: ['烤鸡胸肉 - 约200克', '菠菜沙拉 - 约100克', '黄瓜 - 约100克'],
                    dinner: ['三文鱼 - 约200克', '花椰菜 - 约100克', '菠菜 - 约100克'],
                    snack: ['橄榄 - 约30克']
                },
                7: {
                    breakfast: ['牛油果沙拉 - 约200克', '水煮鸡蛋 - 约60克', '杏仁 - 约30克'],
                    lunch: ['烤鸡胸肉 - 约200克', '生菜沙拉 - 约100克', '黄瓜 - 约100克'],
                    dinner: ['牛排 - 约200克', '西兰花 - 约100克', '菠菜 - 约100克'],
                    snack: ['核桃 - 约30克']
                }
            }
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

        value1: null,
        breakfast:{},
        lunch:{},
        dinner:{},
        snack:{},
        sport:{},
        body:{},
        form: {
          zhongwen:'',
          name: '',

          date: '',


          desc: '',
          input:'',
          username:this.$route.query.username
        },
        hot:{},
      };
    },
  mounted(){
    this.value1=this.formatDate(new Date(new Date(new Date().toLocaleDateString()).getTime()))
    // this.value1=new Date(new Date(new Date().toLocaleDateString()).getTime())
    this.onSubmit2()
    this.get_data_by_username(this.form.username)
  },
    methods:{
      add_sport(){
        // console.log(meal)
         this.form.name='5'
         this.form.zhongwen='运动'
          // this.currentMeal = Object.assign({}, this.meals[meal]);
          this.dialogVisible = true;
      },
      go_eat_plan(name){
        this.plan_visible=true;
        this.activePlan=name;

      },
      setActiveDay(day) {
            this.activeDay = day;
        },
        setActivePlan() {
            // this.activePlan = plan;
            this.activeDay = 1;
            this.plan_visible=true;
        },
      async get_data_by_username(username) {
      await this.$http
        .get("/get_user_data/", {
          params: { username: username },
        })
        .then((response) => {
          console.log(response.data);
          this.body.weight=parseFloat(response.data[0].weight)
          this.body.height=parseFloat(response.data[0].height)*100
        })
        .catch((error) => {
          console.log(error);
        });
    },
      formatDate(date) {
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0'); // 月份从0开始，所以要加1
        const day = String(date.getDate()).padStart(2, '0');

        return `${year}-${month}-${day}`;
      },
      editMeal(meal) {
         console.log(meal)
         this.form.name=meal.name
         this.form.zhongwen=meal.zhongwen
          // this.currentMeal = Object.assign({}, this.meals[meal]);
          this.dialogVisible = true;
      },
      saveMeal() {
          // 保存逻辑（这里只是示例，可以自行实现）
          this.dialogVisible = false;
      },
      async onSubmit(){
        this.dialogVisible = false
        if(this.form.name=='5'  && this.form.date==this.value1){
          if(this.sport.hot==0){
            this.sport.des=[this.form.desc]
          }
          else{
            this.sport.des.push(this.form.desc)
          }
          
          this.form.desc=this.sport.des.join('|')
          console.log(this.form.desc)

          this.sport.hot+=parseInt(this.form.input)
        }
        else if(this.form.name=='1' && this.form.date==this.value1){
          this.breakfast.hot=this.form.input
          this.breakfast.des=this.form.desc
        }
        else if(this.form.name=='2' && this.form.date==this.value1){
          this.lunch.hot=this.form.input
          this.lunch.des=this.form.desc
        }
        else if(this.form.name=='3' && this.form.date==this.value1){
          this.dinner.hot=this.form.input
          this.dinner.des=this.form.desc
        }
        else if(this.form.name=='4' && this.form.date==this.value1){
          this.snack.hot=this.form.input
          this.snack.des=this.form.desc
        }
        this.hot.all_food=parseInt(this.breakfast.hot)+parseInt(this.lunch.hot)+parseInt(this.dinner.hot)+parseInt(this.snack.hot)
          
        
        this.hot.sport=this.sport.hot
         await this.$http.get('/submit/',{
          params:this.form
        })
          .then(response =>{
        console.log(response.data)
        this.form.desc="";
        this.form.input=""
        })
        .catch(error =>{
        console.log(error)
        })
        console.log("********")
      },
      async onSubmit2(){
        console.log(this.value1,new Date(this.value1))
         await this.$http.get('/submit2/',{
          // params:{date:new Date(this.value1),username:this.form.username}
          params:{date:this.value1,username:this.form.username}
        })
          .then(response =>{
        console.log(response.request.status)
        console.log(response.data[0])
        this.breakfast = response.data[0]
        this.lunch = response.data[1]
        this.dinner = response.data[2]
        this.snack = response.data[3]
        this.sport = response.data[4]
        this.hot.all_food=this.breakfast.hot+this.lunch.hot+this.dinner.hot+this.snack.hot
        this.hot.sport=this.sport.hot

        let result = response.data[4].des.split('|');
        this.sport.des=result
        
        this.form.date=this.value1
   
        })
        .catch(error =>{
        console.log(error)
        })
        // console.log("********")
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
body {
  margin: 20px;
  font-family: Arial, sans-serif;
  background-color: #f5f5f5;
}
.container {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.top-section {
  display: flex;
  justify-content: space-between;
  gap: 20px;
}
.top-card {
  flex: 1;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  background-color: #ffffff;
}
.top-card h3 {
  margin-bottom: 15px;
  font-size: 1.2em;
  color: #333;
}
.top-card p {
  margin: 5px 0;
  font-size: 1em;
  color: #555;
}
.cal{
  margin-top: 20px;
  display: flex;
  justify-content: space-between;

}
.cal-text{
  font-size: 18px;
  color: #888;
}
.cal-all-num{
  margin-top: 0px;
  font-weight: 600;
  color: #333;
  font-size: 32px;
}
.cal-num{
  margin-top: 10px;
  /**font-weight: 600;**/
  color: #333;
  font-size: 20px;
  text-align: center;
}
.cal-sign{
  margin:32px 0px 0px 0px;
  font-size: 18px;
}
.meal-cards {
  display: flex;
  justify-content: space-between;
  gap: 20px;
}
.meal-card, .exercise-card {
  flex: 1;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  color: white;
}
.meal-card h3,
.exercise-card h3 {
  margin-bottom: 10px;
  font-size: 1.2em;
}
.meal-card p,
.exercise-card p {
  margin: 5px 0;
  font-size: 1em;
}
.meal-card.breakfast {
  background-color: #7cc6d8;
  opacity: 0.7;
}
.meal-card.lunch {
  background-color: #ff9800;
  opacity: 0.7;
}
.meal-card.dinner {
  background-color: #f44336;
  opacity: 0.7;
}
.meal-card.snack {
  background-color: #aa66d2; 
  opacity: 0.7;
}
.exercise-card {
  background-color: #4caf50;
}
.dialog-footer {
  text-align: right;
}


.container2 {
  max-width: 600px;
  width: 100%;
  background-color: white;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  border-radius: 15px;
  overflow: hidden;
}

.header {
  position: relative;
}

.header-image {
  width: 100%;
  height: auto;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
}

.header-info {
  position: absolute;
  bottom: 10px;
  left: 10px;
  right: 10px;
  color: white;
  background: rgba(0, 0, 0, 0.5);
  padding: 15px;
  border-radius: 10px;
  backdrop-filter: blur(5px);
}

.header-info h1 {
  margin-bottom: 10px;
}

.header-stats {
  display: flex;
  justify-content: space-between;
}

.stat {
  text-align: center;
}

.stat p {
  font-size: 24px;
  margin: 0;
}

.stat span {
  font-size: 12px;
}

.summary {
  padding: 20px;
  border-bottom: 1px solid #eee;
}

.details-link {
  color: #4CAF50;
  text-decoration: none;
  font-weight: bold;
}

.details-link:hover {
  text-decoration: underline;
}

.content {
  padding: 20px;
}

.tabs {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.tabs button {
  flex: 1;
  padding: 10px 0;
  border: none;
  background: #f0f0f0;
  color: #333;
  cursor: pointer;
  transition: background 0.3s;
}

.tabs button.active {
  background: #4CAF50;
  color: white;
}

.tabs button:not(:last-child) {
  border-right: 1px solid #ddd;
}

.meals .meal {
  background: #f7f7f7;
  padding: 10px;
  border-radius: 10px;
  margin-bottom: 10px;
  border: 1px solid #ddd;
}

.meals .meal h3 {
  margin-bottom: 10px;
  color: #4CAF50;
}

.meals .meal ul {
  list-style: none;
}

.meals .meal ul li {
  padding: 5px 0;
  border-bottom: 1px solid #eee;
}

.meals .meal ul li:last-child {
  border-bottom: none;
}

.footer {
  padding: 20px;
  border-top: 1px solid #eee;
  text-align: center;
  background-color: #f5f5f5;
  border-bottom-left-radius: 15px;
  border-bottom-right-radius: 15px;
}

.use-plan-btn {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.use-plan-btn:hover, .use-plan-btn:focus {
  background-color: #388E3C;
}



.card {
  background: white;
  border-radius: 15px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  max-width: 600px;
  margin: 0 auto;
}

.header {
  background: #4CAF50;
  color: white;
  padding: 20px;
  text-align: center;
  border-bottom: 1px solid #eee;
}

.header h1 {
  margin: 0;
}

.content {
  padding: 20px;
}

.tabs {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.tabs button {
  flex: 1;
  padding: 10px 0;
  border: none;
  background: #f0f0f0;
  color: #333;
  cursor: pointer;
  transition: background 0.3s;
}

.tabs button.active {
  background: #4CAF50;
  color: white;
}

.tabs button:not(:last-child) {
  border-right: 1px solid #ddd;
}

.meals .meal {
  background: #f7f7f7;
  padding: 10px;
  border-radius: 10px;
  margin-bottom: 10px;
  border: 1px solid #ddd;
}

.meals .meal h3 {
  margin-bottom: 10px;
  color: #4CAF50;
}

.meals .meal ul {
  list-style: none;
  padding: 0;
}

.meals .meal ul li {
  padding: 5px 0;
  border-bottom: 1px solid #eee;
}

.meals .meal ul li:last-child {
  border-bottom: none;
}

.footer {
  padding: 20px;
  border-top: 1px solid #eee;
  text-align: center;
  background-color: #f5f5f5;
  border-bottom-left-radius: 15px;
  border-bottom-right-radius: 15px;
}

.use-plan-btn {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.use-plan-btn:hover, .use-plan-btn:focus {
  background-color: #388E3C;
}

.rightImg {
  width: 200%;
  height: 120%;
}

.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 120px;
  margin: 0;
}
.el-carousel__container{
  height:143px;
  width:600px;
}

  .el-carousel__mask{
    height: 100px;
  }

  .overlay-text{
    position: absolute;
    top: 55%;
    left: 95%;
    transform: translate(-50%, -50%);
    color: white;
    font-size: 24px;
    font-weight: bold;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.6);
    white-space: nowrap;
  }
</style>