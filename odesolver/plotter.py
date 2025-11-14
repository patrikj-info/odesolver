import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

class Plotter():
    """
        Class for plotting the numerically attained solutions of ODEs.    
    """

    GIF_FORMAT = "GIF"
    HTML_FORMAT = "HTML"
    PNG_FORMAT = "PNG"


    def plot(data:np.ndarray, animated:bool, phase_space:bool = False, save:bool = False, filename:str = None, fileformat:str = None, xlabel:str = "", ylabel:str = "", title:str = "", fps:int = 60):
        """
            Function for plotting the obtained numeric solution of an ODE.

            Parameters
            ------------------
                data : np.ndarray
                    The numeric solution of an ODE.
                animated : bool
                    Animate the solution?
                phase_space : bool
                    Create phase space diagram from the obtained solution? (i.e. x' vs x instead of t vs x)
                save : bool
                    Save the created graph?
                filename : str
                    The filename of the saved graph.
                fileformat : str
                    The format of the saved graph, e.g. png or gif.
                xlabel : str
                    The x-label of the created graph.
                ylabel : str
                    The y-label of the created graph.
                title : str
                    The title of the created graph.
                fps : int
                    The FPS of the saved animation.
        """

        # should the plot be animated?
        if animated:

            # init the figure and axis
            anim_fig, anim_ax = plt.subplots()

            # get number of points -> is number of frames
            frames = data.shape[1]

            # load the data -> phase space diagram or normal solution plot?
            x = data[0]
            if phase_space:
                # get velocity (i.e. first derivative)
                x = data[2]
            y = data[1]

            # plotted data -> required for animation
            plot_x = x[0]
            plot_y = y[0]

            # plot line
            line = anim_ax.plot(plot_x, plot_y)[0]
            
            # axis settings
            anim_ax.set(xlim=[np.nanmin(x)*1.5, np.nanmax(x)*1.5], ylim=[np.nanmin(y)*1.5, np.nanmax(y)*1.5])
            
            # function for updating plot
            def update(frame):
                # append more data
                plot_x = x[:frame]
                plot_y = y[:frame]
                
                # set new data
                line.set_xdata(plot_x)
                line.set_ydata(plot_y)
                
                # return new line
                return line

            # create animation
            anim = FuncAnimation(fig=anim_fig, func=update, frames=frames, interval=1e-15)

            # plot settings
            plt.title(label=title)
            plt.xlabel(xlabel=xlabel)
            plt.ylabel(ylabel=ylabel)

            # show plot
            plt.show()

            # save plot?
            if save:
                if fileformat == Plotter.GIF_FORMAT:
                    anim.save(filename, "pillow", fps=fps, dpi=400)
                elif fileformat == Plotter.HTML_FORMAT:
                    anim.save(filename, "html", fps=fps, dpi=400)
                elif fileformat == Plotter.PNG_FORMAT:
                    plt.plot(x, y)
                    plt.title(label=title)
                    plt.xlabel(xlabel=xlabel)
                    plt.ylabel(ylabel=ylabel)
                    plt.savefig(filename, dpi=400)
                else:
                    raise Exception(f"Given file format not recognized: {fileformat}")


        else:
            # load data
            x = data[0]
            y = data[1] 
            if phase_space:
                # phase space diagram?
                x = data[2] # get first derivative (i.e. velocity)

            plt.plot(x,y)
            plt.title(label=title)
            plt.xlabel(xlabel)
            plt.xlabel(ylabel)
            plt.show()           

            if save:
                plt.savefig(filename, dpi=400)
