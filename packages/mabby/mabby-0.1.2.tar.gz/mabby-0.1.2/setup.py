# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mabby', 'mabby.strategies']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.7.0,<4.0.0', 'numpy>=1.24.2,<2.0.0', 'overrides>=7.3.1,<8.0.0']

setup_kwargs = {
    'name': 'mabby',
    'version': '0.1.2',
    'description': 'A multi-armed bandit (MAB) simulation library',
    'long_description': '<h1 align="center">\n<img src="https://raw.githubusercontent.com/ew2664/mabby/main/assets/mabby-logo-title.png" width="500">\n</h1>\n\n[![PyPI](https://img.shields.io/pypi/v/mabby)](https://pypi.org/project/mabby/)\n[![license](https://img.shields.io/github/license/ew2664/mabby)](https://github.com/ew2664/mabby/blob/main/LICENSE)\n[![issues](https://img.shields.io/github/issues/ew2664/mabby)](https://github.com/ew2664/mabby/issues)\n[![build](https://img.shields.io/github/actions/workflow/status/ew2664/mabby/build.yml)](https://github.com/ew2664/mabby/actions/workflows/build.yml)\n[![docs](https://img.shields.io/github/actions/workflow/status/ew2664/mabby/docs.yml?label=docs)](https://ew2664.github.io/mabby/)\n[![coverage](https://coveralls.io/repos/github/ew2664/mabby/badge.svg)](https://coveralls.io/github/ew2664/mabby)\n\n**mabby** is a library for simulating [multi-armed bandits (MABs)](https://en.wikipedia.org/wiki/Multi-armed_bandit), a resource-allocation problem and framework in reinforcement learning. It allows users to quickly yet flexibly define and run bandit simulations, with the ability to:\n\n- choose from a wide range of classic bandit algorithms to use\n- configure environments with custom arm spaces and rewards distributions\n- collect and visualize simulation metrics like regret and optimality\n\n## Installation\n\nPrerequisites: [Python 3.9+](https://www.python.org/downloads/) and `pip`\n\nInstall **mabby** with `pip`:\n\n```bash\npip install mabby\n```\n\n## Basic Usage\n\nThe code example below demonstrates the basic steps of running a simulation with **mabby**. For more in-depth examples, please see the [Usage Examples](https://ew2664.github.io/mabby/examples/) section of the **mabby** documentation.\n\n```python\nimport mabby as mb\n\n# configure bandit arms\nbandit = mb.BernoulliArm.bandit(p=[0.3, 0.6])\n\n# configure bandit strategy\nstrategy = mb.strategies.EpsilonGreedyStrategy(eps=0.2)\n\n# setup simulation\nsimulation = mb.Simulation(bandit=bandit, strategies=[strategy])\n\n# run simulation\nstats = simulation.run(trials=100, steps=300)\n\n# plot regret statistics\nstats.plot_regret()\n```\n\n## Contributing\n\nPlease see [CONTRIBUTING](https://ew2664.github.io/mabby/contributing/) for more information.\n\n## License\n\nThis software is licensed under the Apache 2.0 license. Please see [LICENSE](https://ew2664.github.io/mabby/license/) for more information.\n',
    'author': 'Ethan Wu',
    'author_email': 'ew2664@columbia.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
