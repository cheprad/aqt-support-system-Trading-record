# สร้าง DataFrame เพื่อใช้ในตัวอย่าง
import pandas as pd

data = {
    'คอร์ส': ['Python', 'Python', 'Java', 'Java', 'Python'],
    'ชื่อ': ['A', 'B', 'C', 'D', 'E'],
    'เลขที่': [1, 2, 3, 4, 5],
    'ชั้นปี': [1, 2, 1, 2, 1]
}

df = pd.DataFrame(data)

# แยก DataFrame ตามชั้นปี
df_by_year = {}
for year, group in df.groupby('ชั้นปี'):
    df_by_year[year] = group

# แสดง DataFrame ที่แยกตามชั้นปี
print(df_by_year[1]) # แสดง DataFrame ของชั้นปี 1
print(df_by_year[2]) # แสดง DataFrame ของชั้นปี 2
