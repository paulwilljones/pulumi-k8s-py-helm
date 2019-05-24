from pulumi_kubernetes.helm.v2 import Chart, ChartOpts

jenkins = Chart(
    "pulumi-jenkins",
    ChartOpts(
        "stable/jenkins"
    )
)