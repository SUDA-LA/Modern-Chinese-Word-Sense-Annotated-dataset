import json
import os
import csv



def T_count(dic_point,lst_gold,k):
    sorted_items_by_value = sorted(dic_point.items(), key=lambda item: item[1],reverse=True)


    output=0

    for combo in sorted_items_by_value:

        if output==k:
            break

        if combo[0] in lst_gold:
            output+=1

        else:
            break
    
    return output


def main():

    path_test=r'请替换为你电脑中的 \Modern-Chinese-Word-Sense-Annotated-Corpus\Dataset_ALL\test.data.txt 文件'
    path_test_gloss=r'请替换为你电脑中的 \Modern-Chinese-Word-Sense-Annotated-Corpus\GlossBERT\test\test.csv 文件'
    path_result=r'请替换为你的结果文件'
    with open(path_test, 'r', encoding='utf-8') as f_test:
        with open(path_test_gloss, 'r', encoding='utf-8') as f_gloss:
            with open(path_result, 'r', encoding='utf-8') as f_result:

                #去掉头名称

                line_gloss=f_gloss.readline()

                #初始化部分变量
                sentence_turn='None'
                lst_gold=[]
                k_num=0
                dic_point={}


                count_right=0
                count_all=0


                while line_gloss:
                    line_gloss=f_gloss.readline()
                    line_result=f_result.readline()

                    if not line_gloss:
                        T=T_count(dic_point,lst_gold,k_num)
                        count_all+=k_num
                        count_right+=T
                        break

                    lst_gloss=line_gloss.strip('\n').split()
                    lst_result=line_result.strip('\n').split()
                    sentence_now=lst_gloss[2]
                    sense_now=lst_gloss[4]
                    point_now=eval(lst_result[2])

                    if sentence_now!=sentence_turn:    #如果当前句子与预存的句子不同，则开始一轮计算
                        T=T_count(dic_point,lst_gold,k_num)
                        count_all+=k_num
                        count_right+=T                

                        #结束一轮计算，下面开始初始化下一轮变量

                        sentence_turn=sentence_now
                        data_gold=f_test.readline()
                        line_gold=data_gold.strip('\n').split()
                        sense_gold=line_gold[2]
                        lst_gold=sense_gold.split('$$')
                        k_num=len(lst_gold)
                        dic_point={}
                    
                    dic_point[sense_now]=point_now
                    

                print(count_right/count_all)

                    
    





if __name__ == "__main__":
    main()