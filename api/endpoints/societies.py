from flask import g, jsonify, request, current_app, url_for
from flask_restplus import Resource

from ..models import Society


class SocietyResource(Resource):
    """To contain CRUD endpoints for Society."""

    def post(self):
        """Create a society."""
        payload = request.get_json()
        if not payload:
            return {
                "status": "fail",
                "message": "name, color_scheme and logo url "
                "required"}, 400
        else:
            name = payload["name"]
            color_scheme = payload["colorScheme"]
            logo = payload["logo"] or None
            photo = payload["photo"] or None
            if not name or not color_scheme or not logo:
                return {
                    "status": "fail",
                    "message": "Name, color scheme and logo are required to create"
                                " a society."
                    }, 400
            society = Society(
                name=name, color_scheme=color_scheme, logo=logo, photo=photo
            )
            society.save()
            response = jsonify({
                "status": "success",
                "data": society.serialize(),
                "message": "Society created succesfully."
            })
            response.status_code = 201
            return response

    def get(self, society_id=None):
        if society_id:
            society = Society.query.get(society_id)
            if society:
                response = jsonify({
                    "data": society.serialize(),
                    "status": "success",
                    "message": "Society {} fetched successfully.".format(society.name)
                })
                response.status_code = 200
                # return response
            else:
                response = jsonify({
                    "data": None,
                    "status": "fail",
                    "message": "Specified society does not exist."
                })
                response.status_code = 404
            return response
        else:
            _page = request.args.get('page')
            _limit = request.args.get('limit')
            page = int(_page or current_app.config['DEFAULT_PAGE'])
            limit = int(_limit or current_app.config['PAGE_LIMIT'])
            search_term = request.args.get('q')
            societies = Society.query
            
            societies = societies.paginate(
                page=page,
                per_page=limit,
                error_out=False
            )
            if societies.items:
                previous_url = None
                next_url = None
                if societies.has_next:
                    next_url = url_for(request.endpoint, limit=limit,
                                    page=page+1, _external=True)
                if societies.has_prev:
                    previous_url = url_for(request.endpoint, limit=limit,
                                        page=page-1, _external=True)

                societies_list = []
                for _society in societies.items:
                    society = _society.serialize()
                    societies_list.append(society)

                response = jsonify({
                    "status": "success",
                    "data": {"societies": societies_list,
                            "count": len(societies.items),
                            "nextUrl": next_url,
                            "previousUrl": previous_url,
                            "currentPage": societies.page},
                    "message": "Society fetched successfully."
                })
                response.status_code = 200
                return response
            else:
                response = jsonify({
                    "status": "success",
                    "data": {"societies": [],
                            "count": 0},
                    "message": "There are no societies."
                })
                response.status_code = 404
                return response
    
    def put(self, society_id):
        payload = request.get_json()

        if payload:
            if not society_id:
                # if society_id is not passed
                return {"status": "fail",
                        "message": "Society id must be provided."}, 400

            society = Society.query.get(society_id)
            if society:
                name = payload["name"]
                color_scheme = payload["colorScheme"]
                logo = payload["logo"] or None
                photo = payload["photo"]or None
                if name:
                    society.name = name
                if color_scheme:
                    society.color = color_scheme
                if photo:
                    society.photo = logo
                if logo:
                    society.logo = photo
                society.save()
                response = jsonify({
                    "data": {"path": society.serialize()},
                    "status": "success"
                })
            else:
                response = jsonify({"status": "fail",
                                    "message": "Society does not exist."})
                response.status_code = 404
            return response

    def delete(self, society_id):
        if not society_id:
            return {"status": "fail",
                        "message": "Society id must be provided."}, 400
        society = Society.query.get(society_id)
        if not society:
            response = jsonify({"status": "fail",
                                    "message": "Society does not exist."})
            response.status_code = 404
            return response
        else:
            society.delete()
            response = jsonify({"status": "success",
                        "message": "Society deleted successfully."})
            response.status_code = 200
            return response
