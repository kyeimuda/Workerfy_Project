"""
Docstring for WorkerfyAPI.API_format

This module specifies the formart for serving API endpoints in Workerfy.
"""

def api_response(success=True, message="", data=None, errors=None, meta=None):
    return {
        "success": success,
        "message": message,
        "data": data,
        "errors": errors,
        "meta": meta
    }
