# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aws_assumptions']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.26']

entry_points = \
{'console_scripts': ['assumptions = aws_assumptions.scripts:main']}

setup_kwargs = {
    'name': 'aws-assumptions',
    'version': '0.1.0',
    'description': 'Easily export env vars for assuming AWS roles using STS Assume Role',
    'long_description': '# aws-assumptions\n\nEasily switch between roles, or a chain of roles and create boto3 clients and resources off of those assumed identities.\nAlong with being able to use this package as an import a cli script is included.\n\n## CLI Usage\n\nAvailable commands\n```\n~  > assumptions -h\nusage: assumptions [-h] {whoami,assume} ...\n\npositional arguments:\n  {whoami,assume}\n\noptional arguments:\n  -h, --help       show this help message and exit\n\nSwitch roles, or through a chain or roles, or print identity information from AWS STS\n```\n\nGetting current identity\n```\n> assumptions whoami -h\nusage: assumptions whoami [-h]\n\noptional arguments:\n  -h, --help  show this help message and exit\n\nPrints get-caller-identity info in JSON format\n```\n\nAssuming a role\n```\n~  > assumptions assume -h\nusage: assumptions assume [-h] -r ROLE_ARN [-n ROLE_SESSION_NAME] [-p POLICY_ARN] [-t TAG] [-T TRANSITIVE_TAG_KEY] [-E EXTERNAL_ID] [-d DURATION_SECONDS] [-e]\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -r ROLE_ARN, --role-arn ROLE_ARN\n                        Role to assume. If declared multiple times each role will assume the next in the order given. All other options will be applied to all roles in the chain.\n  -n ROLE_SESSION_NAME, --role-session-name ROLE_SESSION_NAME\n                        The session name to use with the role.\n  -p POLICY_ARN, --policy-arn POLICY_ARN\n                        Optional policy to attach to a session. Can be declared multiple times.\n  -t TAG, --tag TAG     Optional tag to add to the session in the format of `mytagkey=myvalue`. Can be declared multiple times for multiple tags.\n  -T TRANSITIVE_TAG_KEY, --transitive-tag-key TRANSITIVE_TAG_KEY\n                        Transitive tag key. Can be declared multiple times.\n  -E EXTERNAL_ID, --external-id EXTERNAL_ID\n                        Optional External ID for the session. Required by some AssumeRole policies\n  -d DURATION_SECONDS, --duration-seconds DURATION_SECONDS\n                        Optional duration for the session.\n  -e, --env-vars        Output env vars usable from a terminal. If not set the output will match the output of aws-cli\'s `aws sts assume-role` JSON\n\nAssume a role or a chain of roles with optional attributes, outputting the newly acquired credentials. Maintains parity with boto3\'s sts.assume_role except for MFA\n```\n\nExample of assuming a role with env vars\n```\n> assumptions assume -r "arn:aws:iam::123456789876:role/my-role" -n bob@nowhere.com -e > creds.env\n> . creds.env\n```\n\nor\n\n```\n$(assumptions assume -r "arn:aws:iam::123456789876:role/my-role" -n bob@nowhere.com)\n```\n\n## Switching through multiple roles\nIf you need to chain roles (EG: Assume a role that assumes a role that assumes a role) you can pass the `-r` flag multiple times.\nNote however that all other options, such as `--external-id` or `--tag` will be applied to every session in the chain.\n\n## As a library\n\nAssuming a role and creating clients\n```python\nfrom aws_assumptions.identity import Identity\n\nsession = Identity(\n  RoleArn="arn:aws:iam::123456789876:role/my-role",\n  RoleSessionName="bob"\n)\n\nres = session.client("eks").list_clusters()\ncurrent_role = session.whoami()\nsession_that_made_current_rule = session.whomademe()\n```\n\nChaining roles\n\n```python\nfrom aws_assumptions.identity import Identity\n\nsession = Identity(\n  RoleArn=[\n    "arn:aws:iam::123456789876:role/my-role",\n    "arn:aws:iam::123456789876:role/my-second-role"\n  ],\n  RoleSessionName="bob"\n)\n\nres = session.client("eks").list_clusters()\ncurrent_role = session.whoami()\nsession_that_made_current_rule = session.whomademe()\n```\n\n',
    'author': 'Mathew Moon',
    'author_email': 'me@mathewmoon.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mathewmoon/aws-assumptions',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
