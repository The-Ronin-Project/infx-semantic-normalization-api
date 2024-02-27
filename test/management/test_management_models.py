import pytest
from infx_semantic_normalization_api.management import management_models


def test_load_concept_map():
    with pytest.raises(NotImplementedError):
        management_models.load_concept_map()
