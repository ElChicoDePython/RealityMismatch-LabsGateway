

class Action:
    def install(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def uninstall(self):
        pass


class CreateNetwork(Action):
    pass


class CreateContainer(Action):
    pass


def parse_request(data):
    """Given a JSON data structure return the actions to be performed inside
    the platform"""

    actions = []

    network_names = set()

    for network in data.get('networks', []):
        network_name = network['name']
        if network_name not in network_names:
            network_names.add(network_name)
            actions.append(
                CreateNetwork(name=network_name)
            )

    for lab in data['labs']:
        if lab['type'] == 'docker':
            actions.append(
                CreateContainer(
                    image=lab['image'],
                    network=lab.get('network')
                )
            )
        else:
            raise Exception(f'Lab type {lab[type]} not supported currently')

    return actions
