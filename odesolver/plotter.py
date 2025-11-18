import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, ArtistAnimation
from matplotlib.artist import Artist

class Plotter():
    """
        Class for plotting the numerically attained solutions of ODEs.    
    """

    GIF_FORMAT = "gif"
    HTML_FORMAT = "html"
    PNG_FORMAT = "png"

    def plot(xdata:np.ndarray, ydata:np.ndarray, filename:str = None, fileformat:str = None, animation:bool = False, save_fps:int = 120, animation_tail:bool = False, tail_length:int = 200, center:tuple[float, float] = (None, None), **kwargs) -> None:
        """
            Function for plotting the obtained numeric solution of an ODE.
            Keyword arguments (kwargs) are for additional plot settings, such as labels, figsize, dpi, pointsize etc.

            Parameters
            ------------------
                xdata : np.ndarray
                    The plotted x-data.
                ydata : np.ndarray
                    The plotted y-data.
                filename : str = None
                    The filename of the saved graph.
                fileformat : str = None
                    The format of the saved graph, e.g. png or gif.
                animation : bool = False
                    Animate the solution?
                save_fps : int = 120
                    The FPS of the saved animation.
                animation_tail : bool = False
                    Show a tail within the animation.
                tail_length : int = 200
                    The length of the tail.
                center : tuple = (None, None)
                    The coordinates of the center point.    
        
        """

        if len(xdata.shape) > 1:
            if xdata.shape[1] != 1:
                raise Exception("Given x-data is not one-dimensionsal!")        
        elif len(ydata.shape) > 1:
            if ydata.shape[1] != 1:
                raise Exception("Given y-data is not one-dimensionsal!") 

        # plot settings
        fig = plt.figure(figsize=kwargs.get("figsize", (6,6)))

        xlabel = kwargs.get("xlabel", "")
        ylabel = kwargs.get("ylabel", "")
        title = kwargs.get("title", "")
        grid = kwargs.get("grid", False)

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.grid(visible=grid)

        # axes settings
        axes = plt.gca()

        std_min_xlim = np.nanmin(xdata[xdata != -np.inf])*2 
        std_max_xlim = np.nanmax(xdata[xdata != -np.inf])*2
        axes.set_xlim(kwargs.get("xlim_left", std_min_xlim), kwargs.get("xlim_right", std_max_xlim))


        std_min_ylim = np.nanmin(ydata[ydata != -np.inf])*2 
        std_max_ylim = np.nanmax(ydata[ydata != -np.inf])*2
        axes.set_ylim(kwargs.get("ylim_left", std_min_ylim), kwargs.get("ylim_right", std_max_ylim))

        axes.set_axisbelow(True)

        if animation:
            color = kwargs.get("color", "blue")
            radius = kwargs.get("radius", 0.1)
            lw = kwargs.get("linewidth", 1)
            
            current_point = plt.Circle((xdata[0], ydata[0]), radius=radius, color=color)
            axes.add_artist(current_point)

            tail_line = axes.plot([], [], color=color, lw=lw)[0]
            x_tail, y_tail = list(), list()

            steps = len(xdata)

            def step():
                current = 0
                while True:
                    current = (current + 1) % steps
                    if animation_tail:
                        x_tail.append(xdata[current])               # update tail x-data
                        y_tail.append(ydata[current])               # update tail y-data
                        if len(x_tail) > tail_length:               # clip tail
                            x_tail.pop(0)
                            y_tail.pop(0)                
                    yield (xdata[current], ydata[current])

            def animate(r):
                current_point.center = r
                tail_line.set_data(x_tail, y_tail)
                return current_point,tail_line
            
            interval = kwargs.get("anim_interval", 20)

            anim = FuncAnimation(fig, animate, step, interval=interval, blit=True, cache_frame_data=False)

            plt.show()

            if filename != None:
                dpi = kwargs.get("dpi", 200)
                if fileformat == Plotter.GIF_FORMAT:
                    anim.save(filename, "pillow", fps=save_fps, dpi=dpi)
                elif fileformat == Plotter.HTML_FORMAT:
                    anim.save(filename, "html", fps=save_fps, dpi=dpi)
                elif fileformat == Plotter.PNG_FORMAT:
                    label = kwargs.get("label", "")
                    color = kwargs.get("color", "blue")
                    plt.plot(xdata, ydata, label=label, color=color)
                    plt.title(label=title)
                    plt.xlabel(xlabel=xlabel)
                    plt.ylabel(ylabel=ylabel)
                    plt.grid(visible=grid)
                    plt.savefig(filename, dpi=dpi)
                else:
                    raise Exception(f"Given file format not recognized: {fileformat}")

        else:
            label = kwargs.get("label", "")
            color = kwargs.get("color", "blue")
            plt.plot(xdata, ydata, label=label, color=color)

            plt.show()

            if filename != None:
                dpi = kwargs.get("dpi", 200)
                match fileformat:
                    case Plotter.PNG_FORMAT:
                        plt.savefig(filename, dpi=dpi)
                    case _:
                        raise Exception(f"Unknown fileformat: {fileformat}")