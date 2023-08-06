import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class boxplot:
    def __init__(self, data, x_col, y_col, title="", xlabel="", ylabel=""):
        self.data = data
        self.x_col = x_col
        self.y_col = y_col
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

        self.fig, self.ax = plt.subplots()
        plt.xticks(rotation=45)
        self.boxplot = self.ax.boxplot([self.data[self.data[self.x_col] == x][self.y_col] for x in self.data[self.x_col].unique()], labels=self.data[self.x_col].unique())
        self.annotations = []
        self.min_line = None
        self.max_line = None
        for i, box in enumerate(self.boxplot["boxes"]):
            annotation = self.ax.annotate("", xy=(0,0), xytext=(20,20), textcoords="offset points",
                            bbox=dict(boxstyle="round", facecolor="w", alpha=0.8),
                            arrowprops=dict(arrowstyle="-|>", fc="w", ec="k", lw=1.5, alpha=0.8))
            self.annotations.append(annotation)
        self.ax.set_title(self.title)
        self.ax.set_xlabel(self.xlabel)
        self.ax.set_ylabel(self.ylabel)
        self.jitter_flags = [False] * len(self.boxplot["boxes"])  # initialize jitter flags

        self.cid = self.fig.canvas.mpl_connect("motion_notify_event", self.on_hover)
        self.fig.canvas.mpl_connect("button_press_event", self.on_clickright)
        self.fig.canvas.mpl_connect("button_press_event", self.onclick)
        self.fig.canvas.mpl_connect("button_press_event", self.on_double_click)
        self.fig.canvas.mpl_connect("button_press_event", self.on_double_click_right)
        
    def _process_data(self):
        if self.x_col:
            self.groups = self.data.groupby(self.x_col)
        else:
            self.groups = {"": self.data}
        
    def _create_plot(self):
        self.boxplot = self.ax.boxplot([group[self.y_col] for _, group in self.groups], 
                                       labels=[name for name, _ in self.groups],
                                       patch_artist=True)
        
        
        self.annotations = []
        for i, box in enumerate(self.boxplot["boxes"]):
            annotation = self.ax.annotate("", xy=(0,0), xytext=(20,20), textcoords="offset points",
                            bbox=dict(boxstyle="round", facecolor="w", alpha=0.8),
                            arrowprops=dict(arrowstyle="-|>", fc="w", ec="k", lw=1.5, alpha=0.8))
            self.annotations.append(annotation)
        self.ax.set_xlabel(self.x_col)
        self.ax.set_ylabel(self.y_col)
        self.ax.set_title(f"Boxplot of {self.y_col} by {self.x_col}")
        
    def on_hover(self, event):
        if event.inaxes == self.ax:
            for i, box in enumerate(self.boxplot["boxes"]):
                if box.contains(event)[0]:
                    x = self.data[self.data[self.x_col] == self.ax.get_xticklabels()[i].get_text()][self.y_col]
                    q1, median, q3 = np.percentile(x, [25, 50, 75])
                    iqr = q3 - q1
                    upper_fence = q3 + 1.5*iqr
                    lower_fence = q1 - 1.5*iqr
                    minimum, maximum = x.min(), x.max()
                    self.annotations[i].set_text(f"Box {i+1}\n\n"
                                                 f"Min: {minimum:.2f}\n"
                                                 f"Q1: {q1:.2f}\n"
                                                 f"Median: {median:.2f}\n"
                                                 f"Q3: {q3:.2f}\n"
                                                 f"Max: {maximum:.2f}\n"
                                                 f"Upper fence: {upper_fence:.2f}\n"
                                                 f"Lower fence: {lower_fence:.2f}")
                    self.annotations[i].xy = (box.get_xdata()[0], box.get_ydata()[0])
                    self.annotations[i].set_visible(True)
                else:
                    self.annotations[i].set_visible(False)
        self.fig.canvas.draw_idle()
        
    def on_clickright(self, event):
        if event.button == 3 and event.inaxes == self.ax:
            for i, box in enumerate(self.boxplot["boxes"]):
                if box.contains(event)[0]:
                    x = self.data[self.data[self.x_col] == self.ax.get_xticklabels()[i].get_text()][self.y_col]
                    fig, ax = plt.subplots()
                    ax.hist(x, alpha=0.5, edgecolor='black', linewidth=1.2)
                    ax.axvline(x.mean(), color='r', linestyle='dashed', linewidth=1.5)
                    ax.set_xlabel('Value')
                    ax.set_ylabel('Frequency')
                    ax.set_title(f'Histogram of Box {i+1} Observations')
                    plt.show()
                    
                    arrow_x = box.get_xdata()[0] + 0.5 * box.get_linewidth()
                    arrow_y = x.mean()
                    #arrow_text = f"Box {i+1} Mean: {arrow_y:.2f}"
                    self.ax.annotate( xy=(arrow_x, arrow_y), xytext=(arrow_x, arrow_y+0.5),
                                      ha='center', va='bottom', color='r', arrowprops=dict(arrowstyle="-", color="gray"))
                    
                    break
                
    def onclick(self, event):
        if event.button == 1 and event.inaxes == self.ax:
            for i, box in enumerate(self.boxplot["boxes"]):
                if box.contains(event)[0]:
                    x = self.data[self.data[self.x_col] == self.ax.get_xticklabels()[i].get_text()][self.y_col]
                    if not self.jitter_flags[i]:  # jitter data points and set jitter flag to True
                        jitter_points = self.ax.plot(np.random.normal(i+1, 0.04, size=len(x)), x, ".", alpha=0.3, color="#89CFF0")
                        self.jitter_flags[i] = True
                        self.boxplot["boxes"][i].jitter_points = jitter_points
                    else:  # remove jitter and set jitter flag to False
                        if hasattr(self.boxplot["boxes"][i], "jitter_points"):
                            for jitter_point in self.boxplot["boxes"][i].jitter_points:
                                jitter_point.remove()
                            del self.boxplot["boxes"][i].jitter_points
                        self.jitter_flags[i] = False
                    self.fig.canvas.draw_idle()
                    
    def on_double_click(self, event):
        if event.button == 1 and event.dblclick and event.inaxes == self.ax:
            x = []
            y = []
            for i, box in enumerate(self.boxplot["boxes"]):
                x_val = box.get_xdata().mean()
                y_val = min(self.data[self.data[self.x_col] == self.ax.get_xticklabels()[i].get_text()][self.y_col])
                x.append(x_val)
                y.append(y_val)

            x_sorted, y_sorted = zip(*sorted(zip(x, y)))
        
            if self.min_line:
                self.min_line.remove()
                self.min_line = None
            else:
                self.min_line, = self.ax.plot(x_sorted, y_sorted, '-o', color='#088F8F')
        
            self.fig.canvas.draw_idle()
            
    def on_double_click_right(self, event):
        if event.button == 3 and event.dblclick and event.inaxes == self.ax:
            x = []
            y = []
            for i, box in enumerate(self.boxplot["boxes"]):
                x_val = box.get_xdata().mean()
                y_val = max(self.data[self.data[self.x_col] == self.ax.get_xticklabels()[i].get_text()][self.y_col])
                x.append(x_val)
                y.append(y_val)

            x_sorted, y_sorted = zip(*sorted(zip(x, y)))

            if self.max_line:
                self.max_line.remove()
                self.max_line = None
            else:
                self.max_line, = self.ax.plot(x_sorted, y_sorted, '-o', color='#6495ED')

            self.fig.canvas.draw_idle()
    
        
    def show(self):
        self.fig.canvas.mpl_connect("button_press_event", self.on_double_click)
        self.fig.canvas.mpl_connect("button_press_event", self.on_double_click_right)
        self.fig.canvas.mpl_connect("motion_notify_event", self.on_hover)
        self.fig.canvas.mpl_connect("button_press_event", self.onclick)
        plt.show()



        
