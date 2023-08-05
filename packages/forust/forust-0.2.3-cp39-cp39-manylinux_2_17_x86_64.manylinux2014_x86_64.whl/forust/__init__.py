from __future__ import annotations

import sys
from typing import Any, Union, cast

import numpy as np
import pandas as pd

from .forust import GradientBooster as CrateGradientBooster  # type: ignore

ArrayLike = Union[pd.Series, np.ndarray]
FrameLike = Union[pd.DataFrame, np.ndarray]


class BoosterType:
    monotone_constraints: dict[int, int]

    def fit(
        self,
        flat_data: np.ndarray,
        rows: int,
        cols: int,
        y: np.ndarray,
        sample_weight: np.ndarray,
        parallel: bool = True,
    ):
        raise NotImplementedError()

    def predict(
        self,
        flat_data: np.ndarray,
        rows: int,
        cols: int,
        parallel: bool = True,
    ) -> np.ndarray:
        raise NotImplementedError()

    def predict_contributions(
        self,
        flat_data: np.ndarray,
        rows: int,
        cols: int,
        parallel: bool = True,
    ) -> np.ndarray:
        raise NotImplementedError

    def value_partial_dependence(
        self,
        feature: int,
        value: float,
    ) -> float:
        raise NotImplementedError()

    def text_dump(self) -> list[str]:
        raise NotImplementedError()

    @classmethod
    def load_booster(cls, path: str) -> BoosterType:
        raise NotImplementedError()

    def save_booster(self, path: str):
        raise NotImplementedError()

    @classmethod
    def from_json(cls, json_str: str) -> BoosterType:
        raise NotImplementedError()

    def json_dump(self) -> str:
        raise NotImplementedError()

    def get_params(self) -> dict[str, Any]:
        raise NotImplementedError()

    def insert_metadata(self, key: str, value: str) -> None:
        raise NotImplementedError()

    def get_metadata(self, key: str) -> str:
        raise NotImplementedError()


class GradientBooster:
    def __init__(
        self,
        objective_type: str = "LogLoss",
        iterations: int = 100,
        learning_rate: float = 0.3,
        max_depth: int = 5,
        max_leaves: int = sys.maxsize,
        l2: float = 1.0,
        gamma: float = 0.0,
        min_leaf_weight: float = 1.0,
        base_score: float = 0.5,
        nbins: int = 256,
        parallel: bool = True,
        allow_missing_splits: bool = True,
        monotone_constraints: Union[dict[Any, int], None] = None,
        subsample: float = 1.0,
        seed: int = 0,
        missing: float = np.nan,
    ):
        """Gradient Booster Class, used to generate gradient boosted decision tree ensembles.

        Args:
            objective_type (str, optional): The name of objective function used to optimize.
                Valid options include "LogLoss" to use logistic loss as the objective function
                (binary classification), or "SquaredLoss" to use Squared Error as the objective
                function (continuous regression). Defaults to "LogLoss".
            iterations (int, optional): Total number of trees to train in the ensemble.
                Defaults to 100.
            learning_rate (float, optional): Step size to use at each iteration. Each
                leaf weight is multiplied by this number. The smaller the value, the more
                conservative the weights will be. Defaults to 0.3.
            max_depth (int, optional): Maximum depth of an individual tree. Valid values
            are 0 to infinity. Defaults to 5.
            max_leaves (int, optional): Maximum number of leaves allowed on a tree. Valid values
                are 0 to infinity. This is the total number of final nodes. Defaults to sys.maxsize.
            l2 (float, optional): L2 regularization term applied to the weights of the tree. Valid values
                are 0 to infinity. Defaults to 1.0.
            gamma (float, optional): The minimum amount of loss required to further split a node.
                Valid values are 0 to infinity. Defaults to 0.0.
            min_leaf_weight (float, optional): Minimum sum of the hessian values of the loss function
                required to be in a node. Defaults to 1.0.
            base_score (float, optional): The initial prediction value of the model. Defaults to 0.5.
            nbins (int, optional): Number of bins to calculate to partition the data. Setting this to
                a smaller number, will result in faster training time, while potentially sacrificing
                accuracy. If there are more bins, than unique values in a column, all unique values
                will be used. Defaults to 256.
            parallel (bool, optional): Should multiple cores be used when training and predicting
                with this model? Defaults to `True`.
            allow_missing_splits (bool, optional): Allow for splits to be made such that all missing values go
                down one branch, and all non-missing values go down the other, if this results
                in the greatest reduction of loss. If this is false, splits will only be made on non
                missing values. Defaults to `True`.
            monotone_constraints (dict[Any, int], optional): Constraints that are used to enforce a
                specific relationship between the training features and the target variable. A dictionary
                should be provided where the keys are the feature index value if the model will be fit on
                a numpy array, or a feature name if it will be fit on a pandas Dataframe. The values of
                the dictionary should be an integer value of -1, 1, or 0 to specify the relationship
                that should be estimated between the respective feature and the target variable.
                Use a value of -1 to enforce a negative relationship, 1 a positive relationship,
                and 0 will enforce no specific relationship at all. Features not included in the
                mapping will not have any constraint applied. If `None` is passed no constraints
                will be enforced on any variable.  Defaults to `None`.
            subsample (float, optional): Percent of records to randomly sample at each iteration when
                training a tree. Defaults to 1.0, meaning all data is used to training.
            seed (integer, optional): Integer value used to seed any randomness used in the
                algorithm. Defaults to 0.
            missing (float, optional): Value to consider missing, when training and predicting
                with the booster. Defaults to `np.nan`.

        Raises:
            TypeError: Raised if an invalid dtype is passed.
        """
        booster = CrateGradientBooster(
            objective_type=objective_type,
            iterations=iterations,
            learning_rate=learning_rate,
            max_depth=max_depth,
            max_leaves=max_leaves,
            l2=l2,
            gamma=gamma,
            min_leaf_weight=min_leaf_weight,
            base_score=base_score,
            nbins=nbins,
            parallel=parallel,
            allow_missing_splits=allow_missing_splits,
            monotone_constraints={},
            subsample=subsample,
            seed=seed,
            missing=missing,
        )
        monotone_constraints_ = (
            {} if monotone_constraints is None else monotone_constraints
        )
        self.booster = cast(BoosterType, booster)
        self.objective_type = objective_type
        self.iterations = iterations
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.max_leaves = max_leaves
        self.l2 = l2
        self.gamma = gamma
        self.min_leaf_weight = min_leaf_weight
        self.base_score = base_score
        self.nbins = nbins
        self.parallel = parallel
        self.allow_missing_splits = (allow_missing_splits,)
        self.monotone_constraints = monotone_constraints_
        self.subsample = subsample
        self.seed = seed
        self.missing = missing

    def fit(
        self,
        X: FrameLike,
        y: ArrayLike,
        sample_weight: Union[ArrayLike, None] = None,
    ):
        """Fit the gradient booster on a provided dataset.

        Args:
            X (FrameLike): Either a pandas DataFrame, or a 2 dimensional numpy array.
            y (ArrayLike): Either a pandas Series, or a 1 dimensional numpy array. If "LogLoss"
                was the objective type specified, then this should only contain 1 or 0 values,
                where 1 is the positive class being predicted. If "SquaredLoss" is the
                objective type, then any continuous variable can be provided.
            sample_weight (Union[ArrayLike, None], optional): Instance weights to use when
                training the model. If None is passed, a weight of 1 will be used for every record.
                Defaults to None.
        """
        if isinstance(X, pd.DataFrame):
            X_ = X.to_numpy()
            self.feature_names_in_ = X.columns.to_list()
            self.insert_metadata("feature_names_in_", str(self.feature_names_in_))
        else:
            # Assume it's a numpy array.
            X_ = X
        if not np.issubdtype(X_.dtype, "float64"):
            X_ = X_.astype(dtype="float64", copy=False)

        y_ = y.to_numpy() if isinstance(y, pd.Series) else y

        if not np.issubdtype(y_.dtype, "float64"):
            y_ = y_.astype(dtype="float64", copy=False)

        if sample_weight is None:
            sample_weight = np.ones(y_.shape, dtype="float64")
        sample_weight_ = (
            sample_weight.to_numpy()
            if isinstance(sample_weight, pd.Series)
            else sample_weight
        )

        if not np.issubdtype(sample_weight_.dtype, "float64"):
            sample_weight_ = sample_weight_.astype("float64", copy=False)

        # Convert the monotone constraints into the form needed
        # by the rust code.
        monotone_constraints_ = self._standardize_monotonicity_map(X)
        self.booster.monotone_constraints = monotone_constraints_

        flat_data = X_.ravel(order="F")
        rows, cols = X_.shape
        self.booster.fit(
            flat_data=flat_data,
            rows=rows,
            cols=cols,
            y=y_,
            sample_weight=sample_weight_,
        )

    def predict(self, X: FrameLike, parallel: Union[bool, None] = None) -> np.ndarray:
        """Predict with the fitted booster on new data.

        Args:
            X (FrameLike): Either a pandas DataFrame, or a 2 dimensional numpy array.
            parallel (Union[bool, None], optional): Optionally specify if the predict
                function should run in parallel on multiple threads. If `None` is
                passed, the `parallel` attribute of the booster will be used.
                Defaults to `None`.

        Returns:
            np.ndarray: Returns a numpy array of the predictions.
        """
        X_ = X.to_numpy() if isinstance(X, pd.DataFrame) else X
        if not np.issubdtype(X_.dtype, "float64"):
            X_ = X_.astype(dtype="float64", copy=False)

        parallel_ = self.parallel if parallel is None else parallel
        flat_data = X_.ravel(order="F")
        rows, cols = X_.shape
        return self.booster.predict(
            flat_data=flat_data,
            rows=rows,
            cols=cols,
            parallel=parallel_,
        )

    def predict_contributions(
        self, X: FrameLike, parallel: Union[bool, None] = None
    ) -> np.ndarray:
        """Predict with the fitted booster on new data, returning the feature
        contribution matrix. The last column is the bias term.

        Args:
            X (FrameLike): Either a pandas DataFrame, or a 2 dimensional numpy array.
            parallel (Union[bool, None], optional): Optionally specify if the predict
                function should run in parallel on multiple threads. If `None` is
                passed, the `parallel` attribute of the booster will be used.
                Defaults to `None`.

        Returns:
            np.ndarray: Returns a numpy array of the predictions.
        """
        X_ = X.to_numpy() if isinstance(X, pd.DataFrame) else X
        if not np.issubdtype(X_.dtype, "float64"):
            X_ = X_.astype(dtype="float64", copy=False)

        parallel_ = self.parallel if parallel is None else parallel
        flat_data = X_.ravel(order="F")
        rows, cols = X_.shape
        contributions = self.booster.predict_contributions(
            flat_data=flat_data,
            rows=rows,
            cols=cols,
            parallel=parallel_,
        )
        return np.reshape(contributions, (X_.shape[0], X_.shape[1] + 1))

    def partial_dependence(self, X: FrameLike, feature: Union[str, int]) -> np.ndarray:
        """Calculate the partial dependence values of a feature. For each unique
        value of the feature, this gives the estimate of the predicted value for that
        feature, with the effects of all features averaged out. This information gives
        an estimate of how a given feature impacts the model.

        Args:
            X (FrameLike): Either a pandas DataFrame, or a 2 dimensional numpy array.
                This should be the same data passed into the models fit, or predict,
                with the columns in the same order.
            feature (Union[str, int]): The feature for which to calculate the partial
                dependence values. This can be the name of a column, if the provided
                X is a pandas DataFrame, or the index of the feature.

        Raises:
            ValueError: An error will be raised if the provided X parameter is not a
                pandas DataFrame, and a string is provided for the feature.

        Returns:
            np.ndarray: A 2 dimensional numpy array, where the first column is the
                sorted unique values of the feature, and then the second column
                is the partial dependence values for each feature value.
        """
        is_dataframe = isinstance(X, pd.DataFrame)
        if isinstance(feature, str):
            if not is_dataframe:
                raise ValueError(
                    "If `feature` is a string, then the object passed as `X` must be a pandas DataFrame."
                )
            values = np.sort(X.loc[:, feature].unique())
            feature_idx = next(i for i, v in enumerate(X.columns) if v == feature)
        elif isinstance(feature, int):
            if is_dataframe:
                values = np.sort(X.iloc[:, feature].unique())
            else:
                values = np.sort(np.unique(X[:, feature]))
            feature_idx = feature
        else:
            raise ValueError(
                f"The parameter `feature` must be a string, or an int, however an object of type {type(feature)} was passed."
            )
        res = []
        for v in values:
            res.append(
                (v, self.booster.value_partial_dependence(feature=feature_idx, value=v))
            )
        return np.array(res)

    def text_dump(self) -> list[str]:
        """Return all of the trees of the model in text form.

        Returns:
            list[str]: A list of strings, where each string is a text representation
                of the tree.
        """
        return self.booster.text_dump()

    def json_dump(self) -> str:
        """Return the booster object as a string.

        Returns:
            str: The booster dumped as a json object in string form.
        """
        return self.booster.json_dump()

    @classmethod
    def load_booster(cls, path: str) -> GradientBooster:
        """Load a booster object that was saved with the `save_booster` method.

        Args:
            path (str): Path to the saved booster file.

        Returns:
            GradientBooster: An initialized booster object.
        """
        booster = CrateGradientBooster.load_booster(str(path))

        params = booster.get_params()
        c = cls(**params)
        c.booster = booster
        return c

    def save_booster(self, path: str):
        """Save a booster object, the underlying representation is a json file.

        Args:
            path (str): Path to save the booster object.
        """
        self.booster.save_booster(str(path))

    def _standardize_monotonicity_map(
        self,
        X: Union[pd.DataFrame, np.ndarray],
    ) -> dict[int, Any]:
        if isinstance(X, np.ndarray):
            return self.monotone_constraints
        else:
            feature_map = {f: i for i, f in enumerate(X.columns)}
            return {feature_map[f]: v for f, v in self.monotone_constraints.items()}

    def insert_metadata(self, key: str, value: str):
        """Insert data into the models metadata, this will be saved on the booster object.

        Args:
            key (str): Key to give the inserted value in the metadata.
            value (str): Value to assign the the key.
        """
        self.booster.insert_metadata(key=key, value=value)

    def get_metadata(self, key: str) -> str:
        """Get the value associated with a given key, on the boosters metadata.

        Args:
            key (str): Key of item in metadata.

        Returns:
            str: Value associated with the provided key in the boosters metadata.
        """
        return self.booster.get_metadata(key=key)
