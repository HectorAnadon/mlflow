from mlflow.metrics.base import (
    EvaluationExample,
    MetricValue,
)
from mlflow.metrics.genai.genai_metric import (
    make_genai_metric,
)
from mlflow.metrics.genai.metric_definitions import (
    answer_correctness,
    answer_relevance,
    answer_similarity,
    faithfulness,
)
from mlflow.metrics.metric_definitions import (
    _accuracy_eval_fn,
    _ari_eval_fn,
    _f1_score_eval_fn,
    _flesch_kincaid_eval_fn,
    _mae_eval_fn,
    _mape_eval_fn,
    _max_error_eval_fn,
    _mse_eval_fn,
    _precision_eval_fn,
    _r2_score_eval_fn,
    _recall_eval_fn,
    _rmse_eval_fn,
    _rouge1_eval_fn,
    _rouge2_eval_fn,
    _rougeL_eval_fn,
    _rougeLsum_eval_fn,
    _token_count_eval_fn,
    _toxicity_eval_fn,
)
from mlflow.models import (
    EvaluationMetric,
    make_metric,
)
from mlflow.utils.annotations import experimental


@experimental
def latency() -> EvaluationMetric:
    """
    This function will create a metric for calculating latency. Latency is determined by the time
    it takes to generate a prediction for a given input. Note that computing latency requires
    each row to be predicted sequentially, which will likely slow down the evaluation process.
    """
    return make_metric(
        eval_fn=lambda x: MetricValue(),
        greater_is_better=False,
        name="latency",
    )


# general text metrics
@experimental
def token_count() -> EvaluationMetric:
    """
    This function will create a metric for calculating token_count. Token count is calculated
    using tiktoken by using the `cl100k_base` tokenizer.
    """
    return make_metric(
        eval_fn=_token_count_eval_fn,
        greater_is_better=True,
        name="token_count",
    )


@experimental
def toxicity() -> EvaluationMetric:
    """
    This function will create a metric for evaluating `toxicity`_ using the model
    `roberta-hate-speech-dynabench-r4`_, which defines hate as "abusive speech targeting
    specific group characteristics, such as ethnic origin, religion, gender, or sexual
    orientation."

    The score ranges from 0 to 1, where scores closer to 1 are more toxic. The default threshold
    for a text to be considered "toxic" is 0.5.

    Aggregations calculated for this metric:
        - ratio (of toxic input texts)

    .. _toxicity: https://huggingface.co/spaces/evaluate-measurement/toxicity
    .. _roberta-hate-speech-dynabench-r4: https://huggingface.co/facebook/roberta-hate-speech-dynabench-r4-target
    """
    return make_metric(
        eval_fn=_toxicity_eval_fn,
        greater_is_better=False,
        name="toxicity",
        long_name="toxicity/roberta-hate-speech-dynabench-r4",
        version="v1",
    )


@experimental
def flesch_kincaid_grade_level() -> EvaluationMetric:
    """
    This function will create a metric for calculating `flesch kincaid grade level`_ using
    `textstat`_.

    This metric outputs a number that approximates the grade level needed to comprehend the text,
    which will likely range from around 0 to 15 (although it is not limited to this range).

    Aggregations calculated for this metric:
        - mean

    .. _flesch kincaid grade level:
        https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests#Flesch%E2%80%93Kincaid_grade_level
    .. _textstat: https://pypi.org/project/textstat/
    """
    return make_metric(
        eval_fn=_flesch_kincaid_eval_fn,
        greater_is_better=False,
        name="flesch_kincaid_grade_level",
        version="v1",
    )


@experimental
def ari_grade_level() -> EvaluationMetric:
    """
    This function will create a metric for calculating `automated readability index`_ using
    `textstat`_.

    This metric outputs a number that approximates the grade level needed to comprehend the text,
    which will likely range from around 0 to 15 (although it is not limited to this range).

    Aggregations calculated for this metric:
        - mean

    .. _automated readability index: https://en.wikipedia.org/wiki/Automated_readability_index
    .. _textstat: https://pypi.org/project/textstat/
    """
    return make_metric(
        eval_fn=_ari_eval_fn,
        greater_is_better=False,
        name="ari_grade_level",
        long_name="automated_readability_index_grade_level",
        version="v1",
    )


# question answering metrics
@experimental
def exact_match() -> EvaluationMetric:
    """
    This function will create a metric for calculating `accuracy`_ using sklearn.

    This metric only computes an aggregate score which ranges from 0 to 1.

    .. _accuracy: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html
    """
    return make_metric(
        eval_fn=_accuracy_eval_fn, greater_is_better=True, name="exact_match", version="v1"
    )


# text summarization metrics
@experimental
def rouge1() -> EvaluationMetric:
    """
    This function will create a metric for evaluating `rouge1`_.

    The score ranges from 0 to 1, where a higher score indicates higher similarity.
    `rouge1`_ uses unigram based scoring to calculate similarity.

    Aggregations calculated for this metric:
        - mean

    .. _rouge1: https://huggingface.co/spaces/evaluate-metric/rouge
    """
    return make_metric(
        eval_fn=_rouge1_eval_fn,
        greater_is_better=True,
        name="rouge1",
        version="v1",
    )


@experimental
def rouge2() -> EvaluationMetric:
    """
    This function will create a metric for evaluating `rouge2`_.

    The score ranges from 0 to 1, where a higher score indicates higher similarity.
    `rouge2`_ uses bigram based scoring to calculate similarity.

    Aggregations calculated for this metric:
        - mean

    .. _rouge2: https://huggingface.co/spaces/evaluate-metric/rouge
    """
    return make_metric(
        eval_fn=_rouge2_eval_fn,
        greater_is_better=True,
        name="rouge2",
        version="v1",
    )


@experimental
def rougeL() -> EvaluationMetric:
    """
    This function will create a metric for evaluating `rougeL`_.

    The score ranges from 0 to 1, where a higher score indicates higher similarity.
    `rougeL`_ uses unigram based scoring to calculate similarity.

    Aggregations calculated for this metric:
        - mean

    .. _rougeL: https://huggingface.co/spaces/evaluate-metric/rouge
    """
    return make_metric(
        eval_fn=_rougeL_eval_fn,
        greater_is_better=True,
        name="rougeL",
        version="v1",
    )


@experimental
def rougeLsum() -> EvaluationMetric:
    """
    This function will create a metric for evaluating `rougeLsum`_.

    The score ranges from 0 to 1, where a higher score indicates higher similarity.
    `rougeLsum`_ uses longest common subsequence based scoring to calculate similarity.

    Aggregations calculated for this metric:
        - mean

    .. _rougeLsum: https://huggingface.co/spaces/evaluate-metric/rouge
    """
    return make_metric(
        eval_fn=_rougeLsum_eval_fn,
        greater_is_better=True,
        name="rougeLsum",
        version="v1",
    )


# General Regression Metrics
def mae() -> EvaluationMetric:
    """
    This function will create a metric for evaluating `mae`_.

    This metric computes an aggregate score for the mean absolute error for regression.

    .. _mae: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html
    """
    return make_metric(
        eval_fn=_mae_eval_fn,
        greater_is_better=False,
        name="mean_absolute_error",
    )


def mse() -> EvaluationMetric:
    """
    This function will create a metric for evaluating `mse`_.

    This metric computes an aggregate score for the mean squared error for regression.

    .. _mse: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html
    """
    return make_metric(
        eval_fn=_mse_eval_fn,
        greater_is_better=False,
        name="mean_squared_error",
    )


def rmse() -> EvaluationMetric:
    """
    This function will create a metric for evaluating the square root of `mse`_.

    This metric computes an aggregate score for the root mean absolute error for regression.

    .. _mse: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html
    """

    return make_metric(
        eval_fn=_rmse_eval_fn,
        greater_is_better=False,
        name="root_mean_squared_error",
    )


def r2_score() -> EvaluationMetric:
    """
    This function will create a metric for evaluating `r2_score`_.

    This metric computes an aggregate score for the coefficient of determination. R2 ranges from
    negative infinity to 1, and measures the percentage of variance explained by the predictor
    variables in a regression.

    .. _r2_score: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html
    """
    return make_metric(
        eval_fn=_r2_score_eval_fn,
        greater_is_better=True,
        name="r2_score",
    )


def max_error() -> EvaluationMetric:
    """
    This function will create a metric for evaluating `max_error`_.

    This metric computes an aggregate score for the maximum residual error for regression.

    .. _max_error: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.max_error.html
    """
    return make_metric(
        eval_fn=_max_error_eval_fn,
        greater_is_better=False,
        name="max_error",
    )


def mape() -> EvaluationMetric:
    """
    This function will create a metric for evaluating `mape`_.

    This metric computes an aggregate score for the mean absolute percentage error for regression.

    .. _mape: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_percentage_error.html
    """
    return make_metric(
        eval_fn=_mape_eval_fn,
        greater_is_better=False,
        name="mean_absolute_percentage_error",
    )


# Binary Classification Metrics


def recall_score() -> EvaluationMetric:
    """
    This function will create a metric for evaluating `recall`_ for classification.

    This metric computes an aggregate score between 0 and 1 for the recall of a classification task.

    .. _recall: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html
    """
    return make_metric(eval_fn=_recall_eval_fn, greater_is_better=True, name="recall_score")


def precision_score() -> EvaluationMetric:
    """
    This function will create a metric for evaluating `precision`_ for classification.

    This metric computes an aggregate score between 0 and 1 for the precision of
    classification task.

    .. _precision: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html
    """
    return make_metric(eval_fn=_precision_eval_fn, greater_is_better=True, name="precision_score")


def f1_score() -> EvaluationMetric:
    """
    This function will create a metric for evaluating `f1_score`_ for binary classification.

    This metric computes an aggregate score between 0 and 1 for the F1 score (F-measure) of a
    classification task. F1 score is defined as 2 * (precision * recall) / (precision + recall).

    .. _f1_score: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html
    """
    return make_metric(eval_fn=_f1_score_eval_fn, greater_is_better=True, name="f1_score")


__all__ = [
    "EvaluationExample",
    "EvaluationMetric",
    "MetricValue",
    "make_metric",
    "flesch_kincaid_grade_level",
    "ari_grade_level",
    "accuracy",
    "rouge1",
    "rouge2",
    "rougeL",
    "rougeLsum",
    "toxicity",
    "make_genai_metric",
    "mae",
    "mse",
    "rmse",
    "r2_score",
    "max_error",
    "mape",
    "binary_recall",
    "binary_precision",
    "binary_f1_score",
    "answer_similarity",
    "faithfulness",
    "answer_correctness",
    "answer_relevance",
    "token_count",
    "latency",
]
