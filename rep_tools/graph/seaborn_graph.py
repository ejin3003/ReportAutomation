import matplotlib.pyplot as plt
import seaborn as sns


class SnsGraph:
    """
    Class designed to create Seaborn Graph Objects
    Class Parameters SnsGraph(DataFrame, Title, Fig_Size=(#, #), Palette)
    Palette Options >>> "Blues_d", "plasma", "summer"
    """
    def __init__(self, df, title, fig_size, palette):
        self.df = df
        self.title = title
        self.fig_size = fig_size
        self.palette = palette

    def sns_bar_plot(self):
        x = self.df[self.df.columns[0]]
        y = self.df.index
        sns.set(rc={"figure.figsize": self.fig_size})
        ax = sns.barplot(x, y, data=self.df, palette=self.palette)
        ax.set_title(self.title)
        initial_x = 0
        for p in ax.patches:
            ax.text(p.get_width(), initial_x + p.get_height() / 8, "{:1.0f}".format(p.get_width()))
            initial_x += 1
        plt.show()
