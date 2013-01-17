# Download as a Service

Download as a Service (DaaS) is a service **prototype** built on Amazon EC2. It help you to download Internet resources.

## Dependency

DaaS is written in Python using [boto](https://github.com/boto/boto) as a interface to communicate to EC2.

Install via [pip](http://www.pip-installer.org/)

```
$ pip install boto
```

We use Bottle which is a lightweight web framework

```
$ pip install bottle
```

## Getting Started

1. [Create boto config](http://docs.pythonboto.org/en/latest/boto_config_tut.html)
2. Run worker.py on EC2
3. Run web.py
4. (Optional) You can setting [CloudWatch](http://aws.amazon.com/cloudwatch/) and [Auto Scaling](http://aws.amazon.com/autoscaling/) on EC2

## License

DaaS is released under the [MIT License](http://www.opensource.org/licenses/MIT).

