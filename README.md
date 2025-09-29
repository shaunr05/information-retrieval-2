# Information Retrieval Evaluation Lab

This project implements fundamental retrieval evaluation metrics to critically evaluate and compare search results from different search engines. The system evaluates cached search results from Bing, DuckDuckGo, Google, and Yahoo using standard information retrieval evaluation techniques.

---

## Requirements

Before running the project, make sure Python 3.10 or higher is installed. Install the packages required for this project using:

```bash
pip install -r requirements.txt 
```

## Project Structure

The project contains cached search results in JSON format for two different queries:
- `query1_cache/`: Results for "Modern Information Retrieval"
- `query2_cache/`: Results for "information retrieval evaluation"

Each directory contains cached results from four search engines:
- `bing.json`
- `duckduckgo.json`
- `google.json`
- `yahoo.json`

## Running the code

The project includes Docker configuration for consistent execution. To run with Docker:

```bash
docker compose up --build
```

The `--build` flag ensures that images are rebuilt if any changes occurred.

### Redirecting Output

Output is redirected to a file for easier analysis:

```bash
python main.py > results.txt
```

## Output

The program generates several types of output:

### Console Output
- Detailed search results for each algorithm
- Precision and recall scores for each search engine
- Single-valued summary metrics (F-measure, P@5, P@10)

### Plot Generation
Precision vs Recall plots are automatically saved to the `plots/` directory:
- Individual plots for each search engine comparison
- Plots for both query datasets
- PNG format with descriptive filenames

