from app.api import bp

@bp.after_request
def apply_control_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:8080"
    return response
