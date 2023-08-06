# Copyright (c) 2022 - Present Myalo UG (haftungbeschränkt) (Mark Aron Szulyovszky, Daniel Szemerey) <info@dreamfaster.ai>. All rights reserved. See LICENSE in root folder.


from __future__ import annotations

from enum import Enum
from typing import Optional, Tuple, Union

import pandas as pd


def load_dataset(
    dataset_name: str,
    base_path: str = "https://raw.githubusercontent.com/dream-faster/datasets/main/datasets",
) -> pd.DataFrame:
    return pd.read_csv(f"{base_path}/{dataset_name}.csv", parse_dates=True, index_col=0)


class DeduplicationStrategy(Enum):
    first = "first"
    last = "last"

    @staticmethod
    def from_str(value: Union[str, DeduplicationStrategy]) -> DeduplicationStrategy:
        if isinstance(value, DeduplicationStrategy):
            return value
        for strategy in DeduplicationStrategy:
            if strategy.value == value:
                return strategy
        else:
            raise ValueError(f"Unknown DeduplicationStrategy: {value}")


def __process_dataset(
    df: pd.DataFrame,
    target_col: str,
    resample: Optional[str] = None,
    deduplication_strategy: Optional[Union[DeduplicationStrategy, str]] = None,
    shorten: Optional[int] = None,
) -> Tuple[pd.DataFrame, pd.Series]:
    if deduplication_strategy is not None:
        df = df[
            ~df.index.duplicated(
                keep=DeduplicationStrategy.from_str(deduplication_strategy).value
            )
        ]
    if resample is not None:
        df = df.resample(resample).last()
    if shorten is not None:
        df = df[: shorten + 1]
    y = df[target_col].shift(-1)[:-1]
    X = df[:-1]

    return X, y


def get_preprocessed_dataset(
    dataset_name: str,
    target_col: str,
    base_path: str = "https://raw.githubusercontent.com/dream-faster/datasets/main/datasets",
    resample: Optional[str] = None,
    deduplication_strategy: Optional[Union[DeduplicationStrategy, str]] = None,
    shorten: Optional[int] = None,
) -> Tuple[pd.DataFrame, pd.Series]:
    return __process_dataset(
        load_dataset(dataset_name, base_path),
        target_col=target_col,
        resample=resample,
        deduplication_strategy=deduplication_strategy,
        shorten=shorten,
    )
