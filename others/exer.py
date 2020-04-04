import xlwt
import requests
import json


left_url = "http://jwzx.cqu.pt/data/json_StudentSearch.php?searchKey="

workbook = xlwt.Workbook(encoding='utf-8')
sheet = workbook.add_sheet('my worksheet', True)

list_class = ['学号', '姓名', '性别', '班级', '专业号', '专业名', '院系名', '年级', '出生日期', '民族']
for i in range(len(list_class)):
    sheet.write(0, i, list_class[i])
    workbook.save('stu_test780.xls')

cnt = 0
for num in range(2017210381, 2017210481):

    url = left_url + str(num)
    r = requests.get(url)
    content = r.text

    dic = json.loads(content)
    print(dic)
    '''
    这里要判断 returnData是否为空
    '''
    if dic['returnData']:
        fm_dict = dic["returnData"][0]
        cnt += 1

        xh = fm_dict["xh"]
        xm = fm_dict["xm"]
        xb = fm_dict["xb"]
        bj = fm_dict["bj"]
        zyh = fm_dict["zyh"]
        zym = fm_dict["zym"]
        yxm = fm_dict["yxm"]
        nj = fm_dict["nj"]
        csrq = (fm_dict["csrq"])
        mz = (fm_dict["mz"])

        lis_content = [xh, xm, xb, bj, zyh, zym, yxm, nj, csrq, mz]

        for i in range(len(list_class)):
            sheet.write(cnt, i, lis_content[i])
            workbook.save('stu_test780.xls')
