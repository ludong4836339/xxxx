import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
fig,ax = plt.subplots()    # '''fig表示整张图片'''

ax.plot(squares,linewidth=3)

#设置图标标题并给出坐标轴
ax.set_title('平方数',fontsize=24)
ax.set_xlabel('值',fontsize=14)
ax.set_ylabel('值的平方',fontsize=14)
# 设置刻度标记的大小
ax.tick_params(axis='both',labelsize=14)
plt.show()