import matplotlib.pyplot as plt

def calculate_value(fitness, best):
    return ((fitness - best) / best)

def ecdf_inf(vectors, column, n_instances : int = 402, labels : list[str] = [], instances : list[str] = [], x_lim = (-0.1, 1.0), xlabel : str = None, ylabel : str = None, marker_frequence : int = 10, markers :list[str] = ['x', 'o', '^', '>', 'v', '<', '*']):
    plot_vectors = []
    for vector in vectors:
        plot_vectors.append([[0.0],[0.0]])
        i = 1
        while i < len(vector):
            if vector[i] == float('inf'):
                break
            if vector[i] == -float('inf'):
                break
            while i < len(vector) and vector[i] == vector[i-1]:
                i += 1
            plot_vectors[-1][0].append(vector[i-1])
            plot_vectors[-1][1].append((i-1)/n_instances)
            i += 1
    for i in range(len(vectors)):
        if i >= len(markers):
            print(f'NOTE: not enough markers defined, recycling already used markers for {labels[i]}')
        plt.plot(plot_vectors[i][0], plot_vectors[i][1], label=[labels[i]], marker=markers[i%len(markers)], markevery=list(range(0, len(plot_vectors[i][0]), max(1, int(len(plot_vectors[i][0])/marker_frequence)))))
    plt.xlim(x_lim[0], x_lim[1])
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True, 'both')
    plt.title(column)
    plt.show()

def get_plot_vectors(data : dict[str, list[float]], delta_scope : float = 1.0) -> tuple[list[float], list[str]]:
    plot_data = dict()
    best_results = dict()
    example = list(data.keys())[0]
    for key in data[example].keys():
        best = float('inf')
        best_results[key] = best
        plot_data[key] = dict()
        for solver in data.keys():
            if key in data[solver] and data[solver][key] < best:
                best = data[solver][key]
                best_results[key] = best
        for solver in data.keys():
            if key in data[solver]:
                plot_data[key][solver] = max(calculate_value(data[solver][key], best * delta_scope), 0)
            else:
                plot_data[key][solver] = float('inf')
    vectors = []
    labels = []
    for solver in data.keys():
        labels.append(solver)
        vector = []
        for instance in data[example].keys():
            vector.append(plot_data[instance][solver])
        vector.sort()
        vectors.append(vector)
    return vectors, labels

def visualize_gaps(data : dict[str, list[float]], title : str = 'Fitness', n_instances : int = 1000,  x_lim_lb=-0.1, x_lim_ub=1.75, delta_scope : float = 1.0) -> None:
    plot_vectors, labels = get_plot_vectors(data, delta_scope)
    if delta_scope < 1.0:
        plot_title = title + ' $\delta_{rel}$ <= '+ f'{(1.0-delta_scope)*100:.2f}%'
    else:
        plot_title = title + ' $\delta_{rel}$'
    ecdf_inf(plot_vectors, plot_title, labels=labels, n_instances=n_instances, x_lim=(x_lim_lb, x_lim_ub), xlabel='$\delta_{rel}$', ylabel='Portion of Instances $\leq\delta_{rel}$')

def progress_plot(fitness_data : list[float], timestamps : list[float], labels : list[str], title : str, marker_frequence : int = 10, markers :list[str] = ['x', 'o', '^', '>', 'v', '<', '*'], xlim_lb : float = -0.01, xlim_ub : float = None) -> None:
    n = 0
    for i in range(len(labels)):
        x = timestamps[i]
        y = fitness_data[i]
        label = labels[i]
        if max(x) > n:
            n = max(x)
        if i >= len(markers):
            print(f'NOTE: not enough markers defined, recycling already used markers for {labels[i]}')
        plt.plot(x, y, label=[label], marker=markers[i%len(markers)], markevery=list(range(0, len(x), max(1, int(len(x)/marker_frequence)))))
    if not xlim_ub:
        xlim_ub = n
    plt.xlim(xlim_lb, xlim_ub)
    plt.legend()
    plt.grid(True, 'both')
    plt.xlabel('$t$')
    plt.ylabel('$\delta_{rel}$')
    plt.title(title)
    plt.show()


def visualize_timeline(data : dict[str, list[tuple[float, float]]], title : str = 'Progress', delta_scope : float = 1.0, xlim_lb = None, xlim_ub = None) -> None:
    fitness_data = []
    timestamps = []
    labels = []
    best = float('inf')
    for solver in data:
        for entry in data[solver]:
            if entry[1] < best:
                best = entry[1]
    for solver in data:
        labels.append(solver)
        fitness_data.append([max(calculate_value(entry[1], best * delta_scope), 0) for entry in data[solver]])
        timestamps.append([entry[0] for entry in data[solver]])
    if delta_scope < 1.0:
        plot_title = title + ' $\delta_{rel}$ <= '+ f'{(1.0-delta_scope)*100:.2f}%'
    else:
        plot_title = title + ' $\delta_{rel}$'
    progress_plot(fitness_data=fitness_data, timestamps=timestamps, labels=labels, title=plot_title, xlim_lb=xlim_lb, xlim_ub=xlim_ub)


def rank_plot(data : dict[str, dict[str, tuple[float,float]]]) -> None:
    import pandas as pd
    from autorank import autorank, plot_stats
    plt_data = dict()
    instances = []
    for solver in data:
        for instance in data[solver]:
            if instance not in instances:
                instances.append(instance)
    for solver in data:
        plt_data[solver] = []
        for instance in instances:
            if instance in data[solver]:
                plt_data[solver].append(data[solver][instance][-1][1])
            else:
                plt_data[solver].append(float('inf'))
    df = pd.DataFrame()
    for solver in plt_data:
        df[solver] = plt_data[solver]
    result = autorank(df, alpha=0.05, verbose=False, order='ascending')
    plot_stats(result)
    plt.show()