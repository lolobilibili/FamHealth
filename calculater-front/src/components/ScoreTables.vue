<template>
  <el-table
    :data="tableData"
    :cell-style="{ 'text-align': 'center','font-size':'16px' }" 
    :header-cell-style="{ 
    color: '$ffffff', 
           
    'text-align': 'center',
    }" 
    :span-method="objectSpanMethod"           
    max-height="600"
    style="width: 100%">
    <el-table-column
      prop="grade"
      label="等级"
      width="60">
    </el-table-column>
    
      <el-table-column
        prop="score"
        label="单项得分"
        width="80">
      </el-table-column>
      <el-table-column label="大学男生">
        <el-table-column
          prop="rate1"
          label="大一 大二"
          width="120">
        </el-table-column>
        <el-table-column
          prop="rate2"
          label="大三 大四"
          width="120">
        </el-table-column>
      </el-table-column>
      <el-table-column label="大学女生">  
        <el-table-column
          prop="rate3"
          label="大一大二"
          width="120">
        </el-table-column>
        <el-table-column
          prop="rate4"
          label="大三大四"
          width="120">
        </el-table-column>
      </el-table-column>

  </el-table>

</template>

<script>
  export default {
    data() {
      return {
        tableData: [{
          grade: '占比',
          score: '20%',
          rate1: "耐力跑",
          rate2: "耐力跑",
          rate3: "耐力跑",
          rate4: "耐力跑"
        }, {
          grade: '优秀',
          score: '100',
          rate1: "3\'17\"",
          rate2: "3\'15\"",
          rate3: "3\'18\"",
          rate4: "3\'16\""
        },{
          grade: '优秀',
          score: '95',
          rate1: "3\'22\"",
          rate2: "3\'20\"",
          rate3: "3\'24\"",
          rate4: "3\'22\""
        },{
          grade: '优秀',
          score: '90',
          rate1: "3\'27\"",
          rate2: "3\'35\"",
          rate3: "3\'30\"",
          rate4: "3\'28\""
        },{
          grade: '良好',
          score: '85',
          rate1: "3\'34\"",
          rate2: "3\'32\"",
          rate3: "3\'37\"",
          rate4: "3\'35\""
        },{
          grade: '良好',
          score: '80',
          rate1: "3\'42\"",
          rate2: "3\'40\"",
          rate3: "3\'44\"",
          rate4: "3\'42\""
        },{
          grade: '及格',
          score: '78',
          rate1: "3\'47\"",
          rate2: "3\'45\"",
          rate3: "3\'49\"",
          rate4: "3\'47\""
        },{
          grade: '及格',
          score: '76',
          rate1: "3\'52\"",
          rate2: "3\'50\"",
          rate3: "3\'54\"",
          rate4: "3\'52\""
        },{
          grade: '及格',
          score: '74',
          rate1: "3\'57\"",
          rate2: "3\'55\"",
          rate3: "3\'59\"",
          rate4: "3\'57\""
        },{
          grade: '及格',
          score: '72',
          rate1: "4\'02\"",
          rate2: "4\'00\"",
          rate3: "4\'04\"",
          rate4: "4\'02\""
        },{
          grade: '及格',
          score: '70',
          rate1: "4\'07\"",
          rate2: "4\'05\"",
          rate3: "4\'09\"",
          rate4: "4\'07\""
        },{
          grade: '及格',
          score: '68',
          rate1: "4\'12\"",
          rate2: "4\'10\"",
          rate3: "4\'14\"",
          rate4: "4\'12\""
        },{
          grade: '及格',
          score: '66',
          rate1: "4\'17\"",
          rate2: "4\'15\"",
          rate3: "4\'19\"",
          rate4: "4\'17\""
        },{
          grade: '及格',
          score: '64',
          rate1: "4\'22\"",
          rate2: "4\'20\"",
          rate3: "4\'24\"",
          rate4: "4\'22\""
        },{
          grade: '及格',
          score: '62',
          rate1: "4\'27\"",
          rate2: "4\'25\"",
          rate3: "4\'29\"",
          rate4: "4\'27\""
        },{
          grade: '及格',
          score: '60',
          rate1: "4\'32\"",
          rate2: "4\'30\"",
          rate3: "4\'34\"",
          rate4: "4\'32\""
        },{
          grade: '不及格',
          score: '50',
          rate1: "4\'52\"",
          rate2: "4\'50\"",
          rate3: "4\'44\"",
          rate4: "4\'42\""
        },{
          grade: '不及格',
          score: '40',
          rate1: "5\'12\"",
          rate2: "5\'10\"",
          rate3: "4\'54\"",
          rate4: "4\'52\""
        },{
          grade: '不及格',
          score: '30',
          rate1: "5\'32\"",
          rate2: "5\'30\"",
          rate3: "5\'04\"",
          rate4: "5\'02\""
        },{
          grade: '不及格',
          score: '20',
          rate1: "5\'52\"",
          rate2: "5\'50\"",
          rate3: "5\'14\"",
          rate4: "5\'12\""
        },{
          grade: '不及格',
          score: '10',
          rate1: "6\'12\"",
          rate2: "6\'10\"",
          rate3: "5\'24\"",
          rate4: "5\'22\""
        },{
          grade: '占比',
          score: '10%',
          rate1: "引体向上",
          rate2: "引体向上",
          rate3: "仰卧起坐",
          rate4: "仰卧起坐"
        },{
          grade: '优秀',
          score: '100',
          rate1: "19",
          rate2: "20",
          rate3: "56",
          rate4: "57"
        },{
          grade: '优秀',
          score: '95',
          rate1: "18",
          rate2: "19",
          rate3: "54",
          rate4: "55"
        },{
          grade: '优秀',
          score: '90',
          rate1: "17",
          rate2: "18",
          rate3: "52",
          rate4: "53"
        },{
          grade: '良好',
          score: '85',
          rate1: "16",
          rate2: "17",
          rate3: "49",
          rate4: "50"}
          ,{
          grade: '良好',
          score: '80',
          rate1: "15",
          rate2: "16",
          rate3: "46",
          rate4: "47 "  },{
          grade: '及格',
          score: '78',
          rate1: "",
          rate2: "",
          rate3: "44",
          rate4: "45"
        },{
          grade: '及格',
          score: '76',
          rate1: "14",
          rate2: "15",
          rate3: "42",
          rate4: "43"
        },{
          grade: '及格',
          score: '74',
          rate1: "",
          rate2: "",
          rate3: "40",
          rate4: "41"
        },{
          grade: '及格',
          score: '72',
          rate1: "13",
          rate2: "14",
          rate3: "38",
          rate4: "39"
        },{
          grade: '及格',
          score: '70',
          rate1: "",
          rate2: "",
          rate3: "36",
          rate4: "37"
        },{
          grade: '及格',
          score: '68',
          rate1: "12",
          rate2: "13",
          rate3: "34",
          rate4: "35"
        },{
          grade: '及格',
          score: '66',
          rate1: "",
          rate2: "",
          rate3: "32",
          rate4: "33"
        },{
          grade: '及格',
          score: '64',
          rate1: "12",
          rate2: "13",
          rate3: "30",
          rate4: "31"
        },{
          grade: '及格',
          score: '62',
          rate1: "",
          rate2: "",
          rate3: "28",
          rate4: "29"
        },{
          grade: '及格',
          score: '60',
          rate1: "10",
          rate2: "11",
          rate3: "26",
          rate4: "27"
        },{
          grade: '不及格',
          score: '50',
          rate1: "9",
          rate2: "10",
          rate3: "24",
          rate4: "25"
        },{
          grade: '不及格',
          score: '40',
          rate1: "8",
          rate2: "9",
          rate3: "22",
          rate4: "23"
        },{
          grade: '不及格',
          score: '30',
          rate1: "7",
          rate2: "8",
          rate3: "20",
          rate4: "21"
        },{
          grade: '不及格',
          score: '20',
          rate1: "6",
          rate2: "7",
          rate3: "18",
          rate4: "19"
        },{
          grade: '不及格',
          score: '10',
          rate1: "5",
          rate2: "6",
          rate3: "16",
          rate4: "17"
        },{
          grade: '占比',
          score: '10%',
          rate1: "立定跳远",
          rate2: "立定跳远",
          rate3: "立定跳远",
          rate4: "立定跳远"
        },{
          grade: '优秀',
          score: '100',
          rate1: "273",
          rate2: "275",
          rate3: "207",
          rate4: "208"
        },{
          grade: '优秀',
          score: '95',
          rate1: "268",
          rate2: "270",
          rate3: "201",
          rate4: "202"
        },{
          grade: '优秀',
          score: '90',
          rate1: "263",
          rate2: "265",
          rate3: "195",
          rate4: "196"
        },{
          grade: '良好',
          score: '85',
          rate1: "256",
          rate2: "258",
          rate3: "188",
          rate4: "189"}
          ,{
          grade: '良好',
          score: '80',
          rate1: "248",
          rate2: "250",
          rate3: "181",
          rate4: "182"  }
          ,{
          grade: '及格',
          score: '78',
          rate1: "244",
          rate2: "246",
          rate3: "178",
          rate4: "179"
        },{
          grade: '及格',
          score: '76',
          rate1: "240",
          rate2: "242",
          rate3: "175",
          rate4: "176"
        },{
          grade: '及格',
          score: '74',
          rate1: "236",
          rate2: "238",
          rate3: "172",
          rate4: "173"
        },{
          grade: '及格',
          score: '72',
          rate1: "232",
          rate2: "234",
          rate3: "169",
          rate4: "170"
        },{
          grade: '及格',
          score: '70',
          rate1: "228",
          rate2: "230",
          rate3: "166",
          rate4: "167"
        },{
          grade: '及格',
          score: '68',
          rate1: "224",
          rate2: "226",
          rate3: "163",
          rate4: "164"
        },{
          grade: '及格',
          score: '66',
          rate1: "220",
          rate2: "222",
          rate3: "160",
          rate4: "161"
        },{
          grade: '及格',
          score: '64',
          rate1: "216",
          rate2: "218",
          rate3: "157",
          rate4: "158"
        },{
          grade: '及格',
          score: '62',
          rate1: "212",
          rate2: "214",
          rate3: "154",
          rate4: "155"
        },{
          grade: '及格',
          score: '60',
          rate1: "208",
          rate2: "210",
          rate3: "151",
          rate4: "152"
        },{
          grade: '不及格',
          score: '50',
          rate1: "203",
          rate2: "205",
          rate3: "146",
          rate4: "147"
        },{
          grade: '不及格',
          score: '40',
          rate1: "198",
          rate2: "200",
          rate3: "141",
          rate4: "142"
        },{
          grade: '不及格',
          score: '30',
          rate1: "193",
          rate2: "195",
          rate3: "136",
          rate4: "137"
        },{
          grade: '不及格',
          score: '20',
          rate1: "188",
          rate2: "190",
          rate3: "131",
          rate4: "132"
        },{
          grade: '不及格',
          score: '10',
          rate1: "183",
          rate2: "185",
          rate3: "126",
          rate4: "127"
        },{
          grade: '占比',
          score: '10%',
          rate1: "坐位体前屈",
          rate2: "坐位体前屈",
          rate3: "坐位体前屈",
          rate4: "坐位体前屈"
        },{
          grade: '优秀',
          score: '100',
          rate1: "24.9",
          rate2: "25.1",
          rate3: "25.8",
          rate4: "26.3"
        },{
          grade: '优秀',
          score: '95',
          rate1: "23.1",
          rate2: "23.3",
          rate3: "24.0",
          rate4: "24.4"
        },{
          grade: '优秀',
          score: '90',
          rate1: "21.3",
          rate2: "21.5",
          rate3: "22.2",
          rate4: "22.4"
        },{
          grade: '良好',
          score: '85',
          rate1: "19.5",
          rate2: "19.9",
          rate3: "20.6",
          rate4: "21.0"}
          ,{
          grade: '良好',
          score: '80',
          rate1: "17.7",
          rate2: "18.2",
          rate3: "19.0",
          rate4: "19.5"  }
          ,{
          grade: '及格',
          score: '78',
          rate1: "16.3",
          rate2: "16.8",
          rate3: "17.7",
          rate4: "18.2"
        },{
          grade: '及格',
          score: '76',
          rate1: "14.9",
          rate2: "15.4",
          rate3: "16.4",
          rate4: "16.9"
        },{
          grade: '及格',
          score: '74',
          rate1: "13.5",
          rate2: "14.0",
          rate3: "15.1",
          rate4: "15.6"
        },{
          grade: '及格',
          score: '72',
          rate1: "12.1",
          rate2: "12.6",
          rate3: "13.8",
          rate4: "14.3"
        },{
          grade: '及格',
          score: '70',
          rate1: "10.7",
          rate2: "11.2",
          rate3: "12.5",
          rate4: "13.0"
        },{
          grade: '及格',
          score: '68',
          rate1: "9.3",
          rate2: "9.8",
          rate3: "11.2",
          rate4: "11.7"
        },{
          grade: '及格',
          score: '66',
          rate1: "7.9",
          rate2: "8.4",
          rate3: "9.9",
          rate4: "10.4"
        },{
          grade: '及格',
          score: '64',
          rate1: "6.5",
          rate2: "7.0",
          rate3: "8.6",
          rate4: "9.1"
        },{
          grade: '及格',
          score: '62',
          rate1: "5.1",
          rate2: "5.6",
          rate3: "7.3",
          rate4: "7.8"
        },{
          grade: '及格',
          score: '60',
          rate1: "3.7",
          rate2: "4.2",
          rate3: "6.0",
          rate4: "6.5"
        },{
          grade: '不及格',
          score: '50',
          rate1: "2.7",
          rate2: "3.2",
          rate3: "5.2",
          rate4: "5.7"
        },{
          grade: '不及格',
          score: '40',
          rate1: "1.7",
          rate2: "2.2",
          rate3: "4.4",
          rate4: "4.9"
        },{
          grade: '不及格',
          score: '30',
          rate1: "0.7",
          rate2: "1.2",
          rate3: "3.6",
          rate4: "4.1"
        },{
          grade: '不及格',
          score: '20',
          rate1: "-0.3",
          rate2: "0.2",
          rate3: "2.8",
          rate4: "3.3"
        },{
          grade: '不及格',
          score: '10',
          rate1: "-1.3",
          rate2: "-0.8",
          rate3: "2.0",
          rate4: "2.5"
        },{
          grade: '占比',
          score: '10%',
          rate1: "50米跑",
          rate2: "50米跑",
          rate3: "50米跑",
          rate4: "50米跑"
        },{
          grade: '优秀',
          score: '100',
          rate1: "6.7",
          rate2: "6.6",
          rate3: "7.5",
          rate4: "7.4"
        },{
          grade: '优秀',
          score: '95',
          rate1: "6.8",
          rate2: "6.7",
          rate3: "7.6",
          rate4: "7.5"
        },{
          grade: '优秀',
          score: '90',
          rate1: "6.9",
          rate2: "6.8",
          rate3: "7.7",
          rate4: "7.6"
        },{
          grade: '良好',
          score: '85',
          rate1: "7.0",
          rate2: "6.9",
          rate3: "8.0",
          rate4: "7.9"}
          ,{
          grade: '良好',
          score: '80',
          rate1: "7.1",
          rate2: "7.0",
          rate3: "8.3",
          rate4: "8.2"  }
          ,{
          grade: '及格',
          score: '78',
          rate1: "7.3",
          rate2: "7.2",
          rate3: "8.5",
          rate4: "8.4"
        },{
          grade: '及格',
          score: '76',
          rate1: "7.5",
          rate2: "7.4",
          rate3: "8.7",
          rate4: "8.6"
        },{
          grade: '及格',
          score: '74',
          rate1: "7.7",
          rate2: "7.6",
          rate3: "8.9",
          rate4: "8.8"
        },{
          grade: '及格',
          score: '72',
          rate1: "7.9",
          rate2: "7.8",
          rate3: "9.1",
          rate4: "9.0"
        },{
          grade: '及格',
          score: '70',
          rate1: "8.1",
          rate2: "8.0",
          rate3: "9.3",
          rate4: "9.2"
        },{
          grade: '及格',
          score: '68',
          rate1: "8.3",
          rate2: "8.2",
          rate3: "9.5",
          rate4: "9.4"
        },{
          grade: '及格',
          score: '66',
          rate1: "8.5",
          rate2: "8.4",
          rate3: "9.7",
          rate4: "9.6"
        },{
          grade: '及格',
          score: '64',
          rate1: "8.7",
          rate2: "8.6",
          rate3: "9.9",
          rate4: "9.8"
        },{
          grade: '及格',
          score: '62',
          rate1: "8.9",
          rate2: "8.8",
          rate3: "10.1",
          rate4: "10.0"
        },{
          grade: '及格',
          score: '60',
          rate1: "9.1",
          rate2: "9.0",
          rate3: "10.3",
          rate4: "10.2"
        },{
          grade: '不及格',
          score: '50',
          rate1: "9.3",
          rate2: "9.2",
          rate3: "10.5",
          rate4: "10.4"
        },{
          grade: '不及格',
          score: '40',
          rate1: "9.5",
          rate2: "9.4",
          rate3: "10.7",
          rate4: "10.6"
        },{
          grade: '不及格',
          score: '30',
          rate1: "9.7",
          rate2: "9.6",
          rate3: "10.9",
          rate4: "10.8"
        },{
          grade: '不及格',
          score: '20',
          rate1: "9.9",
          rate2: "9.8",
          rate3: "11.1",
          rate4: "11.0"
        },{
          grade: '不及格',
          score: '10',
          rate1: "10.1",
          rate2: "10.0",
          rate3: "11.3",
          rate4: "11.2"
        },{
          grade: '占比',
          score: '10%',
          rate1: "肺活量",
          rate2: "肺活量",
          rate3: "肺活量",
          rate4: "肺活量"
        },{
          grade: '优秀',
          score: '100',
          rate1: "5040",
          rate2: "5140",
          rate3: "3400",
          rate4: "3450"
        },{
          grade: '优秀',
          score: '95',
          rate1: "4920",
          rate2: "5020",
          rate3: "3350",
          rate4: "3400"
        },{
          grade: '优秀',
          score: '90',
          rate1: "4800",
          rate2: "4900",
          rate3: "3150",
          rate4: "3200"
        },{
          grade: '良好',
          score: '85',
          rate1: "4550",
          rate2: "4650",
          rate3: "3150",
          rate4: "3200"}
          ,{
          grade: '良好',
          score: '80',
          rate1: "4300",
          rate2: "4400",
          rate3: "3000",
          rate4: "3050"  }
          ,{
          grade: '及格',
          score: '78',
          rate1: "4180",
          rate2: "4280",
          rate3: "2900",
          rate4: "2950"
        },{
          grade: '及格',
          score: '76',
          rate1: "4060",
          rate2: "4160",
          rate3: "2800",
          rate4: "2850"
        },{
          grade: '及格',
          score: '74',
          rate1: "3940",
          rate2: "4040",
          rate3: "2700",
          rate4: "2750"
        },{
          grade: '及格',
          score: '72',
          rate1: "3820",
          rate2: "3920",
          rate3: "2600",
          rate4: "2650"
        },{
          grade: '及格',
          score: '70',
          rate1: "3700",
          rate2: "3800",
          rate3: "2500",
          rate4: "2550"
        },{
          grade: '及格',
          score: '68',
          rate1: "3580",
          rate2: "3680",
          rate3: "2400",
          rate4: "2450"
        },{
          grade: '及格',
          score: '66',
          rate1: "3460",
          rate2: "3560",
          rate3: "2300",
          rate4: "2350"
        },{
          grade: '及格',
          score: '64',
          rate1: "3340",
          rate2: "3440",
          rate3: "2200",
          rate4: "2250"
        },{
          grade: '及格',
          score: '62',
          rate1: "3220",
          rate2: "3320",
          rate3: "2100",
          rate4: "2150"
        },{
          grade: '及格',
          score: '60',
          rate1: "3100",
          rate2: "3200",
          rate3: "2000",
          rate4: "2050"
        },{
          grade: '不及格',
          score: '50',
          rate1: "2940",
          rate2: "3030",
          rate3: "1960",
          rate4: "2010"
        },{
          grade: '不及格',
          score: '40',
          rate1: "2780",
          rate2: "2860",
          rate3: "1920",
          rate4: "1970"
        },{
          grade: '不及格',
          score: '30',
          rate1: "2620",
          rate2: "2690",
          rate3: "1880",
          rate4: "1930"
        },{
          grade: '不及格',
          score: '20',
          rate1: "2460",
          rate2: "2520",
          rate3: "1840",
          rate4: "1890"
        },{
          grade: '不及格',
          score: '10',
          rate1: "2300",
          rate2: "2350",
          rate3: "1800",
          rate4: "1850"
        },{
          grade: '占比',
          score: '15%',
          rate1: "BMI",
          rate2: "BMI",
          rate3: "BMI",
          rate4: "BMI"
        },{
          grade: '正常',
          score: '100',
          rate1: "17.9~23.9",
          rate2: "17.9~23.9",
          rate3: "17.2~23.9",
          rate4: "17.2~23.9"
        },{
          grade: '低体重',
          score: '80',
          rate1: "<=17.8",
          rate2: "<=17.8",
          rate3: "<=17.1",
          rate4: "<=17.1"
        },{
          grade: '超重',
          score: '80',
          rate1: "24.0~27.9",
          rate2: "24.0~27.9",
          rate3: "24.0~27.9",
          rate4: "24.0~27.9"
        },{
          grade: '肥胖',
          score: '60',
          rate1: ">=28.0",
          rate2: ">=28.0",
          rate3: ">=28.0",
          rate4: ">=28.0"
        },]
        
      }
    },
    created() {
      this.setrowspans();
    },
    methods: {
      objectSpanMethod({ row, column, rowIndex, columnIndex }) {
      if (columnIndex === 0) {
        return {
          rowspan: row.rowspan,
          colspan: 1
        };
      }
    },
    setrowspans() {
      // 先给所有的数据都加一个v.rowspan = 1
      this.tableData.forEach(v => {
        v.rowspan = 1;
      });
      // 双层循环
      for (let i = 0; i < this.tableData.length; i++) {
        // 内层循环，上面已经给所有的行都加了v.rowspan = 1
        // 这里进行判断
        // 如果当前行的id和下一行的id相等
        // 就把当前v.rowspan + 1
        // 下一行的v.rowspan - 1
        for (let j = i + 1; j < this.tableData.length; j++) {
          //此处可根据相同字段进行合并，此处是根据的id
          if (this.tableData[i].grade === this.tableData[j].grade) {
            this.tableData[i].rowspan++;
            this.tableData[j].rowspan--;
          }else{
            j= this.tableData.length;
          }
        }
        // 这里跳过已经重复的数据
        i = i + this.tableData[i].rowspan - 1;
      }
    },



    }
  }
</script>

