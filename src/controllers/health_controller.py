from flask_restful import Resource as PublicBaseController


class HealthController(PublicBaseController):
    def get(self):
        return "healthy!!!!"
