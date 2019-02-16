ansible-role-docker-gc
=========

Install and configure [docker-gc](https://github.com/spotify/docker-gc).

Role Variables
--------------

- `docker_gc_version` Git commit SHA1 from [docker-gc](https://github.com/spotify/docker-gc).
- `docker_gc_installdir` Install directory path (default: `/opt/docker-gc`).
- `docker_gc_exclude` List of Docker images excluded from garbage collection (default: `[]`).
- `docker_gc_exclude_containers` List of Docker containers excluded from garbage collection (default: `[]`).
- `docker_gc_exclude_volumes` List of Docker volumes excluded from garbage collection (default: `[]`).
- `docker_gc_force_image_removal` Delete Docker images if it's tagged in multiple repositories (default: `false`).
- `docker_gc_force_container_removal` Force deletion of Docker containers (default: `false`).
- `docker_gc_minimum_images_to_save` The minimum number of images you want to keep (default: `0`).
- `docker_gc_grace_period_seconds` Remove Docker container older than X seconds (default: `3600`).
- `docker_gc_cron_file` The name of cron.d task file (default: `docker-gc`).
- `docker_gc_cron_special_time` The frequency of cron.d task execution (default: `daily`).

Dependencies
------------

- [geerlingguy.docker](https://github.com/geerlingguy/ansible-role-docker)

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: jenkins
      become: true
      become_method: sudo
      roles:
         - ebury.docker-gc

License
-------

BSD

Author Information
------------------

[Ebury](https://labs.ebury.rocks) Infrastructure Operations

