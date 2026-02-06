# Experiments: The Declare Feature Space for Explainable Event Data

This repository contains the code and resources required to reproduce the experimental results presented in the paper "The Declare Feature Space for Explainable Event Data".

## Overview

Complex temporal dependencies in event data often hinder the interpretability of machine learning models. This research proposes a feature space grounded in the declarative modeling language Declare (based on Linear Temporal Logic over finite traces) to abstract raw event sequences into interpretable behavioral constraints. This repository demonstrates the feasibility of this approach in generating semantic explanations.

## Contents

The experiments are organized into self-contained Jupyter notebooks corresponding to the two main application scenarios discussed in the paper:

* **explaining_event_data_clustering_results.ipynb**: Addresses the unsupervised learning use case. It demonstrates how to cluster event data (specifically the BPI Challenge 2020 dataset) and apply data-driven constraint mining to generate concise, rule-based explanations for the resulting clusters.
* **explaining_RNN_event_sequence_conformance_prediction.ipynb**: Addresses the supervised learning use case. It trains a Recurrent Neural Network (RNN) for conformance prediction on the Road Traffic Fine Management dataset and applies a domain-driven constraint selection strategy to explain model predictions.
