# vizmetrics
## VizMetrics Library for AI Models
This is a library that provides tools to calculate various metrics for AI models, including accuracy, precision, recall, F1 score, ROC curve, and confusion matrix. It also includes functions to plot these metrics as graphs and figures.

## Features
Calculates common metrics for AI models
Plots ROC curves and confusion matrices
Provides easy-to-use functions to display metrics and plots

## Installation
To install the library, use pip:
```
pip install vizmetrics
```

## Usage
Here is an example of how to use the library to calculate and plot metrics for a binary classification model:

python
```
import vizmetrics

# Generate some example data
y_true = [0, 1, 0, 1, 0, 0, 1, 1]
y_pred = [0, 1, 0, 0, 1, 0, 1, 1]

# Example
vizmetrics.plot_confusion_matrix(y_true, y_pred)
vizmetrics.accuracy_confusion_matrix_precision_recall_multiclass(y_true, y_pred)
sens_multicalss = vizmetrics.sensitivity_multiclass(y_true, y_pred)


## License
This library is licensed under the MIT License.