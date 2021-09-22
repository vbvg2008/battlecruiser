from typing import Any, Tuple


class Dataset:
    def __init__(self) -> None:
        pass

    def __len__(self) -> int:
        return 0

    def __getitem__(self, idx) -> Any:
        return None


class MemoryDataset(Dataset):
    def __init__(self, *args):
        self.features = args
        self.feature_length = None
        self.__check_inputs(self.features)

    def __check_inputs(self, features):
        ds_length = set()
        for feature in features:
            assert hasattr(feature, "__getitem__"), "cannot index the feature"
            if hasattr(feature, "__len__"):
                ds_length.add(len(feature))
            else:
                assert hasattr(feature, "shape"), "cannot find the shape of feature"
                ds_length.add(feature.shape[0])
        assert len(ds_length) == 1, "found inconsistent feature lengths: {}".format(ds_length)
        self.feature_length = ds_length.pop()

    def __len__(self) -> int:
        return self.feature_length

    def __getitem__(self, idx) -> Tuple:
        results = tuple(feature[idx] for feature in self.features)
        return results[0] if len(results) == 1 else results
