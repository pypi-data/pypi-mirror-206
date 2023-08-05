import cgi
import http.server
import mimetypes
import os
import re
import socketserver
import jinja2


class MVCactus(http.server.BaseHTTPRequestHandler):
    """
    MVCactus is a simple web micro-framework that allows users to quickly develop and deploy web
    applications. It uses the Jinja2 templating engine for rendering templates and provides a set of convenient
    methods for handling HTTP requests and responses.

    MVCactus includes a routing system that allows users to map URLs to Python functions, and it supports both
    GET and POST requests. It also provides a method for serving static files, and includes a basic file upload feature.

    To use MVCactus, create a new class that inherits from MVCactus, define your routes using the route decorator,
    and implement the corresponding Python functions. Then, create an instance of MVCactusRun and call its run method,
    passing in your app class as an argument.

    For more information on how to use MVCactus, please refer to the documentation and examples on GitHub.
    """
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
    routes = []

    @classmethod
    @classmethod
    def route(cls, pattern):
        '''
        A decorator for registering a URL pattern and callback function to handle requests for that pattern.
        '''

        def wrapper(callback):
            # Add the '^' at the beginning and '$' at the end of the pattern to ensure a full match.
            regex_pattern = f'^{pattern}$'
            cls.routes.append((regex_pattern, callback))
            return callback

        return wrapper

    def url_for_static(self, filename):
        '''
        Returns the URL for a static file.
        '''
        # print(f'/static/{filename}')
        return f'/static/{filename}'

    def handle_error(self, status, message, template_name='upload.html', context=None):
        """
        Handles errors by sending the specified status and message as a response
        and rendering the specified template with the given context.

        Args:
            status (int): The HTTP status code to send in the response.
            message (str): The message to send in the response.
            template_name (str): The name of the template to render.
            context (dict): A dictionary containing any variables to be used in the template.

        Returns:
            None
        """
        self.send_error(status, message)
        if context is None:
            context = {}
        context['status'] = status
        context['message'] = message
        self.render_template(template_name, context)

    def send_response_headers(self, content_type, content_length=None):
        """
        Sends the response headers.

        Args:
            content_type (str): The content type of the response.
            content_length (int, optional): The content length of the response. Defaults to None.

        Features:
            - Access-Control-Allow-Origin: Sends the CORS header allowing any origin to access the resource.
            - X-Content-Type-Options: Prevents browsers from interpreting files as a different MIME type.
            - X-Frame-Options: Prevents the content from being embedded within an iframe, avoiding clickjacking attacks.
            - X-XSS-Protection: Enables the Cross-site scripting (XSS) filter in the browser.
            - Referrer-Policy: Controls the information sent in the Referer header, avoiding information leaks.
            - Feature-Policy: Restricts the use of browser features such as geolocation, microphone, and camera.
        """
        self.send_response(200)
        self.send_header('Content-Type', content_type)
        if content_length is not None:
            self.send_header('Content-Length', str(content_length))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('X-Frame-Options', 'SAMEORIGIN')
        self.send_header('X-XSS-Protection', '1; mode=block')
        self.send_header('Referrer-Policy', 'no-referrer')
        self.send_header('Feature-Policy', "geolocation 'none'; microphone 'none'; camera 'none'")
        self.end_headers()

    def do_GET(self):
        if self.path.startswith('/static/'):
            path = self.path[7:]
            self.serve_static_file(path)
            return

        for pattern, callback in self.routes:
            match = re.match(pattern, self.path)
            if match:
                callback(self, match)
                return

        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        '''
        This method handles POST requests sent to the server. It first checks if the request contains multipart form
        data. If it does, it saves the uploaded file and sends a success response. If it doesn't, it reads the
        request body and searches for a callback function in self. routes with the matching path and function name. If
        it finds a match, it calls the function with the request body as a parameter. If no match is found,
        it sends a 404 error response.
        '''
        content_length = int(self.headers['Content-Length'])
        content_type = self.headers['Content-Type']

        if 'multipart/form-data' in content_type:
            fields = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={
                'REQUEST_METHOD': 'POST',
                'CONTENT_TYPE': content_type,
            })

            if 'file' in fields:
                file_item = fields['file']
                filename = os.path.join('uploads', file_item.filename)
                with open(filename, 'wb') as f:
                    f.write(file_item.file.read())
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Successfully uploaded file')

                return
        else:
            body = self.rfile.read(content_length).decode('utf-8')

            for pattern, callback in self.routes:
                if self.path == pattern and callback.__name__ == 'handle_post':
                    callback(self, body)
                    return

        self.send_response(404)
        self.end_headers()

    @classmethod
    def post(cls, path):
        """
        Class method that acts as a decorator for registering a POST request handler with a given path.

        Args:
            path (str): The path to associate the handler with.

        Returns: function: The decorator function that registers the given callback function as a POST request
        handler for the given path.
        """

        def wrapper(callback):
            """
            Wrapper function that registers the given callback function as a POST request handler for the path given
            to the outer function.

            Args:
                callback (function): The function that handles the POST request.

            Returns:
                function: The given callback function.
            """
            cls.routes.append((path, callback))
            return callback

        return wrapper

    @staticmethod
    def handle_post(handler, body):
        """
        Static method that handles POST requests by sending a plain text response with the given request body.

        Args:
            handler (MVCactus): The instance of the MVCactus server handling the request.
            body (str): The body of the POST request.

        Returns:
            None
        """
        handler.send_response(200)
        handler.send_header('Content-type', 'text/plain')
        handler.end_headers()
        handler.wfile.write(body.encode('utf-8'))

    def serve_static_file(self, path):
        try:
            current_dir = os.path.abspath("static")
            file_path = f"{current_dir}{path}"
            print(f'Serving static file: {file_path}')

            if not os.path.isfile(file_path):
                raise IOError

            mime_type, _ = mimetypes.guess_type(path)
            content_length = os.path.getsize(file_path)

            self.send_response_headers(mime_type, content_length)

            with open(file_path, 'rb') as f:
                chunk_size = 8192
                while True:
                    chunk = f.read(chunk_size)
                    if not chunk:
                        break
                    self.wfile.write(chunk)
        except IOError:
            self.send_error(404, 'File not found')

    def validate_input(self, data, fields):
        """
        Validates the input data for a request, checking that all required fields are present.

        Args:
            data (dict): The input data for the request.
            fields (list): The list of required fields.

        Returns:
            bool: True if all required fields are present, False otherwise.
        """
        missing_fields = []
        for field in fields:
            if field not in data:
                missing_fields.append(field)
        if missing_fields:
            self.send_error(400, f'Missing fields: {", ".join(missing_fields)}')
            return False
        return True

    def render_template(self, template_name, context=None):
        """
        Renders a Jinja2 template with the given context and sends the resulting HTML to the client.

        Args:
            template_name (str): The name of the template file.
            context (dict, optional): The context to render the template with. Defaults to None.

        Returns:
            None
        """
        template = self.env.get_template(template_name)
        if context is None:
            context = {}
        context['url_for_static'] = self.url_for_static
        html = template.render(context)
        self.send_response_headers('text/html', len(html.encode('utf-8')))
        self.wfile.write(html.encode('utf-8'))


class MVCactusRun:

    def __init__(self, address='localhost', port=8080):
        self.ADDRESS = address
        self.PORT = port

    def run(self, app_class):
        with socketserver.TCPServer((self.ADDRESS, self.PORT), app_class) as httpd:
            print(f"Running on {self.ADDRESS}:{self.PORT}")
            print(f"Enter here: http://{self.ADDRESS}:{self.PORT}/")
            if "static" or "templates" not in os.listdir():
                if "static" not in os.listdir():
                    os.mkdir("static")
                    print("* Static folder created")
                elif "templates" not in os.listdir():
                    os.mkdir("templates")
                    print("* Templates folder created")
            print("* Press Ctrl+C to stop")
            print("========================================")

            httpd.serve_forever()
