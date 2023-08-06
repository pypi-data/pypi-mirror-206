`pytos2` CE: Official Python Library for the [Tufin Orchestration Suite](https://tufin.com)
==============================================
`pytos2` "Community Edition" (CE) is the official Python library
for the Tufin Orchestration Suite. It is created, maintained by
and supported by the Tufin Professional Services Solutions team (PSS). It wraps the
[Official TOS API](https://forum.tufin.com/support/kc/latest/Content/Suite/4423.htm)
and provides idiomatic Python-level types and features.

`pytos2-ce` currently supports TufinOS3 and both TOS Classic and Aurora. The
implementation of Aurora-specific GraphQL features, as well as some of the
below-stated features are still under active development.


Installation
------------
[Git](https://git-scm.com) is a prerequisite for installation. Also, development using either
[`venv`](https://docs.python.org/3/library/venv.html#creating-virtual-environments)
or [Docker](https://docs.docker.com/get-docker/)
is recommended.

`pytos2` CE is currently *not* yet available on [PyPI](https://pypi.org). To install, use
the following [`pip`](https://pypi.org/project/pip/) command:

```bash
$ pip install pytos2-ce 

# Pull latest code (requires git)


$ pip install git+https://gitlab.com/tufinps/pytos2-ce
```

Setup
-----
`pytos2` CE recommends pre-setting the following environment
variables while using this library, and they will be assumed to be
set from this point onward. They can either be set directly
in the environment using a method of your choice, or you can use [python-dotenv](https://saurabh-kumar.com/python-dotenv/). They are as follows:

- `TOS_HOSTNAME`: The hostname where your TOS installation lives.
  It is assumed to *not* be a split SecureTrack/SecureChange
  environment.
- `SCW_API_USERNAME`: The username of the SecureChange user that we
  will be utilizing for the following examples. Please ensure that
  this user exists and has appropriate permissions for whatever
  workflows/tickets will be used.
- `SCW_API_PASSSWORD`: The password of the SecureChange user that we
  will be utilizing for the following examples.

Other Articles
==============================================
[Setup Jupyter](./docs/Jupyter%20Notebook%20Setup.md)
[Basic Trigger Example](./docs/Basic%20Trigger%20.md)
[Basic Usage Example](./docs/Basic%20Usage.ipynb)
[API Jupyter Notebook](./docs/pytos2-ce.ipynb)

Development
-----------
`pytos2` CE is under active development by the Tufin PSS team. Bug
and feature requests can created by
[opening a new issue](https://gitlab.com/tufinps/pytos2-ce/-/issues/new).

The versioning strategy is [semver](https://semver.org).

Support
-------
For additional `pytos2-ce` support or inquiries, please visit the
[pytos category of our Developer Community](https://community.tufin.com/c/pytos/11).
For sales or other general-purpose inquiries please contact your account manager or visit
[our contact page](https://www.tufin.com/contact-us).
