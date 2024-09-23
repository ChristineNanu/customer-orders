from django.utils.deprecation import MiddlewareMixin


class SecurityHeadersMiddleware(MiddlewareMixin):
    """Enfoce security headers to protect the API.

    I'm focussing on the following:
    - enable the XSS filter.
    - prevent browsers from MIME-sniffing responses besides the declared content type.
    - force clients to only connect via HTTPS for the specified duration.
    - control the referrer info sent when navigating from this API to other URLs.
    """

    def process_response(self, request, response):
        response["X-XSS-Protection"] = "1; mode=block"
        response["X-Content-Type-Options"] = "nosniff"
        response["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response["Referrer-Policy"] = "no-referrer-when-downgrade"
        return response
