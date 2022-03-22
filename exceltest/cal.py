import xlrd
import xlwt

data_raw = xlrd.open_workbook('./scores.xls')
sheet = data_raw.sheet_by_index(0)
n_rows = sheet.nrows  # rows
n_cols = sheet.ncols  # cols
head_row = sheet.row_values(0)  # ['group', 'item1', 'item2', 'item3', 'item4', 'item5', 'scores']

wbk = xlwt.Workbook()
sheet_write = wbk.add_sheet('sheet 1', cell_overwrite_ok=True)
group_dic={}

for j in range(n_cols):
    sheet_write.write(0, j, head_row[j])

# cal the scores
for i in range(1, n_rows):
    sheet_write.write(i, 0, i)
    row_list = sheet.row_values(i)
    row_score = 1 / row_list[1] + row_list[2] + row_list[3] + 1 / row_list[4] + row_list[5]
    ii=str(i)
    group_dic.update({ii:row_score})
    for k in range(n_cols):
        sheet_write.write(i, k, row_list[k])
    sheet_write.write(i, n_cols-1, row_score)


res=sorted(group_dic.items(),key=lambda item:item[1],reverse=True)
print("the group rank top 8 is\n")
for a in range(8):
    print('rank ',a+1,' is group ',res[a][0],' and score is ',res[a][1])

sheet_write.write(0,n_cols,'rank')
for b in range(len(res)):
    sheet_write.write(int(res[b][0]),n_cols,b+1)

wbk.save('scores_results.xls')
