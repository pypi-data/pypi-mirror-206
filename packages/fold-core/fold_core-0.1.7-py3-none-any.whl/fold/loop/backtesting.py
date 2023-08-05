# Copyright (c) 2022 - Present Myalo UG (haftungbeschränkt) (Mark Aron Szulyovszky, Daniel Szemerey) <info@dreamfaster.ai>. All rights reserved. See LICENSE in root folder.


from typing import Optional, Union

import pandas as pd
from tqdm.auto import tqdm

from ..base import OutOfSamplePredictions, TrainedPipelines
from ..splitters import Fold, Splitter
from ..utils.trim import trim_initial_nans_single
from .checks import check_types
from .common import deepcopy_pipelines, recursively_transform
from .types import Backend, Stage


def backtest(
    trained_pipelines: TrainedPipelines,
    X: Optional[pd.DataFrame],
    y: pd.Series,
    splitter: Splitter,
    backend: Union[Backend, str] = Backend.no,
    sample_weights: Optional[pd.Series] = None,
    silent: bool = False,
    mutate: bool = False,
) -> OutOfSamplePredictions:
    """
    Run backtest on TrainedPipelines and given data.

    Parameters
    ----------

    trained_pipelines: TrainedPipelines
        The fitted pipelines, for all folds.
    X: pd.DataFrame, optional
        Exogenous Data.
    y: pd.Series
        Endogenous Data (Target).
    splitter: Splitter
        Defines how the folds should be constructed.
    backend: str, Backend = Backend.no
        The library/service to use for parallelization / distributed computing, by default `no`.
    sample_weights: pd.Series, optional = None
        Weights assigned to each sample/timestamp, that are passed into models that support it, by default None.
    silent: bool = False
        Wether the pipeline should print to the console, by default False.
    mutate: bool = False
        Whether `trained_pipelines` should be mutated, by default False. This is discouraged.

    Returns
    -------
    OutOfSamplePredictions
        Predictions for all folds, concatenated.
    """
    backend = Backend.from_str(backend)
    X, y = check_types(X, y)

    results = [
        __backtest_on_window(
            trained_pipelines,
            split,
            X,
            y,
            sample_weights,
            backend,
            mutate=mutate,
        )
        for split in tqdm(splitter.splits(length=len(X)), disable=silent)
    ]
    return trim_initial_nans_single(pd.concat(results, axis="index"))


def __backtest_on_window(
    trained_pipelines: TrainedPipelines,
    split: Fold,
    X: pd.DataFrame,
    y: pd.Series,
    sample_weights: Optional[pd.Series],
    backend: Backend,
    mutate: bool,
) -> pd.DataFrame:
    current_pipeline = [
        pipeline_over_time.loc[split.model_index]
        for pipeline_over_time in trained_pipelines
    ]
    if not mutate:
        current_pipeline = deepcopy_pipelines(current_pipeline)

    X_test = X.iloc[split.test_window_start : split.test_window_end]
    y_test = y.iloc[split.test_window_start : split.test_window_end]
    sample_weights_test = (
        sample_weights.iloc[split.train_window_start : split.test_window_end]
        if sample_weights is not None
        else None
    )
    return recursively_transform(
        X_test,
        y_test,
        sample_weights_test,
        current_pipeline,
        stage=Stage.update_online_only,
        backend=backend,
    )
