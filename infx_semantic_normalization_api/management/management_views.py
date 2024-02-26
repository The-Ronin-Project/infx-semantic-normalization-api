from flask import Blueprint
from infx_semantic_normalization_api.management import (
    management_models as management_models,
)

# TODO: Naming is hard. This is intended to hold the endpoints for all things administrative and management related.
#   I'm thinking this would hold endpoints for refreshing the data in the database (e.g. concept map release).
#   "Management" might be a bit too generic though. I could alternatively create separate modules for conceptMaps and
#   registries
management_blueprint = Blueprint("management", __name__)


# TODO: Creat routes for management endpoints. The below are placeholders
@management_blueprint.route("/load_concept_map")
def refresh_concept_map():
    management_models.load_concept_map()
    return


@management_blueprint.route("/load_data_normalization_registry")
def refresh_data_normalization_registry():
    management_models.load_data_normalization_registry()
    return


@management_blueprint.route("/healthcheck")
def load_concept_map():
    management_models.health_check()
    return
