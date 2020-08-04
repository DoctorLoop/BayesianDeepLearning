violin_parts = plt.violinplot(underdone['time'], positions=[0], showmeans=True)
# over-ride default blue color, you can't use 'color' parameter as can on histograms etc
for pc in violin_parts['bodies']: # used to
    pc.set_facecolor('red')
    violin_parts['cbars'].set_edgecolor('red')
    violin_parts['cmaxes'].set_edgecolor('red')
    violin_parts['cmins'].set_edgecolor('red')
    violin_parts['cmeans'].set_edgecolor('red')
    plt.violinplot(softboiled['time'], positions=[0.5], showmeans=True)
    plt.violinplot(hardboiled['time'], positions=[1], showmeans=True)
    plt.ylabel("time")
    plt.xticks([0,0.5,1],["underdone", "soft", "hard"])
