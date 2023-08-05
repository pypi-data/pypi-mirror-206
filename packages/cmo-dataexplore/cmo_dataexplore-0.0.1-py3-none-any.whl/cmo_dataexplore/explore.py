import warnings
import pandas as pd
from sklearn.feature_selection import mutual_info_classif
from collections import Counter
import ppscore as pps
import math
import itertools
import matplotlib.pyplot as plt
import numpy as np
from pandas.api.types import is_numeric_dtype
from typing import List

import cmo_dataviz as ddv


class Explore:
    def __init__(
        self, data: pd.DataFrame, dependent_var: str = None, verbose: bool = True,
    ):
        assert isinstance(data, pd.DataFrame), "Please make sure you input a DataFrame"
        assert len(data) > 0, "You've inputted an empty dataframe"

        self.data = data
        self.dependent_var = dependent_var
        self.verbose = verbose

        if dependent_var is not None:
            if dependent_var not in data.columns:
                raise ValueError(
                    "Your dependent variable cannot be found in the dataframe you provided"
                )
            self._prep_dependent()

        self._remove_completely_empty_columns()

    def _prep_dependent(self):
        """
        remove records where the dependent variable is empty
        make sure the dependent variable is not numeric
        """
        row_idx = self.data.index[self.data[self.dependent_var].isna()].tolist()
        rm_perc = round(len(row_idx) / len(self.data) * 100, 2)

        target_is_num = is_numeric_dtype(self.data[self.dependent_var])
        target_has_empty = len(row_idx) > 0

        if target_has_empty:
            self.data = self.data.drop(row_idx, axis=0, inplace=False)
            warnings.warn(
                f"""for the target variable {self.dependent_var} a total 
                    of {len(row_idx)} records ({rm_perc}%) are removed due to missing values"""
            )

        original_values = self.data[self.dependent_var].unique().tolist()
        new_values = self.data[self.dependent_var].astype("str").unique().tolist()
        dict_with_replace_values = dict(zip(original_values, new_values))

        # if variable is categorical, add new values to categories
        if hasattr(self.data[self.dependent_var], "cat"):
            self.data[self.dependent_var].cat.add_categories(new_values, inplace=True)

        self.data[self.dependent_var] = self.data[self.dependent_var].replace(
            dict_with_replace_values
        )
        if target_is_num:
            warnings.warn(f"the target variable {self.dependent_var} has been converted to string")

    def _remove_completely_empty_columns(self):
        empty_cols = [col for col in self.data.columns if self.data[col].isnull().all()]
        if (self.dependent_var in empty_cols) & (len(empty_cols) > 0):
            raise ValueError("Your dependent variable is completely empty")
        if len(empty_cols) > 0:
            self.data.drop(empty_cols, axis=1, inplace=True)
            warnings.warn(
                f"""A total of {len(empty_cols)} completely empty columns(s) 
                    ({empty_cols}) will be removed from the data"""
            )

    def _prep_for_MI_calculation(self):
        X, y = (
            self.data.drop([self.dependent_var], axis=1),
            self.data[[self.dependent_var]],
        )

        # transform target to numeric categories
        if not set(list(y[self.dependent_var].unique())).issubset(
            set(list(range(0, 10)))
        ):
            target, _ = y[self.dependent_var].factorize()
            y = pd.DataFrame(target, columns=[self.dependent_var])
        cat_cols = X.select_dtypes(include=["object"]).columns.tolist()

        for column in X.columns:
            if X[column].isnull().any():
                if column in cat_cols:
                    X[column] = X[column].fillna(X[column].mode()[0])
                    print(
                        f"There are missing values in {column}, these are filled by the mode, but only for the calculation of the MI score"
                    )
                else:
                    X[column] = X[column].fillna(X[column].median())
                    print(
                        f"There are missing values in {column}, these are filled by the median, but only for the calculation of the MI score"
                    )

        for colname in cat_cols:
            X[colname], _ = X[colname].factorize()

        discrete_cols = X.dtypes == int

        return X, y, discrete_cols

    def _show_MI_scores(self, data: pd.DataFrame, ax: plt.Axes = None):
        ddv.create_horizontal_barplot(
            data=data,
            x_var="MI-score",
            y_var="feature",
            x_label="",
            title="Mutual Information Scores",
            ax=ax,
        )

    def calculate_MI_scores(
        self, plot: bool = True, ax: plt.Axes = None,
    ) -> pd.DataFrame:
        independent, dependent, discrete = self._prep_for_MI_calculation()
        mi_scores = mutual_info_classif(
            independent,
            dependent.values.ravel(),
            discrete_features=discrete,
            random_state=1502,
            n_neighbors=3,
        )
        mi_df = pd.Series(mi_scores, name="MI Scores", index=independent.columns)
        mi_df = mi_df.sort_values(ascending=False)
        mi_df = mi_df.reset_index()
        mi_df.columns = ["feature", "MI-score"]
        if plot:
            self._show_MI_scores(data=mi_df, ax=ax)
        return mi_df

    def _mode(self, var: pd.Series) -> float:
        most_freq = Counter(var).most_common(1)[0]
        mode_value = most_freq[0]
        mode_frequency = most_freq[1]
        return [mode_value, mode_frequency]

    def frequency_ratio(self, var: pd.Series) -> float:
        if var.isnull().all():
            return np.Inf
        else:
            frequencies = var.value_counts().reset_index()
            frequencies.columns = ["value", "frequency"]
            frequencies.sort_values(by="frequency", ascending=False, inplace=True)
            first_most_frequent = frequencies.iloc[0, 1]
            if len(frequencies) == 1:
                return np.Inf
            else:
                second_most_frequent = frequencies.iloc[1, 1]
                return first_most_frequent / second_most_frequent

    def data_stats(self, transpose: bool = False) -> pd.DataFrame:
        data_stats = self.data.describe(include="all")
        data_stats.loc["unique"] = self.data.nunique(dropna=True)

        top_freq_list = self.data.apply(self._mode, axis=0)
        data_stats.loc["top"] = top_freq_list.iloc[0]
        data_stats.loc["freq"] = top_freq_list.iloc[1]

        data_stats.loc["nr_records"] = len(self.data.index)
        data_stats.loc["missing"] = self.data.isnull().sum()
        data_stats.loc["percentage_missing"] = (
            self.data.isnull().sum() / len(self.data.index) * 100
        )
        data_stats.loc["all_missing"] = self.data.isnull().all()
        data_stats.loc["percentage_unique"] = (
            self.data.nunique(dropna=True) / self.data.count() * 100
        )  # don't take missings into account
        data_stats.loc["frequency_ratio"] = self.data.apply(
            self.frequency_ratio, axis=0
        )

        if transpose:
            return data_stats.transpose()
        else:
            return data_stats

    def column_stats(self, col: str) -> pd.DataFrame:
        var = self.data[col]
        data_stats = var.describe()
        data_stats.loc["unique"] = var.nunique(dropna=True)
        top_freq_list = self._mode(var)
        data_stats.loc["top"] = top_freq_list[0]
        data_stats.loc["freq"] = top_freq_list[1]
        data_stats.loc["nr_records"] = len(var.index)
        data_stats.loc["missing"] = var.isnull().sum()
        data_stats.loc["percentage_missing"] = var.isnull().sum() / len(var) * 100
        data_stats.loc["all_missing"] = var.isnull().all()
        data_stats.loc["percentage_unique"] = (
            var.nunique(dropna=True) / var.count() * 100
        )  # don't take missings into account
        data_stats.loc["frequency_ratio"] = self.frequency_ratio(var)
        return pd.DataFrame(data_stats)

    def calculate_correlation(
        self, missings_thresh: float = 0.8, plot: bool = True, ax: plt.Axes = None,
    ) -> pd.DataFrame:
        df_num = self.data.select_dtypes(include=np.number)
        df_num = df_num[df_num.columns[df_num.isnull().mean() < missings_thresh]]
        corr_matrix = df_num.corr()
        if plot:
            ddv.create_heatmap(
                data=corr_matrix,
                complete=False,
                figtitle="Correlation of numeric variables",
                ax=ax,
            )
        return corr_matrix

    def retrieve_columns_highly_correlated(
        self, corr_thresh: float = 0.8
    ) -> pd.DataFrame:
        corr_matrix = self.calculate_correlation(missings_thresh=0.8, plot=False)
        high_corr = (
            corr_matrix[(corr_matrix < -corr_thresh) | (corr_matrix > corr_thresh)]
            .dropna(thresh=2, axis=0)
            .dropna(thresh=2, axis=1)
        )
        # create a series with correlations ordered from high to low (absolute values)
        if len(high_corr) > 0:
            # only keep the lower half of the matrix and stack to a pandas series
            high_corr_series = high_corr.where(
                np.triu(np.ones(high_corr.shape), k=1).astype(bool)
            ).stack()
            # sort the outcome on the absolute correlation value
            high_corr_series = high_corr_series[
                high_corr_series.abs().sort_values(ascending=False).index
            ]
            # turn into a dataframe
            high_corr_series = pd.DataFrame(high_corr_series).reset_index()
            high_corr_series.columns = ["feature_1", "feature_2", "correlation"]
        else:
            # there is no high correlation detected
            high_corr_series = pd.DataFrame(
                columns=["feature_1", "feature_2", "correlation"]
            )
        return high_corr_series

    def calculate_PPS(self, plot: bool = True, ax: plt.Axes = None) -> pd.DataFrame:
        with warnings.catch_warnings(record=True):
            pps_df = pps.matrix(self.data)

        if plot:
            plot_df = pps_df[["x", "y", "ppscore"]].pivot(
                columns="x", index="y", values="ppscore"
            )
            ddv.create_heatmap(
                data=plot_df,
                complete=True,
                figtitle="",
                ax=ax,
            )
            plt.show()

        return pps_df

    def calculate_PPS_target(
        self, plot: bool = True, ax: plt.Axes = None,
    ) -> pd.DataFrame:

        with warnings.catch_warnings(record=True):
            pps_df = pps.predictors(
                self.data, y=self.dependent_var, output="df", sorted=True
            )

        if plot:
            ddv.create_horizontal_barplot(
                data=pps_df,
                x_var="ppscore",
                y_var="x",
                x_label="",
                title="Predictive Power Scores",
                ax=ax,
            )
            plt.show()

        return pps_df

    def categories_counter(self) -> pd.DataFrame:
        df = self._select_cat_data()
        cat_cnt = pd.DataFrame(df.nunique().sort_values(ascending=False)).reset_index()
        cat_cnt.columns = ["column", "nr categories"]

        return cat_cnt

    def _select_cat_data(self) -> pd.DataFrame:
        return self.data.select_dtypes(exclude=["number"])

    def _select_num_data(self) -> pd.DataFrame:
        return self.data.select_dtypes(include=["number"])

    def retrieve_columns_with_missings(self) -> List[str]:
        return list(self.data.columns[self.data.isnull().any()])

    def show_col_type(self):
        cat_cols = list(self._select_cat_data().columns)
        num_cols = list(self._select_num_data().columns)
        return cat_cols, num_cols

    def show_hists(
        self,
        color_by: str = None,
        bins: int = 10,
        max_categories: int = 50,
        nr_plot_cols: int = 3,
        plotsize: tuple = (15, 20),
    ) -> None:
        # remove all categorical columns with too many unique values
        cat_cnt = self.categories_counter()
        cat_cnt = cat_cnt[cat_cnt["nr categories"] > max_categories]["column"].tolist()
        all_cols = list(self.data.columns)
        if len(cat_cnt) > 0:
            all_cols = [x for x in all_cols if x not in cat_cnt]
            warnings.warn(
                f"The column(s) {cat_cnt} contain more than {max_categories} unique values and won't be plotted"
            )
        nr_plots = len(all_cols)
        nr_rows_plot = math.ceil(nr_plots / nr_plot_cols)
        fig, ax = plt.subplots(
            nrows=nr_rows_plot,
            ncols=nr_plot_cols,
            figsize=plotsize,
            squeeze=False,
            sharex=False,
            sharey=False,
        )
        col_nr = 0
        for i in range(nr_rows_plot):
            for j in range(nr_plot_cols):
                if col_nr < nr_plots:
                    ddv.create_histogram(
                        data=self.data,
                        var=all_cols[col_nr],
                        color_by=color_by,
                        bins=bins,
                        max_categories=max_categories,
                        ax=ax[i, j],
                    )
                    col_nr += 1
        plt.tight_layout()
        plt.show()

    def show_relations(
        self, bins: int = 10, max_categories: int = 50, nr_plot_cols: int = 2,
    ) -> None:
        # remove all categorical columns with too many unique values
        cat_cnt = self.categories_counter()
        cat_cnt = cat_cnt[cat_cnt["nr categories"] > max_categories]["column"].tolist()
        all_cols = list(self.data.columns)
        if len(cat_cnt) > 0:
            all_cols = [x for x in all_cols if x not in cat_cnt]
            warnings.warn(
                f"The column(s) {cat_cnt} contain more than {max_categories} unique values and won't be plotted"
            )
        all_pairs = list(set(itertools.combinations(all_cols, 2)))
        all_num_pairs = list(
            set(itertools.combinations(self._select_num_data().columns, 2))
        )
        nr_plots = ((len(all_pairs) - len(all_num_pairs)) * 2) + len(all_num_pairs)
        nr_rows_plot = math.ceil(nr_plots / nr_plot_cols)

        fig, ax = plt.subplots(
            nrows=nr_rows_plot,
            ncols=nr_plot_cols,
            figsize=(15, nr_rows_plot * 5),
            squeeze=False,
            sharex=False,
            sharey=False,
        )

        col_nr = 0
        first_time = True
        for i in range(nr_rows_plot):
            for j in range(nr_plot_cols):
                if col_nr < len(all_pairs):
                    col1 = all_pairs[col_nr][0]
                    col2 = all_pairs[col_nr][1]
                    if (is_numeric_dtype(self.data[col1])) & (
                        is_numeric_dtype(self.data[col2])
                    ):
                        ddv.create_scatterplot(
                            data=self.data,
                            x_var=col1,
                            y_var=col2,
                            title=f"{col1} vs {col2}",
                            ax=ax[i, j],
                        )
                        col_nr += 1
                    elif is_numeric_dtype(self.data[col1]):
                        if first_time:
                            ddv.create_boxplot(
                                data=self.data,
                                x_var=col1,
                                y_var=col2,
                                color_by=None,
                                ax=ax[i, j],
                                title=f"{col1} vs {col2}",
                            )
                            col_nr += 0
                            first_time = False
                        else:
                            plotdata = (
                                self.data[[col1, col2]]
                                .groupby([col2])
                                .mean()
                                .reset_index()
                            )
                            ddv.create_histogram(
                                data=plotdata,
                                var=col2,
                                color_by=None,
                                bins=bins,
                                max_categories=max_categories,
                                ax=ax[i, j],
                                title=f"mean of {col1} per {col2}",
                            )
                            first_time = True
                            col_nr += 1
                    elif is_numeric_dtype(self.data[col2]):
                        if first_time:
                            ddv.create_boxplot(
                                data=self.data,
                                x_var=col2,
                                y_var=col1,
                                color_by=None,
                                ax=ax[i, j],
                                title=f"{col2} vs {col1}",
                            )
                            col_nr += 0
                            first_time = False
                        else:
                            plotdata = (
                                self.data[[col1, col2]]
                                .groupby([col1])
                                .mean()
                                .reset_index()
                            )
                            ddv.create_histogram(
                                data=plotdata,
                                var=col1,
                                color_by=None,
                                bins=bins,
                                max_categories=max_categories,
                                ax=ax[i, j],
                                title=f"mean of {col2} per {col1}",
                            )
                            first_time = True
                            col_nr += 1
                    elif first_time:
                        ddv.create_histogram(
                            data=self.data,
                            var=col1,
                            color_by=col2,
                            bins=bins,
                            max_categories=max_categories,
                            ax=ax[i, j],
                            title=f"{col1} vs {col2}",
                        )
                        col_nr += 0
                        first_time = False
                    else:
                        ddv.create_histogram(
                            data=self.data,
                            var=col2,
                            color_by=col1,
                            bins=bins,
                            max_categories=max_categories,
                            ax=ax[i, j],
                            title=f"{col2} vs {col1}",
                        )
                        col_nr += 1
                        first_time = True

    def calculate_NZV(
        self,
        frequency_ratio_thresh: float = 95 / 5,
        percentage_unique_thresh: float = 10,
        verbose: bool = True,
    ):
        # calculate statistics and determine near zero variance
        nzv = self.data_stats(transpose=True)
        nzv["zero_variance"] = (nzv["unique"] == 1) | (nzv["all_missing"])
        nzv["near_zero_variance"] = (
            (
                (nzv["frequency_ratio"] > frequency_ratio_thresh)
                & (nzv["percentage_unique"] <= percentage_unique_thresh)
            )
            | (nzv["unique"] == 1)
            | (nzv["all_missing"])
        )
        # filter columns with near zero variance
        nzv_columns = nzv[
            (nzv["zero_variance"]) | (nzv["near_zero_variance"])
        ].index.to_list()
        # make sure the dependent variable is not in the list of columns
        if self.dependent_var in nzv_columns:
            if verbose:
                print("WARNING: the dependent variable has (near) zero variance!")
            nzv_columns.remove(self.dependent_var)
        return nzv, nzv_columns

