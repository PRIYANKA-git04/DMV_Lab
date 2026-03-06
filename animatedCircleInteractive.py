import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)


circle = plt.Circle((0, 5), 0.5)
ax.add_patch(circle)

x = 0
y = 5


def init():
    circle.center = (x, y)
    return circle,


def animate(frame):
    circle.center = (x, y)
    return circle,


def on_key(event):
    global x, y
    
    if event.key == "right":
        x += 0.5
    elif event.key == "left":
        x -= 0.5
    elif event.key == "up":
        y += 0.5
    elif event.key == "down":
        y -= 0.5


fig.canvas.mpl_connect('key_press_event', on_key)

ani = animation.FuncAnimation(
    fig,
    animate,
    frames=100,
    init_func=init,
    interval=30,
    blit=True
)

plt.show()
