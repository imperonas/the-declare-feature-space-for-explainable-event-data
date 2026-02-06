# Miscellaneous notebooks

This folder contains exploratory and supporting notebooks that are not part of the core experiment pipeline.
They are useful for data preparation, visualization, and prototype analyses.
Use these notebooks to understand intermediate steps, sanity-check assumptions, and create auxiliary artifacts.
Their outputs are typically not used directly in the paper but can inform the experimental design.

## Notebooks

- `conformance_checking.ipynb`: Runs conformance checking on prepared logs and inspects results.
- `declare_discovery.ipynb`: Prototype for Declare constraint discovery and inspection.
- `declerative_feature_space.ipynb`: Early exploration of the declarative feature space construction.
- `rnn_sequence_classifier_train.ipynb`: Trains the sequence classifier used by some experiments.
- `visualize_dfg.ipynb`: Visualizes directly-follows graphs (DFGs) for selected logs.

## Suggested usage

- Start with `declerative_feature_space.ipynb` if you want to understand how features are derived from Declare constraints.
- Use `declare_discovery.ipynb` to prototype or debug discovery parameters before integrating them into experiments.
- Run `rnn_sequence_classifier_train.ipynb` when you need to retrain or update the sequence model.
- Use `visualize_dfg.ipynb` for quick, qualitative inspection of process behavior across logs.

## Data and outputs

- Input samples for conformance checking are under `conformance_checking_data/input/`.
- Generated outputs are stored in `conformance_checking_data/output/` or under `results_dfg_visualizing/`.
- Trained model artifacts are stored in `rnn_model/`.
- Intermediate figures or debug prints may be saved alongside the notebook that generated them.
