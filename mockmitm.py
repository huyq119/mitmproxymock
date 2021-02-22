from mitmproxy import ctx
from mitmproxy import http


class Stock:
    def __init__(self):
        self.num = 0

    def request(self, flow: http.HTTPFlow) -> None:
        if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
            with open("../mitmproxymock/mocktmp.json", 'r', encoding="utf-8") as f:
                flow.response = http.HTTPResponse.make(
                    200,  # (optional) status code
                    f.read(),  # (optional) content
                    {"Content-Type": "application/json"}  # (optional) headers
                )


addons = [
    Stock()
]
