import matplotlib.pyplot as plt

x = list(range(1, 1001))
y = [i ** 2 for i in x]
plt.scatter(x, y, s=10, edgecolors='none', c=y, cmap=plt.cm.Reds)

plt.title("Square number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14, which='major')

plt.axis([0, 1100, 0, 1100000])
plt.savefig('s.png', bbox_inches='tight')
plt.show()

