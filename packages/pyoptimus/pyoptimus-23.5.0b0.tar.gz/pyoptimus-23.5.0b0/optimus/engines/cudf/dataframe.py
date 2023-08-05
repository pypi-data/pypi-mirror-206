from optimus.engines.base.cudf.dataframe import CUDFBaseDataFrame
from optimus.engines.base.dataframe.dataframe import DataFrameBaseDataFrame
from optimus.engines.cudf.io.save import Save
from optimus.engines.pandas.dataframe import PandasDataFrame


class CUDFDataFrame(CUDFBaseDataFrame, DataFrameBaseDataFrame):

    def _base_to_dfd(self, pdf, n_partitions):
        pass

    def to_optimus_pandas(self):
        return PandasDataFrame(self.root.data.to_pandas(), op=self.op)

    @property
    def rows(self):
        from optimus.engines.cudf.rows import Rows
        return Rows(self)

    @property
    def cols(self):
        from optimus.engines.cudf.columns import Cols
        return Cols(self)

    @property
    def save(self):
        return Save(self)

    @property
    def mask(self):
        from optimus.engines.cudf.mask import CUDFMask
        return CUDFMask(self)

    @property
    def functions(self):
        from optimus.engines.cudf.functions import CUDFFunctions
        return CUDFFunctions(self)

    @property
    def constants(self):
        from optimus.engines.cudf.constants import Constants
        return Constants()

    def _iloc(self, lower_bound, upper_bound, copy=True):
        dfd = self.data[lower_bound: upper_bound]
        if copy:
            dfd = dfd.reset_index(drop=True)
        return self.root.new(dfd, meta=self.root.meta)

    def to_pandas(self):
        return self.data.to_pandas().reset_index(drop=True)

    def to_dict(self, cols="*", n=10, orient="list"):

        if n == "all":
            series = self.cols.select(cols).to_pandas()
        else:
            series = self.cols.select(cols).iloc(0, n).to_pandas()

        return series.to_dict(orient)

    def repartition(self, n=None, *args, **kwargs):
        return self.root
