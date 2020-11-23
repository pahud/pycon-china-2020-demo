from constructs import Construct, Node

# import typing
# from imports import k8s

import cdk8s_plus_17 as kplus
import cdk8s

class WebService(Construct):
    def __init__(self, scope: Construct, ns: str, *,
                image: str,
                replicas: int = 1,
                port: int = 80,
                container_port: int = 8080):
        super().__init__(scope, ns)

        label = {'app': Node.of(self).unique_id}

        deploy = kplus.Deployment(self, 'deployment',
            replicas=replicas)

        deploy.add_container(image=image, port=container_port)
        deploy.expose(port, service_type=kplus.ServiceType.LOAD_BALANCER)

        # k8s.KubeService(self, 'service',
        #                 spec=k8s.ServiceSpec(
        #                   type='LoadBalancer',
        #                   ports=[k8s.ServicePort(port=port, target_port=k8s.IntOrString.from_number(container_port))],
        #                   selector=label))

        # k8s.KubeDeployment(self, 'deployment',
        #                    spec=k8s.DeploymentSpec(
        #                       replicas=replicas,
        #                       selector=k8s.LabelSelector(match_labels=label),
        #                       template=k8s.PodTemplateSpec(
        #                       metadata=k8s.ObjectMeta(labels=label),
        #                       spec=k8s.PodSpec(
        #                         containers=[
        #                             k8s.Container(
        #                                 name='app',
        #                                 image=image,
        #                                 ports=[k8s.ContainerPort(container_port=container_port)])]))))
