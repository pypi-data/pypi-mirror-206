from typing import Tuple

import numpy as np
import pandas as pd
import pytest
from xgboost import XGBClassifier, XGBRegressor

from forust import GradientBooster


@pytest.fixture
def X_y() -> Tuple[pd.DataFrame, pd.Series]:
    df = pd.read_csv("../resources/titanic.csv")
    X = df.select_dtypes("number").drop(columns="survived").reset_index(drop=True)
    y = df["survived"]
    return X, y


def test_booster_to_xgboosts(X_y):
    X, y = X_y
    X = X.fillna(0)
    xmod = XGBClassifier(
        n_estimators=100,
        learning_rate=0.3,
        max_depth=5,
        reg_lambda=1,
        min_child_weight=1.0,
        gamma=0,
        objective="binary:logitraw",
        tree_method="hist",
    )
    xmod.fit(X, y)
    xmod_preds = xmod.predict(X, output_margin=True)

    fmod = GradientBooster(
        iterations=100,
        learning_rate=0.3,
        max_depth=5,
        l2=1,
        min_leaf_weight=1.0,
        gamma=0,
        objective_type="LogLoss",
    )
    fmod.fit(X, y=y)
    fmod_preds = fmod.predict(X)
    assert np.allclose(fmod_preds, xmod_preds, atol=0.00001)


def test_booster_to_xgboosts_with_missing(X_y):
    X, y = X_y
    X = X
    xmod = XGBClassifier(
        n_estimators=100,
        learning_rate=0.3,
        max_depth=5,
        reg_lambda=1,
        min_child_weight=1,
        gamma=1,
        objective="binary:logitraw",
        eval_metric="auc",
        tree_method="hist",
        max_bin=10000,
    )
    xmod.fit(X, y)
    xmod_preds = xmod.predict(X, output_margin=True)

    fmod = GradientBooster(
        iterations=100,
        learning_rate=0.3,
        max_depth=5,
        l2=1,
        min_leaf_weight=1,
        gamma=1,
        objective_type="LogLoss",
        nbins=500,
        parallel=True,
    )
    fmod.fit(X, y=y)
    fmod_preds = fmod.predict(X)
    assert np.allclose(fmod_preds, xmod_preds, atol=0.00001)


def test_booster_to_xgboosts_with_missing_sl(X_y):
    X, y = X_y
    X = X
    X["survived"] = y
    y = X["fare"]
    X = X.drop(columns=["fare"])
    xmod = XGBRegressor(
        n_estimators=100,
        learning_rate=0.3,
        max_depth=5,
        reg_lambda=1,
        min_child_weight=1,
        gamma=1,
        eval_metric="auc",
        tree_method="hist",
        max_bin=10000,
    )
    xmod.fit(X, y)
    xmod_preds = xmod.predict(X, output_margin=True)

    fmod = GradientBooster(
        iterations=100,
        learning_rate=0.3,
        max_depth=5,
        l2=1,
        min_leaf_weight=1,
        gamma=1,
        objective_type="SquaredLoss",
        nbins=500,
        parallel=True,
    )
    fmod.fit(X, y=y)
    fmod_preds = fmod.predict(X)
    assert np.allclose(fmod_preds, xmod_preds, atol=0.00001)


def test_booster_with_new_missing(X_y):
    X, y = X_y
    X = X
    fmod = GradientBooster(
        iterations=100,
        learning_rate=0.3,
        max_depth=5,
        l2=1,
        min_leaf_weight=1,
        gamma=1,
        objective_type="LogLoss",
        nbins=500,
        parallel=True,
    )
    fmod.fit(X, y=y)
    fmod_preds = fmod.predict(X)

    Xm = X.copy().fillna(-9999)
    fmod2 = GradientBooster(
        iterations=100,
        learning_rate=0.3,
        max_depth=5,
        l2=1,
        min_leaf_weight=1,
        gamma=1,
        objective_type="LogLoss",
        nbins=500,
        parallel=True,
        missing=-9999,
    )
    fmod2.fit(Xm, y=y)
    fmod_preds2 = fmod2.predict(Xm)
    assert np.allclose(fmod_preds, fmod_preds2, atol=0.00001)


def test_booster_with_seed(X_y):
    X, y = X_y
    X = X
    fmod1 = GradientBooster(
        iterations=100,
        learning_rate=0.3,
        max_depth=5,
        l2=1,
        min_leaf_weight=1,
        gamma=1,
        objective_type="LogLoss",
        nbins=500,
        parallel=True,
        subsample=0.5,
        seed=0,
    )
    fmod1.fit(X, y=y)
    fmod1_preds = fmod1.predict(X)

    fmod2 = GradientBooster(
        iterations=100,
        learning_rate=0.3,
        max_depth=5,
        l2=1,
        min_leaf_weight=1,
        gamma=1,
        objective_type="LogLoss",
        nbins=500,
        parallel=True,
        subsample=0.5,
        seed=0,
    )
    fmod2.fit(X, y=y)
    fmod2_preds = fmod2.predict(X)
    assert np.allclose(fmod2_preds, fmod1_preds, atol=0.0000001)

    fmod3 = GradientBooster(
        iterations=100,
        learning_rate=0.3,
        max_depth=5,
        l2=1,
        min_leaf_weight=1,
        gamma=1,
        objective_type="LogLoss",
        nbins=500,
        parallel=True,
        subsample=0.5,
        seed=1,
    )
    fmod3.fit(X, y=y)
    fmod3_preds = fmod3.predict(X)
    assert not np.allclose(fmod3_preds, fmod2_preds, atol=0.0000001)

    fmod4 = GradientBooster(
        iterations=100,
        learning_rate=0.3,
        max_depth=5,
        l2=1,
        min_leaf_weight=1,
        gamma=1,
        objective_type="LogLoss",
        nbins=500,
        parallel=True,
    )
    fmod4.fit(X, y=y)
    fmod4_preds = fmod4.predict(X)
    assert not np.allclose(fmod4_preds, fmod2_preds, atol=0.00001)


def test_booster_to_xgboosts_weighted(X_y):
    X, y = X_y
    X = X.fillna(0)
    w = X["fare"].to_numpy() + 1
    xmod = XGBClassifier(
        n_estimators=100,
        learning_rate=0.3,
        max_depth=5,
        reg_lambda=1,
        min_child_weight=1,
        gamma=0,
        objective="binary:logitraw",
        tree_method="hist",
        max_bins=1000,
    )
    xmod.fit(X, y, sample_weight=w)
    xmod_preds = xmod.predict(X, output_margin=True)

    fmod = GradientBooster(
        iterations=100,
        learning_rate=0.3,
        max_depth=5,
        l2=1,
        min_leaf_weight=1,
        gamma=0,
        objective_type="LogLoss",
    )
    fmod.fit(X, y=y, sample_weight=w)
    fmod_preds = fmod.predict(X)
    assert np.allclose(fmod_preds, xmod_preds, atol=0.0001)


def test_booster_saving(X_y, tmp_path):
    # squared loss
    f64_model_path = tmp_path / "modelf64_sl.json"
    X, y = X_y
    X = X
    fmod = GradientBooster(
        iterations=100,
        learning_rate=0.3,
        max_depth=5,
        l2=1,
        min_leaf_weight=1,
        gamma=1,
        objective_type="SquaredLoss",
        nbins=500,
        parallel=True,
    )
    fmod.fit(X, y=y)
    fmod_preds = fmod.predict(X)
    fmod.save_booster(f64_model_path)
    fmod_loaded = GradientBooster.load_booster(f64_model_path)
    assert all(fmod_preds == fmod_loaded.predict(X))

    # LogLoss
    f64_model_path = tmp_path / "modelf64_ll.json"
    X, y = X_y
    X = X
    fmod = GradientBooster(
        iterations=100,
        learning_rate=0.3,
        max_depth=5,
        l2=1,
        min_leaf_weight=1,
        gamma=1,
        objective_type="LogLoss",
        nbins=500,
        parallel=True,
    )
    fmod.fit(X, y=y)
    fmod_preds = fmod.predict(X)
    fmod.save_booster(f64_model_path)
    fmod_loaded = GradientBooster.load_booster(f64_model_path)
    assert all(fmod_preds == fmod_loaded.predict(X))


def test_booster_saving_with_montone_constraints(X_y, tmp_path):
    # squared loss
    f64_model_path = tmp_path / "modelf64_sl.json"
    X, y = X_y
    X = X
    mono_ = X.apply(lambda x: int(np.sign(x.corr(y)))).to_dict()
    fmod = GradientBooster(
        iterations=100,
        learning_rate=0.3,
        max_depth=5,
        l2=1,
        min_leaf_weight=1,
        gamma=1,
        objective_type="SquaredLoss",
        nbins=500,
        parallel=True,
        monotone_constraints=mono_,
    )
    fmod.fit(X, y=y)
    fmod_preds = fmod.predict(X)
    fmod.save_booster(f64_model_path)
    fmod_loaded = GradientBooster.load_booster(f64_model_path)
    assert all(fmod_preds == fmod_loaded.predict(X))

    # LogLoss
    f64_model_path = tmp_path / "modelf64_ll.json"
    X, y = X_y
    X = X
    fmod = GradientBooster(
        iterations=100,
        learning_rate=0.3,
        max_depth=5,
        l2=1,
        min_leaf_weight=1,
        gamma=1,
        objective_type="LogLoss",
        nbins=500,
        parallel=True,
        monotone_constraints=mono_,
    )
    fmod.fit(X, y=y)
    fmod_preds = fmod.predict(X)
    fmod.save_booster(f64_model_path)
    fmod_loaded = GradientBooster.load_booster(f64_model_path)
    assert all(fmod_preds == fmod_loaded.predict(X))


def test_monotone_constraints(X_y):
    X, y = X_y
    X = X
    mono_ = X.apply(lambda x: int(np.sign(x.corr(y)))).to_dict()
    fmod = GradientBooster(
        iterations=100,
        learning_rate=0.3,
        max_depth=5,
        l2=1,
        min_leaf_weight=1,
        gamma=1,
        objective_type="SquaredLoss",
        nbins=500,
        parallel=True,
        monotone_constraints=mono_,
    )
    fmod.fit(X, y=y)
    for f, m in mono_.items():
        p_d = fmod.partial_dependence(X, feature=f)
        p_d = p_d[~np.isnan(p_d[:, 0])]
        if m < 0:
            assert np.all(p_d[0:-1, 1] >= p_d[1:, 1])
        else:
            assert np.all(p_d[0:-1, 1] <= p_d[1:, 1])


def test_booster_to_xgboosts_with_contributions(X_y):
    X, y = X_y
    X = X
    fmod = GradientBooster(
        iterations=100,
        learning_rate=0.3,
        max_depth=5,
        l2=1,
        min_leaf_weight=1,
        gamma=1,
        objective_type="LogLoss",
        nbins=500,
        parallel=True,
        base_score=0.5,
    )
    fmod.fit(X, y=y)
    fmod_preds = fmod.predict(X)
    fmod_contribs = fmod.predict_contributions(X)
    fmod_preds[~np.isclose(fmod_contribs.sum(1), fmod_preds, rtol=5)]
    fmod_contribs.sum(1)[~np.isclose(fmod_contribs.sum(1), fmod_preds, rtol=5)]
    assert fmod_contribs.shape[1] == X.shape[1] + 1
    assert np.allclose(fmod_contribs.sum(1), fmod_preds)

    xmod = XGBClassifier(
        n_estimators=100,
        learning_rate=0.3,
        max_depth=5,
        reg_lambda=1,
        min_child_weight=1,
        gamma=1,
        objective="binary:logitraw",
        eval_metric="auc",
        tree_method="hist",
        max_bin=10000,
        base_score=0.5,
    )
    xmod.fit(X, y)
    xmod_preds = xmod.predict(X, output_margin=True)
    import xgboost as xgb

    xmod_contribs = xmod.get_booster().predict(
        xgb.DMatrix(X), approx_contribs=True, pred_contribs=True
    )
    assert np.allclose(fmod_contribs, xmod_contribs, atol=0.000001)


def test_booster_metadata(X_y, tmp_path):
    f64_model_path = tmp_path / "modelf64_sl.json"
    X, y = X_y
    X = X
    fmod = GradientBooster(
        iterations=100,
        learning_rate=0.3,
        max_depth=5,
        l2=1,
        min_leaf_weight=1,
        gamma=1,
        objective_type="SquaredLoss",
        nbins=500,
        parallel=True,
    )
    fmod.fit(X, y=y)
    fmod_preds = fmod.predict(X)
    fmod.save_booster(f64_model_path)
    fmod.insert_metadata("test-info", "some-info")
    assert fmod.get_metadata("test-info") == "some-info"
    fmod.save_booster(f64_model_path)

    loaded = GradientBooster.load_booster(f64_model_path)
    assert loaded.get_metadata("test-info") == "some-info"

    with pytest.raises(KeyError):
        loaded.get_metadata("No-key")
