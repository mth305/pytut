import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation

def animate_imshow(frames, time=None, vmin=0, vmax=1, cmap_name="gist_rainbow",
                  figsize=(8,5)):
    def _blit_draw(self, artists, bg_cache):
        # Handles blitted drawing, which renders only the artists given instead
        # of the entire figure.
        updated_ax = []
        for a in artists:
            # If we haven't cached the background for this axes object, do
            # so now. This might not always be reliable, but it's an attempt
            # to automate the process.
            if a.axes not in bg_cache:
                # bg_cache[a.axes] = a.figure.canvas.copy_from_bbox(a.axes.bbox)
                # change here
                bg_cache[a.axes] = a.figure.canvas.copy_from_bbox(a.axes.figure.bbox)
            a.axes.draw_artist(a)
            updated_ax.append(a.axes)
    
        # After rendering all the needed artists, blit each axes individually.
        for ax in set(updated_ax):
            # and here
            # ax.figure.canvas.blit(ax.bbox)
            ax.figure.canvas.blit(ax.figure.bbox)
    matplotlib.animation.Animation._blit_draw = _blit_draw
    fig = plt.figure(figsize=figsize)
    ax  = plt.gca()
    im  = ax.imshow(frames[0], animated=True, vmin=vmin, vmax=vmax,
                    cmap=plt.get_cmap(cmap_name))
    text = ax.text(.5, 1.05, '', transform = ax.transAxes, va='center')
    if time is None:
        time = np.arange(len(frames))
    def init():
        text.set_text("")
        im.set_data(frames[0])
        return im,text
    def animate(i):
        text.set_text(str(time[i]))
        im.set_data(frames[i])
        return im,text
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=len(frames), interval=20, blit=True)
    return anim
