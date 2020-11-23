#!/usr/bin/env python
from constructs import Construct
from cdk8s import App, Chart

from webservice import WebService


class MyChart(Chart):
    def __init__(self, scope: Construct, name: str):
        super().__init__(scope, name)

        WebService(self, 'hello', image='paulbouwer/hello-kubernetes:1.7', replicas=2)
        WebService(self, 'ghost', image='ghost', container_port=2368)


app = App()
MyChart(app, "hello")

app.synth()
