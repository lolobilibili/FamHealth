from django.shortcuts import render
import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
from . import models
from django.utils.timezone import localtime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from drf_yasg.openapi import Parameter, IN_PATH, IN_QUERY, TYPE_STRING, TYPE_INTEGER
# Create your views here.

# 读取项目所需文件
path = os.getcwd()+'\\calculator\\files\\'
df_bmi = pd.read_excel(path + 'BMI.xlsx')
df_vital_capacity = pd.read_excel(path + "肺活量.xlsx")
df_run_50 = pd.read_excel(path + "50米跑.xlsx")
df_sit_and_reach = pd.read_excel(path + "坐位体前屈.xlsx")
df_jump = pd.read_excel(path + "立定跳远.xlsx")
df_Pull_ups_and_sit_ups = pd.read_excel(path + "引体向上与仰卧起坐.xlsx")
df_run_1000 = pd.read_excel(path + "耐力跑.xlsx")
standard = pd.read_excel(path + '档位表.xlsx')


# 这个函数计算肺活量，立定跳远，引体向上与仰卧起坐，坐位体前屈，BMI的分值转换
# 其中，label代表学生对应性别与年级信息，df表示成绩对应表，performance表示体测表现
def Cal_each_1(label, df, performance):
    performance_range = df[(df[label] <= performance)]
    return performance_range["分数"].iloc[0]


# 这个函数计算50米跑，耐力跑的分值转换
# 其中，label代表学生对应性别与年级信息，df表示成绩对应表，performance表示体测表现
def Cal_each_2(label, df, performance):
    performance_range = df[(df[label] >= performance)]
    return performance_range["分数"].iloc[0]


# 这个函数将各个项目的分值汇总，各占比如下：
"""
* BMI 15%
* 肺活量 15%
* 50米 20%
* 坐位体前屈 10%
* 立定跳远 10%
* 引体向上与仰卧起坐 10%  <u>（引体向上与仰卧起坐需要单独写函数）</u>
* 耐力跑 20%
"""


def Cal_score(label, bmi, vital_capacity, run_50, sit_and_reach, jump, Pull_ups_and_sit_ups, run_1000):
    performance = [bmi, vital_capacity, run_50, sit_and_reach, jump, Pull_ups_and_sit_ups, run_1000]
    bmi_score = Cal_each_1(label, df_bmi, bmi)
    vital_capacity_score = Cal_each_1(label, df_vital_capacity, vital_capacity)
    run_50_score = Cal_each_2(label, df_run_50, run_50)
    sit_and_reach_score = Cal_each_1(label, df_sit_and_reach, sit_and_reach)
    jump_score = Cal_each_1(label, df_jump, jump)
    Pull_ups_and_sit_ups_score = Cal_each_1(label, df_Pull_ups_and_sit_ups, Pull_ups_and_sit_ups)
    run_1000_score = Cal_each_2(label, df_run_1000, run_1000)
    score = 0.15 * bmi_score + 0.15 * vital_capacity_score + 0.2 * run_50_score + 0.1 * sit_and_reach_score + 0.1 * jump_score + 0.1 * Pull_ups_and_sit_ups_score + 0.2 * run_1000_score
    all_score = [bmi_score, vital_capacity_score, run_50_score, sit_and_reach_score, jump_score,
                 Pull_ups_and_sit_ups_score, run_1000_score, score]
    return performance, all_score


# 该函数用于对直接分数的计算
def use_score_Cal(each_score):
    score = each_score[0] * 0.15 + each_score[1] * 0.15 + each_score[2] * 0.2 + each_score[3] * 0.1 + each_score[
        4] * 0.1 + each_score[5] * 0.1 + each_score[6] * 0.2
    return score


# 该函数用于返回主函数所需要的列表值
# 考虑到引体向上提升较难，所以若一个人引体向上是0分，我们会将引体向上这一项不列入推荐提升中
# bmi也会被剔除掉
def renew_lst(each_score, performance, expect_score):
    table_lst = []
    if (each_score[5] < 60) and (expect_score < 80):
        elimate_score = [each_score[1], each_score[2], each_score[3], each_score[4], each_score[6]]
        elimate_performance = [performance[1], performance[2], performance[3], performance[4], performance[6]]
        table_lst.append(df_vital_capacity)
        table_lst.append(df_run_50)
        table_lst.append(df_sit_and_reach)
        table_lst.append(df_jump)
        table_lst.append(df_run_1000)
        flag = 0
    else:
        elimate_score = each_score[1:]
        elimate_performance = performance[1:]
        table_lst.append(df_vital_capacity)
        table_lst.append(df_run_50)
        table_lst.append(df_sit_and_reach)
        table_lst.append(df_jump)
        table_lst.append(df_Pull_ups_and_sit_ups)
        table_lst.append(df_run_1000)
        flag = 1
    return elimate_score, elimate_performance, table_lst, flag


# 提升完各分值之后，再次汇总更新到总的分值表中
def return_score_lst(bmi, Pull_ups_and_sit_ups, elimate_score, flag):
    return_lst = []
    if flag == 0:
        return_lst = [bmi, elimate_score[0], elimate_score[1], elimate_score[2], elimate_score[3], Pull_ups_and_sit_ups,
                      elimate_score[4]]
    else:
        return_lst = [bmi, elimate_score[0], elimate_score[1], elimate_score[2], elimate_score[3], elimate_score[4],
                      elimate_score[5]]
    return return_lst

def numTorun(num):
    s=str(num)
    s = s.replace('.','’')
    s = s + '’’'
    return s


# 提升完的表现也更新到总的表现中
def return_performance_lst(bmi, Pull_ups_and_sit_ups, elimate_performance, flag):
    return_lst = []
    if flag == 0:
        return_lst = [bmi, elimate_performance[0], elimate_performance[1], elimate_performance[2],
                      elimate_performance[3], Pull_ups_and_sit_ups, elimate_performance[4]]
    else:
        return_lst = [bmi, elimate_performance[0], elimate_performance[1], elimate_performance[2],
                      elimate_performance[3], elimate_performance[4], elimate_performance[5]]
    return return_lst


# 用于判断学生当前体测后的下一个档次分值，方便系统推荐提升项
def Get_expect_score(score, standard):
    score_range = standard[(standard['当前分数'] <= score)]
    expect_score = score_range['档位'].iloc[0]
    return expect_score


# 定义一个函数，用于找出低于平均值的元素下标
def find_below_average_indices(input_list, average):
    below_average_indices = []  # 用于存储低于平均值的元素下标
    # 遍历列表，找出低于平均值的元素，记录它们的下标
    for index, element in enumerate(input_list):
        if element <= average:
            below_average_indices.append(index)
    return below_average_indices

def find_minIndex(input_list):
    # 1. 初始化最小值和下标
    min_value = input_list[0]
    min_index = 0
    # 2. 遍历列表
    for index, element in enumerate(input_list):
        # 3. 检查是否有更小的元素
        if element < min_value:
            min_value = element
            min_index = index
    # 4. 返回最小值
    return min_index

# 该函数用于挖掘同学表现最差的一项，给出针对性建议
def give_suggest(label, each_score):
    new_score = each_score[1:]
    suggest1 = ['您的肺活量表现最差。*日常锻炼：参加长跑、登山、游泳、慢跑等有氧运动，能够锻炼肺部功能，有助于提升肺活量。*对于肺功能较弱，残气量较多的个体，可以通过吹气球和缩唇呼吸来提高肺活量。',
                '您的50米表现最差。*增强基础体能,通过有氧运动、力量训练、柔韧性训练等方式提高心肺功能、肌肉力量、关节灵活性等。*提高专项技能，通过模拟比赛、分段训练、间歇训练等方式提高起跑技术、加速技术、冲刺技术等。',
                '您的坐位体前屈表现最差。*增强柔韧性练习，进行拉伸等合理科学的锻炼，如单脚支撑练习法和双脚并拢体前屈练习法。',
                '您的立定跳远表现最差。*增强力量：特别是下肢肌群的爆发用力能力。*增强协调用力：协调用力正确的标志是髋、膝、踝三关节能迅速有力地蹬直，上肢能做出协调的摆动，起到带、领、提拉的作用。',
                '您的引体向上表现最差。*提升握杠的抓力,如单杠半握垂吊训练、坐姿杠铃屈腕训练、健身球辅助手指训练。*发展臂力与腰背的协作力量，可以强化背阔肌、肱二头肌。',
                '您的耐力跑表现最差。*加强上肢训练。1000米中长跑，上肢力量是很关键的，上肢力量决定摆臂的频率，这就决定了跑步的频率，这样可以提升1000米的跑步成绩。 *加强肺活量。可以保证我们能量的提供。 ']
    suggest2 = ['您的肺活量表现最差。*日常锻炼：参加长跑、登山、游泳、慢跑等有氧运动，能够锻炼肺部功能，有助于提升肺活量。*对于肺功能较弱，残气量较多的个体，可以通过吹气球和缩唇呼吸来提高肺活量。',
                '您的50米表现最差。*增强基础体能,通过有氧运动、力量训练、柔韧性训练等方式提高心肺功能、肌肉力量、关节灵活性等。*提高专项技能，通过模拟比赛、分段训练、间歇训练等方式提高起跑技术、加速技术、冲刺技术等。',
                '您的坐位体前屈表现最差。*增强柔韧性练习，进行拉伸等合理科学的锻炼，如单脚支撑练习法和双脚并拢体前屈练习法。',
                '您的立定跳远表现最差。*增强力量：特别是下肢肌群的爆发用力能力。*增强协调用力：协调用力正确的标志是髋、膝、踝三关节能迅速有力地蹬直，上肢能做出协调的摆动，起到带、领、提拉的作用。',
                '您的仰卧起坐表现最差。 *在睡觉前做仰卧起坐，根据自己的身体情况，可以从每天二十个增加到每天三十个再增加到每天四十个，直到有吃力感或者呼吸不太顺畅为止。*平时可以加强腰腹肌肉的锻炼。',
                '您的耐力跑表现最差。*加强上肢训练。1000米中长跑，上肢力量是很关键的，上肢力量决定摆臂的频率，这就决定了跑步的频率，这样可以提升1000米的跑步成绩。*加强肺活量。可以保证我们能量的提供， ']
    sex = label[2]
    index = find_minIndex(new_score)
    if sex == '男':
        suggestion = suggest1[index]
    else:
        suggestion = suggest2[index]
    return suggestion

'''
 推荐系统
* 首先读取档位表.xlsx，若score大于90，则返回真棒。若score小于，则选出上一档次分数并进入循环
* 计算出列表的平均值，低于平均值的<u>逐层往上</u>提高档次【这里剔除了引体向上/仰卧起坐与bmi】【引体向上/仰卧起坐若大于60，则有基础可以继续提升】
* 更新列表后计算得分，如果仍低于预期，继续计算平均值并向上提高档次。
* 如此循环更新，最终返回新列表与成绩
'''

def recommend_func(label, bmi, vital_capacity, run_50, sit_and_reach, jump, Pull_ups_and_sit_ups, run_1000):
    performance, all_score = Cal_score(label, bmi, vital_capacity, run_50, sit_and_reach, jump, Pull_ups_and_sit_ups,
                                       run_1000)
    score = all_score.pop()
    each_score = all_score
    if score >= 90:
        score = -1
        return performance, each_score, score
    else:
        expect_score = Get_expect_score(score, standard)
        while score < expect_score:
            elimate_score, elimate_performance, table_lst, flag = renew_lst(each_score, performance, expect_score)
            average = sum(elimate_score) / len(elimate_score)
            below_average_indices = find_below_average_indices(elimate_score, average)  # 对应项目的下标
            need_to_improve_score = []
            for index in below_average_indices:
                need_to_improve_score.append(elimate_score[index])
            for i in range(0, len(need_to_improve_score)):
                index = below_average_indices[i]  # 用于寻找表格与后续更新表格
                df = table_lst[index]
                filtered_rows = df[df['分数'] == need_to_improve_score[i]]
                row_indices = filtered_rows.index.tolist()[0]
                new_performance = df[label].iloc[row_indices - 1]
                new_score = df['分数'].iloc[row_indices - 1]
                if new_performance == 100000:
                    new_performance = df[label].iloc[row_indices - 2]
                    new_score = df['分数'].iloc[row_indices - 2]
                elimate_score[index] = new_score
                elimate_performance[index] = new_performance
                each_score = return_score_lst(each_score[0], each_score[5], elimate_score, flag)
                performance = return_performance_lst(performance[0], performance[5], elimate_performance, flag)
            score = use_score_Cal(each_score)
        return performance, each_score, score

# 该函数用于配置前端按钮，若按钮向下，会传递flag=-1，函数会寻找向下一档的分数以及对应的表现，按钮向上则反之。

def button_adjust(label, option, score, flag):
    file_name = {
        'bmi': 'BMI.xlsx',
        'vital_capacity': '肺活量.xlsx',
        'run_50': '50米跑.xlsx',
        'sit_and_reach': '坐位体前屈.xlsx',
        'jump': '立定跳远.xlsx',
        'Pull_ups_and_sit_ups': '引体向上与仰卧起坐.xlsx',
        'run_1000': '耐力跑.xlsx'
    }
    bmi_score = {
        100: 21,
        80: 25,
        60: 28
    }
    if option == 'bmi':
        new_score = score + flag * 20
        new_performance = bmi_score[new_score]
    else:
        df = pd.read_excel(path+file_name[option])
        filtered_rows = df[df['分数'] == score]
        row_indices = filtered_rows.index.tolist()[0]
        new_score = df['分数'].iloc[row_indices - flag]
        new_performance = df[label].iloc[row_indices - flag]
        if new_performance == 100000:
            new_score = df['分数'].iloc[row_indices - flag - flag]
            new_performance = df[label].iloc[row_indices - flag - flag]

    return new_score, new_performance

# score = Cal_score("大一男", 18.1, 4320, 7.1, 11.5, 258, 4, 3.40)

@api_view(['GET'])
def get_data(request):
    height=float(request.GET.get("height"))
    weight = float(request.GET.get("weight"))
    bmi = float(request.GET.get("bmi"))
    vital_capacity = float(request.GET.get("vital_capacity"))
    run_50 = float(request.GET.get("run_50"))
    sit_and_reach = float(request.GET.get("sit_and_reach"))
    jump = float(request.GET.get("jump"))
    Pull_ups_and_sit_ups = float(request.GET.get("Pull_ups_and_sit_ups"))
    run_1000 = float(request.GET.get("run_1000"))
    label = str(request.GET.get("label"))
    username = str(request.GET.get("username"))
    performance, all_score = Cal_score(label, bmi, vital_capacity, run_50, sit_and_reach, jump, Pull_ups_and_sit_ups,run_1000)
    # all_score_new = all_score

    score = all_score.pop()
    each_score = all_score
    suggestion = give_suggest(label, each_score)
    data = [
        {'name': 'bmi','height':height,'weight':weight, 'performance': round(performance[0],2), 'score': all_score[0]},
        {'name': 'vital_capacity', 'performance': performance[1], 'score': all_score[1]},
        {'name': 'run_50', 'performance': performance[2], 'score': all_score[2]},
        {'name': 'sit_and_reach', 'performance': performance[3], 'score': all_score[3]},
        {'name': 'jump', 'performance': performance[4], 'score': all_score[4]},
        {'name': 'Pull_ups_and_sit_ups', 'performance': performance[5], 'score': all_score[5]},
        {'name': 'run_1000', 'num_performance': performance[6], 'performance': numTorun(performance[6]), 'score': all_score[6]},
        {'name': 'score', 'score': round(score,2),'suggestion':suggestion},
    ]
    models.Score_record.objects.update_or_create(
        username=username,
        defaults={'weight':weight,'height':height,'bmi':round(performance[0],2),'vital_capacity':performance[1],'run_50':performance[2],'sit_and_reach':performance[3],'jump':performance[4],'Pull_ups_and_sit_ups':performance[5],'run_1000':performance[6],'run_1000_performance':numTorun(performance[6]),'bmi_score':all_score[0],'vital_capacity_score':all_score[1],'run_50_score':all_score[2],'sit_and_reach_score':all_score[3],'jump_score':all_score[4],'Pull_ups_and_sit_ups_score':all_score[5],'run_1000_score':all_score[6],'score':score,'suggestion':suggestion}
    )
    return Response(data)

polygon_view_get_desc='获取当前对象的历史成绩'
polygon_view_get_parm=[
    Parameter(name='username',in_=IN_QUERY,description='输入用户名',type=openapi.TYPE_STRING,required=True),

]

@swagger_auto_schema(method='get',operation_description=polygon_view_get_desc,manual_parameters=polygon_view_get_parm,operation_summary="获取当前对象的历史成绩")
@api_view(['GET'])
def get_data_by_username(request):
    
    username = str(request.GET.get("username"))
    data=models.Score_record.objects.filter(username=username)[0]
    # print(data[0].bmi)
    data = [
        {'name': 'bmi','height':data.height,'weight':data.weight, 'performance': data.bmi, 'score': data.bmi_score},
        {'name': 'vital_capacity', 'performance': data.vital_capacity, 'score': data.vital_capacity_score}, 
        {'name': 'run_50', 'performance': data.run_50, 'score': data.run_50_score},
        {'name': 'sit_and_reach', 'performance': data.sit_and_reach, 'score': data.sit_and_reach_score},
        {'name': 'jump', 'performance': data.jump, 'score': data.jump_score},
        {'name': 'Pull_ups_and_sit_ups', 'performance': data.Pull_ups_and_sit_ups, 'score': data.Pull_ups_and_sit_ups_score},
        {'name': 'run_1000', 'num_performance': data.run_1000, 'performance': data.run_1000_performance, 'score': data.run_1000_score},
        {'name': 'score', 'score':data.score,'suggestion':data.suggestion},
    ]
    # models.Score_record.objects.update_or_create(
    #     username=username,
    #     defaults={'bmi':round(performance[0],2),'vital_capacity':performance[1],'run_50':performance[2],'sit_and_reach':performance[3],'jump':performance[4],'Pull_ups_and_sit_ups':performance[5],'run_1000':performance[6],'run_1000_performance':numTorun(performance[6]),'bmi_score':all_score[0],'vital_capacity_score':all_score[1],'run_50_score':all_score[2],'sit_and_reach_score':all_score[3],'jump_score':all_score[4],'Pull_ups_and_sit_ups_score':all_score[5],'run_1000_score':all_score[6]}
    # )
    return Response(data)

polygon_view_get_desc='获取当前对象所在组所有成员的成绩'
polygon_view_get_parm=[
    Parameter(name='username',in_=IN_QUERY,description='输入用户名',type=openapi.TYPE_STRING,required=True),

]

@swagger_auto_schema(method='get',operation_description=polygon_view_get_desc,manual_parameters=polygon_view_get_parm,operation_summary="获取当前对象所在组所有成员的成绩")
@api_view(['GET'])
def get_data_by_group(request):
    
    username = str(request.GET.get("username"))
    def get_user_group_members(username):
        # 获取给定用户名的用户
        user = get_object_or_404(models.User_group, username=username)

        # 获取该用户所属的所有组
        user_groups = user.group_id

        # 获取所有属于这些组的用户，排除自己
        group_users = models.User_group.objects.filter(group_id=user_groups).distinct()

        # 提取这些用户的用户名
        usernames = group_users.values_list('username', flat=True)

        return list(usernames)
    # data=models.Score_record.objects.filter(username=username)
    # print(data[0].bmi)
    users=get_user_group_members(username)
    print(users)
    records=models.Score_record.objects.filter(username__in=users)
    result=[]
    for data in records:
        item = [
        {'username':data.username},
        {'name': 'bmi','height':data.height,'weight':data.weight, 'performance': data.bmi, 'score': data.bmi_score},
        {'name': 'vital_capacity', 'performance': data.vital_capacity, 'score': data.vital_capacity_score}, 
        {'name': 'run_50', 'performance': data.run_50, 'score': data.run_50_score},
        {'name': 'sit_and_reach', 'performance': data.sit_and_reach, 'score': data.sit_and_reach_score},
        {'name': 'jump', 'performance': data.jump, 'score': data.jump_score},
        {'name': 'Pull_ups_and_sit_ups', 'performance': data.Pull_ups_and_sit_ups, 'score': data.Pull_ups_and_sit_ups_score},
        {'name': 'run_1000', 'num_performance': data.run_1000, 'performance': data.run_1000_performance, 'score': data.run_1000_score},
        {'name': 'score', 'score': data.score,'suggestion':data.suggestion},
    ]
        result.append(item)

    return Response(result)



@api_view(['GET'])
def advise(request):
    bmi = float(request.GET.get("bmi"))
    vital_capacity = float(request.GET.get("vital_capacity"))
    run_50 = float(request.GET.get("run_50"))
    sit_and_reach = float(request.GET.get("sit_and_reach"))
    jump = float(request.GET.get("jump"))
    Pull_ups_and_sit_ups = float(request.GET.get("Pull_ups_and_sit_ups"))
    run_1000 = float(request.GET.get("run_1000"))
    label = str(request.GET.get("label"))
    performance, each_score, score = recommend_func(label, bmi, vital_capacity, run_50, sit_and_reach, jump,
                                                    Pull_ups_and_sit_ups, run_1000)
    data = [
        {'name': 'bmi', 'performance':  round(performance[0],2), 'score': each_score[0]},
        {'name': 'vital_capacity', 'performance': performance[1], 'score': each_score[1]},
        {'name': 'run_50', 'performance': performance[2], 'score': each_score[2]},
        {'name': 'sit_and_reach', 'performance': performance[3], 'score': each_score[3]},
        {'name': 'jump', 'performance': performance[4], 'score': each_score[4]},
        {'name': 'Pull_ups_and_sit_ups', 'performance': performance[5], 'score': each_score[5]},
        {'name': 'run_1000', 'num_performance': performance[6], 'performance': numTorun(performance[6]), 'score': each_score[6]},
        {'name': 'score', 'score': round(score,2)},
    ]

    return Response(data)

@api_view(['GET'])
def btn(request):
    label = str(request.GET.get("label"))
    option = str(request.GET.get("option"))
    score = int(request.GET.get("score"))
    flag = int(request.GET.get("flag"))
    new_score,new_performance = button_adjust(label,option,score,flag)
    if option == 'run_1000':
        data = [{'name':option,'score':new_score, 'num_performance':new_performance, 'performance':numTorun(new_performance)}]
    else:
        data = [{'name':option,'score':new_score,'performance':new_performance}]

    return Response(data)

@api_view(['GET'])
def sub(request):
    name = int(request.GET.get("name"))
    date = request.GET.get("date")
    desc = str(request.GET.get("desc"))
    input = int(request.GET.get("input"))
    username = request.GET.get("username")
    print(name,date,desc,input)
    date = date[0:10]
    if name==1:
        data =models.breakfast.objects.filter(date =date,username = username)
        if data:
            models.breakfast.objects.filter(date=date,username = username).update(des= desc,hot = input)
        else:
            models.breakfast.objects.create(date = date,des = desc,hot = input,username = username)
    if name==2:
        data =models.lunch.objects.filter(date =date,username = username)
        if data:
            models.lunch.objects.filter(date=date,username = username).update(des= desc,hot = input)
        else:
            models.lunch.objects.create(date = date,des = desc,hot = input,username = username)
    if name==3:
        data =models.dinner.objects.filter(date =date,username = username)
        if data:
            models.dinner.objects.filter(data=data,username = username).update(des= desc,hot = input)
        else:
            models.dinner.objects.create(date = date,des = desc,hot = input,username = username)
    if name==4:
        data =models.snack.objects.filter(date =date,username = username)
        if data:
            models.snack.objects.filter(data=data,username = username).update(des= desc,hot = input)
        else:
            models.snack.objects.create(date = date,des = desc,hot = input,username = username)
    if name==5:
        data =models.sport.objects.filter(date =date,username = username)
        if data:
            models.sport.objects.filter(data=data,username = username).update(des= desc,hot = input)
        else:
            models.sport.objects.create(date = date,des = desc,hot = input,username = username)
    return Response('成功')

@api_view(['GET'])
def sub2(request):
    date = request.GET.get("date")
    username = request.GET.get("username")
    date = date[0:10]
    print(date)
    
    data = []
    #获取五种行动消耗的热量和对应的描述
    breakfast= models.breakfast.objects.filter(date = date,username = username).values('hot','des')
    lunch= models.lunch.objects.filter(date = date,username = username).values('hot','des')
    dinner= models.dinner.objects.filter(date = date,username = username).values('hot','des')
    snack= models.snack.objects.filter(date = date,username = username).values('hot','des')
    sport= models.sport.objects.filter(date = date,username = username).values('hot','des')
    if breakfast:
        data.append({'hot':breakfast[0]['hot'],'des':breakfast[0]['des']})
    else:
        data.append({'hot':0,'des':''})
    if lunch:
        data.append({'hot':lunch[0]['hot'],'des':lunch[0]['des']})
    else:
        data.append({'hot':0,'des':''})
    if dinner:
        data.append({'hot':dinner[0]['hot'],'des':dinner[0]['des']})
    else:
        data.append({'hot':0,'des':''})
    if snack:
        data.append({'hot':snack[0]['hot'],'des':snack[0]['des']})
    else:
        data.append({'hot':0,'des':''})
    if sport:
        data.append({'hot':sport[0]['hot'],'des':sport[0]['des']})
    else:
        data.append({'hot':0,'des':''})
    print(data)
    return Response(data)





@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['username', 'password'],
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING,description='e: 造林更新'),
            'password': openapi.Schema(type=openapi.TYPE_STRING,description='变化原因 example: 造林更新'),
        },

    ),
    operation_summary='登录',
)
@api_view(['POST'])
def login(request):
	username = request.POST.get("username")
	password = request.POST.get("password")
	print(username)
	print(password)
	try:
		user = models.User.objects.get(username=username)
	except:
		date = {'flag': 'no', "msg" : "no to user"}
		return JsonResponse({'request':date})
	if password == user.password:
		date_msg = "登陆成功"
		date_flag = "yes"
		print("成功")
	else:
		date_msg = "密码输入错误"
		date_flag = "no"
	date = {'flag':date_flag,'msg': date_msg}

	return JsonResponse({'request': date})
@api_view(['GET'])
def fnotice(request):
    username = request.GET.get("username")
    print(username)
    data = []
    id = models.User_group.objects.filter(username = username).values('group_id')
    print(id[0]['group_id'])
    lists = models.User_group.objects.filter(group_id = id[0]['group_id']).values('username','text')
    print(lists)
    for l in lists:
        data.append({'username':l['username'],'text':l['text']})
    return Response(data)

@api_view(['GET'])
def update_notice(request):
    username  = request.GET.get("username")
    print(username)
    text = request.GET.get("textarea")
    print(username)
    models.User_group.objects.filter(username = username).update(text = text)
    return Response()