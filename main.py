from bus import *


result = np.zeros(300)
perfect = np.zeros(300)

for people in range(0, 1000):
    rounds = play_memory_less()
    result[rounds] += 1
    rounds = play_perfectly()
    perfect[rounds] += 1
    # print('You drank ', rounds, 'times')


result /= 1000
perfect /= 1000
mean = 0
mean_perfect = 0
for i in range(50):
    val = result[i]
    mean += val*i
    mean_perfect += perfect[i]*i

graphline(result, 'Best Guess Results')
graphline(perfect, 'Pefect Game Results')
plt.show()
print('average:', mean)
print('average_perfect:', mean_perfect)
# scatterPlot(result)
