import matplotlib.pyplot as plt

f = plt.figure()
patch1 = plt.Circle([0., 0.], 4, fc='r')
patch2 = plt.Circle([5., 2.], 4, fc='b')
ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
ax.add_patch(patch1)
ax.add_patch(patch2)
plt.show()