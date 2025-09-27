import json

import numpy as np
from pprint import pprint
from pathlib import Path
from matplotlib import pyplot as plt


def get_search_results(algo, dir="query1_cache", top_n=20):
    def get_ranking(cache_file):
        if cache_file.exists():
            with open(cache_file) as f:
                result = json.load(f)
        else:
            raise FileNotFoundError(f'Cache file {cache_file} not found')

        # Considering only the top_n rankings of the results
        _ranking = [x['link'] for x in result['organic_results']]
        return _ranking

    cache_dir = Path(f'{dir}')
    cache_dir.mkdir(parents=True, exist_ok=True)

    cache_file_path = cache_dir.joinpath(f'{algo}.json')
    ranking = get_ranking(cache_file_path)[:top_n]
    print(f'Number of search results: {len(ranking)}')
    pprint(ranking)

    return ranking


def precision_recall(retrieved_docs, relevant_docs):
    relevant_retrieved_docs = sum(1 for doc in retrieved_docs if doc in relevant_docs)

    p = relevant_retrieved_docs / relevant_docs # precision
    r = relevant_retrieved_docs / retrieved_docs # recall
    return p, r


def precision_at_11_standard_recall_levels(retrieved_docs, relevant_docs):
    pr_values_for_relevant_retrieved_docs = []  # List of tuples
    for idx, doc in enumerate(retrieved_docs):
        if doc in relevant_docs:
            pr_values_for_relevant_retrieved_docs.append(precision_recall(retrieved_docs[:idx + 1], relevant_docs))

    p_values, r_values = [], []
    # TODO: Implement this function to compute the precision values for the 11 standard recall levels
    # INSERT YOUR CODE HERE
    return r_values, p_values


def plot_precision_vs_recall_curve(p_values, r_values, plt_title=None):
    plt.figure()
    plt.plot(r_values, p_values, marker='.')
    if plt_title:
        plt.title(plt_title)
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.ylim([-0.1, 1.1])
    
    plots_dir = Path(f'plots')
    plots_dir.mkdir(parents=True, exist_ok=True)

    # make plt_title suitable for file name
    plt_title = plt_title.replace('\n', ' ').replace(':', ' -').replace('/', '-').replace('?', '').replace(' ', '_')
    plt.savefig(f'plots/{plt_title}.png')
    plt.show()
    plt.close()


def f_metric(retrieved_docs, relevant_docs):
    p, r = precision_recall(retrieved_docs, relevant_docs)

    f_score = (2 * (p * r)) / (p + r)
    return f_score


def p_at_5():
    # TODO: implement this function
    p = None
    return p


def p_at_10():
    #TODO: implement this function
    p = None
    return p


def run_all_parts(dir):
    search_results = {
        'google': get_search_results('google', dir, top_n=7),
        'bing': get_search_results('bing', dir, top_n=20),
        'duckduckgo': get_search_results('duckduckgo', dir, top_n=20),
        'yahoo': get_search_results('yahoo', dir, top_n=20)
    }

    # Relevant documents (Let's create a baseline using results from Google search)
    relevant_docs = set(search_results['google'])

    # Precision and Recall
    print('\nThe precision and recall scores for the various search algorithms with Google search as the baseline:')
    for ranking_name, retrieved_docs in search_results.items():
        # call the precision_recall function with the proper arguments
        p, r = precision_recall(retrieved_docs, relevant_docs)
        print(f'{ranking_name.ljust(11)} ranking  ==>  precision: {round(p, 2)} \t recall: {round(r, 2)}')

    # Precision vs Recall Plots
    print('\nPlotting precision vs recall plots')
    for ranking_name, retrieved_docs in search_results.items():
        #TODO: call these functions with the proper parameters
        r_values, p_values = precision_at_11_standard_recall_levels()
        plot_title = (f'Precision vs Recall plot for {ranking_name} ranking\n'
                      f'considering Google search as the baseline')
        plot_precision_vs_recall_curve(p_values, r_values, plot_title)

    # Single valued Summaries
    print('\nComputing the single valued summaries')
    for ranking_name, retrieved_docs in search_results.items():
        # TODO: call these functions with the proper parameters
        f_score = f_metric(retrieved_docs, relevant_docs)
        p_at_5_score = p_at_5()
        p_at_10_score = p_at_10()
        print(f'{ranking_name.ljust(11)}   ==>  f: {round(f_score, 2)} '
              f'\t p@5: {round(p_at_5_score, 2)} \t p@10: {round(p_at_10_score, 2)}')


if __name__ == '__main__':
    print('Running for query1_cache')
    run_all_parts(dir = 'query1_cache')
    print('\nRunning for query2_cache')
    run_all_parts(dir = 'query2_cache')
