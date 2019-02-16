import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_docker_gc(host):
    crontask = host.file('/etc/cron.d/docker-gc')

    assert crontask.exists

    envvars = [
        'FORCE_IMAGE_REMOVAL',
        'FORCE_CONTAINER_REMOVAL',
        'MINIMUM_IMAGES_TO_SAVE',
        'GRACE_PERIOD_SECONDS',
    ]

    for envvar in envvars:
        assert crontask.contains(envvar)

    docker_gc = host.file('/usr/local/bin/docker-gc')

    assert docker_gc.exists
    assert docker_gc.is_symlink
