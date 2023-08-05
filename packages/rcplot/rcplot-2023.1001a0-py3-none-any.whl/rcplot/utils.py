from sklearn.metrics import f1_score, accuracy_score
from sklearn.utils import column_or_1d, check_consistent_length
from sklearn.preprocessing import label_binarize

import numpy as np
import pandas as pd


# Code to generate mean average error in cover estimates for each class and the 95% confidence interval (using bootstrapping)
def bootstrap_MAE_ci(x, name, confidence=0.95):
    MAE = x.mean()
    values = [np.random.choice(x, len(x), replace=True).mean() for i in range(1000)]
    pcs = np.percentile(values, [100 * (1 - confidence) / 2, 100 * (1 - (1 - confidence) / 2)])
    return pd.Series({"{}_MAE".format(name): MAE, "{}_lower".format(name): pcs[0], "{}_upper".format(name): pcs[1]})

def MAE_cover_error_bootstrap(df, col, true_col, image_col):
    dfp = df[[image_col, true_col, col]]
    tmpdf = pd.DataFrame(dfp.groupby(image_col)[true_col].value_counts(normalize=True))
    tmpdf.columns = ["{}_cover".format(true_col)]
    tmpdf_pred = pd.DataFrame(dfp.groupby(image_col)[col].value_counts(normalize=True))
    tmpdf_pred.columns = ["col_cover"]
    tmpdf_pred.reset_index(inplace=True)

    cover_df = tmpdf.join(
        tmpdf_pred.rename({col: true_col}, axis=1).set_index([image_col, true_col])).reset_index().fillna(0)
    ce = cover_df.assign(cover_error=np.abs(cover_df["{}_cover".format(true_col)] - cover_df["col_cover"]))[
        [true_col, "cover_error"]]
    out = ce.groupby(true_col)["cover_error"].apply(lambda x: bootstrap_MAE_ci(x, col)).unstack()
    return out


def error_per_image(df, true_col, col, image_col):
    dfp = df[[image_col, true_col, col]]
    tmpdf = pd.DataFrame(dfp.groupby(image_col)[true_col].value_counts(normalize=True))
    tmpdf.columns = ["{}_cover".format(true_col)]
    tmpdf_pred = pd.DataFrame(dfp.groupby(image_col)[col].value_counts(normalize=True))
    tmpdf_pred.columns = ["col_cover"]
    tmpdf_pred.reset_index(inplace=True)

    cover_df = tmpdf.join(
      tmpdf_pred.rename({col: true_col}, axis=1).set_index([image_col, true_col])).reset_index().fillna(0)
    ce = cover_df.assign(cover_error=np.abs(cover_df["{}_cover".format(true_col)] - cover_df["col_cover"]))[
      [image_col, true_col, "cover_error"]]
    return ce


def binarise_df_class(df, cls,y_true_col="human_classification", y_pred_col="model_classification",
                 score_col="model_classification_score"):
    y_trues = df[y_true_col].apply(lambda x: 1  if x==cls else 0)
    y_preds = df[y_pred_col].apply(lambda x: 1  if x==cls else 0)

    out = pd.DataFrame(y_trues).rename({y_true_col:"y_true"}, axis=1).join(pd.DataFrame(y_preds).rename({y_pred_col:"y_pred"}, axis=1)).join(df[[score_col]])
    return out

def binarise_df_class_f1(df, cls,y_true_col="human_classification", y_pred_col="model_classification"):
    y_trues = df[y_true_col].apply(lambda x: 1  if x==cls else 0)
    y_preds = df[y_pred_col].apply(lambda x: 1  if x==cls else 0)

    out = pd.DataFrame(y_trues).rename({y_true_col:"y_true"}, axis=1).join(pd.DataFrame(y_preds).rename({y_pred_col:"y_pred"}, axis=1))
    return out

def pred2f1(df, y_true_col="human_classification", y_pred_col="model_classification"):
    metrics = []

    # calculate overall metrics
    metrics.append({"Class": "OVERALL",
                        "Support": len(df),
                        "F1_score": f1_score(df[y_true_col], df[y_pred_col], average="weighted")
                    }
                   )
    for cl in df[y_true_col].unique():
        cldf = binarise_df_class_f1(df,cl, y_true_col=y_true_col, y_pred_col=y_pred_col) #df[df[y_true_col] == cl]

        metrics.append({"Class": cl,
                        "Support": sum(cldf["y_true"]),
                        "F1_score": f1_score( cldf["y_true"], cldf["y_pred"] )
                        }
                       )

    return pd.DataFrame(metrics)

def pred2cal(df, y_true_col="human_classification", y_pred_col="model_classification",
                 score_col="model_classification_score"):
    metrics = []

    # calculate overall metrics

    test_true = df.apply(lambda row: 1 if row[y_true_col] == row[y_pred_col] else 0, axis=1)
    pt, pp, ece = custom_calibration_curve(test_true, df[score_col])

    metrics.append({"Class": "OVERALL",
                    "Support": len(df),
                    "Prob_True": pt,
                    "Prob_Pred": pp})

    for cl in df[y_true_col].unique():
        cldf = binarise_df_class(df,cl, y_true_col=y_true_col, y_pred_col=y_pred_col, score_col=score_col) #df[df[y_true_col] == cl]
        test_true = cldf.apply(lambda row: 1 if row["y_true"] == row["y_pred"] else 0, axis=1)
        pt, pp, ece = custom_calibration_curve(test_true, cldf[score_col])

        metrics.append({"Class": cl,
                        "Support": sum(cldf["y_true"]),
                        "Prob_True": pt,
                        "Prob_Pred": pp})

    return pd.DataFrame(metrics)

def pred2metrics(df, y_true_col="human_classification", y_pred_col="model_classification",
                 score_col="model_classification_score"):
    metrics = []

    # calculate overall metrics

    test_true = df.apply(lambda row: 1 if row[y_true_col] == row[y_pred_col] else 0, axis=1)
    pt, pp, ece = custom_calibration_curve(test_true, df[score_col])

    metrics.append({"Class": "OVERALL",
                    "Support": len(df),
                    "F1_score": f1_score(df[y_true_col], df[y_pred_col], average="weighted"),
                    "accuracy": accuracy_score(df[y_true_col], df[y_pred_col]),
                    "Prob_True": pt,
                    "Prob_Pred": pp})

    for cl in df[y_true_col].unique():
        cldf = binarise_df_class(df,cl, y_true_col=y_true_col, y_pred_col=y_pred_col, score_col=score_col) #df[df[y_true_col] == cl]
        test_true = cldf.apply(lambda row: 1 if row["y_true"] == row["y_pred"] else 0, axis=1)
        pt, pp, ece = custom_calibration_curve(test_true, cldf[score_col])

        metrics.append({"Class": cl,
                        "Support": sum(cldf["y_true"]),
                        "F1_score": f1_score( cldf["y_true"], cldf["y_pred"] ),#cldf[y_true_col], cldf[y_pred_col], average="weighted"),
                        "accuracy": accuracy_score(cldf["y_true"], cldf["y_pred"]),
                        "Prob_True": pt,
                        "Prob_Pred": pp})

    return pd.DataFrame(metrics)

def custom_calibration_curve(y_true, y_prob, *, normalize=False, n_bins=5,
                             strategy='uniform'):
    """Compute true and predicted probabilities for a calibration curve.

    The method assumes the inputs come from a binary classifier, and
    discretize the [0, 1] interval into bins.

    Calibration curves may also be referred to as reliability diagrams.

    Read more in the :ref:`User Guide <calibration>`.

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True targets.

    y_prob : array-like of shape (n_samples,)
        Probabilities of the positive class.

    normalize : bool, default=False
        Whether y_prob needs to be normalized into the [0, 1] interval, i.e.
        is not a proper probability. If True, the smallest value in y_prob
        is linearly mapped onto 0 and the largest one onto 1.

    n_bins : int, default=5
        Number of bins to discretize the [0, 1] interval. A bigger number
        requires more data. Bins with no samples (i.e. without
        corresponding values in `y_prob`) will not be returned, thus the
        returned arrays may have less than `n_bins` values.

    strategy : {'uniform', 'quantile'}, default='uniform'
        Strategy used to define the widths of the bins.

        uniform
            The bins have identical widths.
        quantile
            The bins have the same number of samples and depend on `y_prob`.

    Returns
    -------
    prob_true : ndarray of shape (n_bins,) or smaller
        The proportion of samples whose class is the positive class, in each
        bin (fraction of positives).

    prob_pred : ndarray of shape (n_bins,) or smaller
        The mean predicted probability in each bin.

    References
    ----------
    Alexandru Niculescu-Mizil and Rich Caruana (2005) Predicting Good
    Probabilities With Supervised Learning, in Proceedings of the 22nd
    International Conference on Machine Learning (ICML).
    See section 4 (Qualitative Analysis of Predictions).

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.calibration import calibration_curve
    >>> y_true = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1])
    >>> y_pred = np.array([0.1, 0.2, 0.3, 0.4, 0.65, 0.7, 0.8, 0.9,  1.])
    >>> prob_true, prob_pred = calibration_curve(y_true, y_pred, n_bins=3)
    >>> prob_true
    array([0. , 0.5, 1. ])
    >>> prob_pred
    array([0.2  , 0.525, 0.85 ])
    """
    y_true = column_or_1d(y_true)
    y_prob = column_or_1d(y_prob)
    check_consistent_length(y_true, y_prob)

    if normalize:  # Normalize predicted values into interval [0, 1]
        y_prob = (y_prob - y_prob.min()) / (y_prob.max() - y_prob.min())
    elif y_prob.min() < 0 or y_prob.max() > 1:
        raise ValueError("y_prob has values outside [0, 1] and normalize is "
                         "set to False.")

    labels = np.unique(y_true)
    if len(labels) > 2:
        raise ValueError("Only binary classification is supported. "
                         "Provided labels %s." % labels)
    y_true = label_binarize(y_true, classes=labels)[:, 0]

    if strategy == 'quantile':  # Determine bin edges by distribution of data
        quantiles = np.linspace(0, 1, n_bins + 1)
        bins = np.percentile(y_prob, quantiles * 100)
        bins[-1] = bins[-1] + 1e-8
    elif strategy == 'uniform':
        bins = np.linspace(0., 1. + 1e-8, n_bins + 1)
    else:
        raise ValueError("Invalid entry to 'strategy' input. Strategy "
                         "must be either 'quantile' or 'uniform'.")

    binids = np.digitize(y_prob, bins) - 1

    bin_sums = np.bincount(binids, weights=y_prob, minlength=len(bins))
    bin_true = np.bincount(binids, weights=y_true, minlength=len(bins))
    bin_total = np.bincount(binids, minlength=len(bins))

    nonzero = bin_total != 0
    prob_true = bin_true[nonzero] / bin_total[nonzero]
    prob_pred = bin_sums[nonzero] / bin_total[nonzero]

    ece = np.sum(np.abs(prob_true - prob_pred) * (bin_total[nonzero] / len(y_true)))

    return prob_true, prob_pred, ece