import pytest
from infx_semantic_normalization_api.mapping import mapping_models


def test_map_it():
    with pytest.raises(NotImplementedError):
        mapping_models.do_mapping()
