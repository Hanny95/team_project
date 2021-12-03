import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager, rc


font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

data = pd.read_csv('./resources/비만.csv',
                   index_col=0,
                   encoding='CP949',
                   engine='python')

print(data)

age = data['연령']
menFatRate = data['남성비만율']
womenFatRate = data['여성비만율']

plt.plot(age, menFatRate,
         color='#74a3d6',
         marker='o',
         label='남성')

plt.plot(age, womenFatRate,
         color='#e099d9',
         marker='o',
         label='여성')

plt.title('연령에 따른 비만율')
plt.xlabel('연령')
plt.ylabel('비만율(%)')
plt.ylim([0, 100])

plt.legend()

plt.show()

# plt.plot(years,gdp,color='green',marker='o',linestyle='solid')
