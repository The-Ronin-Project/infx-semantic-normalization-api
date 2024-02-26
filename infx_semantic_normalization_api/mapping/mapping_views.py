from flask import Blueprint
from infx_semantic_normalization_api.mapping import mapping_models as mapping_models

# TODO: Naming is hard. This is intended to hold the endpoints for all things mapping that interops would call.
#   Does mapping make sense, or should I align to the service name and call it normalization or similar
mapping_blueprint = Blueprint("mapping", __name__)


# TODO: Creat route(s) for mapping endpoints. The below is just a placeholder
@mapping_blueprint.route("/map")
def map_it():
    mapping_models.do_mapping()
    return
